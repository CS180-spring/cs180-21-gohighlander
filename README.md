[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10809429&assignment_repo_type=AssignmentRepo)

# GoHighlander

 
 > Authors: [Kevin Qu](https://github.com/KevinDevs), [Wesley Fan](https://github.com/wesleyfan2015), [Haolin Liu](https://github.com/terrylhl), [Tiffany Wang](https://github.com/twang0323)



## Project Description
A web app that saves students’ schedule information into an easy-to-read schedule and gathers parking lot occupancy each hour during weekdays to display an occupancy forecast.

## Interface Documentation

### Frontend Interfaces:

`index.php` - Dashboard for this app, displays links to pages

`login.php` - Login page for users

`register.php` - Registration page for users

`my_schedule.php` - Displays courses in order for each day of the week

`add_course.php` - Allows users to add courses to their schedule

`manage_schedule.php` - Allows users to delete added schedule from the courses list


### Backend Interfaces:

`/api/check_session` - returns yes or no, if the user is logged in

`/api/login.php` - takes two POST parameters: `name` and `password`. returns `logged_in` on success and error message if failed.

`/api/register.php` - takes two POST parameters: `name` and `password`, returns `success` on success and error message if failed.

`/api/get_schedule.php` - accepts GET request, and returns gzipped course informations in JSON

`/api/save_schedule.php` - accepts POST request with parameter `sh`, returns success if saved correctly.

> Note: This web application is written using python Flask, the `.php` file extension acts as a disguise.


 ## Screenshots
 ![Screenshots](https://raw.githubusercontent.com/CS180-spring/cs180-21-gohighlander/main/screenshots/cs180.jpg)
 ## Installation/Usage
 > pip install -r requirements.txt
 
 > pip main.py
 ## Testing
 > TBD

