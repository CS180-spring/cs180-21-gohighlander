import urllib.request
import json
from datetime import datetime, timedelta
import os
import pytz
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

urls = ["https://streetsoncloud.com/parking/rest/occupancy/id/547",
        "https://streetsoncloud.com/parking/rest/occupancy/id/548",
        "https://streetsoncloud.com/parking/rest/occupancy/id/495",
        "https://streetsoncloud.com/parking/rest/occupancy/id/545",
        "https://streetsoncloud.com/parking/rest/occupancy/id/544",
        "https://streetsoncloud.com/parking/rest/occupancy/id/546",
        "https://streetsoncloud.com/parking/rest/occupancy/id/543"]
output_file = "static/parking.json"

data_by_lot = {}

# load existing data from file
if os.path.isfile(output_file):
    with open(output_file, "r") as infile:
        existing_data = json.load(infile)
else:
    existing_data = data_by_lot

# delete data that is 2 weeks old
two_weeks_ago = datetime.now(pytz.timezone('America/Los_Angeles')) - timedelta(days=14)
current_weekday = datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%A")

for url in urls:
    # retrieve JSON data from URL
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    json_data = json.loads(data[data.index("(") + 1:data.rindex(")")])

    # extract relevant information
    lot_name = json_data["results"][0]["location_name"]
    free_spaces = int(json_data["results"][0]["free_spaces"])
    total_spaces = json_data["results"][0]["total_spaces"]
    if free_spaces == "FULL":
        free_spaces = total_spaces
    current_date = datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%Y-%m-%d")
    current_hour = datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%H")
    print(free_spaces)
    # add new occupancy data to lot
    if lot_name in existing_data.get(current_weekday, {}):
        lot_data = existing_data[current_weekday][lot_name]

        if current_hour in lot_data:
            last_reset_date = pytz.timezone('America/Los_Angeles').localize(
                datetime.strptime(lot_data[current_hour]["last_reset_date"], "%Y-%m-%d"))
            if last_reset_date > two_weeks_ago:
                lot_data[current_hour]["free_spaces"] = int(
                    (lot_data[current_hour]["free_spaces"] + (
                                (free_spaces - lot_data[current_hour]["free_spaces"]) / lot_data[current_hour][
                            "collected_data"])))
                lot_data[current_hour]["collected_data"] += 1
            else:
                lot_data[current_hour] = {"last_reset_date": current_date, "free_spaces": free_spaces,
                                          "total_spaces": total_spaces, "collected_data": 1}
        else:
            lot_data[current_hour] = {"last_reset_date": current_date, "free_spaces": free_spaces,
                                      "total_spaces": total_spaces, "collected_data": 1}
    else:
        existing_data.setdefault(current_weekday, {})
        existing_data[current_weekday][lot_name] = {
            current_hour: {"last_reset_date": current_date, "free_spaces": free_spaces, "total_spaces": total_spaces,
                           "collected_data": 1}}

# write updated data to file
with open(output_file, "w") as outfile:
    json.dump(existing_data, outfile)