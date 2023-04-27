[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10809429&assignment_repo_type=AssignmentRepo)

# GoHighlander

 
 > Authors: [Kevin Qu](https://github.com/KevinDevs), [Wesley Fan](https://github.com/wesleyfan2015), [Haolin Liu](https://github.com/terrylhl), [Tiffany Wang](https://github.com/twang0323)



## Project Description
A web app that saves students’ schedule information into an easy-to-read schedule and gathers parking lot occupancy each hour during weekdays to display an occupancy forecast. The project is important to us because as college students we need to be organized as we need to drive to school for classes, discussions, exams, etc. Students who use this program would be able to stay organized and thus be able to keep their focus on their eductation. It will be interesting to see how to develop new features from a user's perspective. The languages/tools/technologies we plan to use are:
* Python - Primary Programming language we use in this project
* PHP - General-purpose scripting language geared toward web development
* HTML - Hypertext markup language, the system for displaying material retrieved over the Internet
* CSS - Style our HTML document by describing the presentation of Web pages, including colors, layout, and fonts
* JS (JavaScript) - types and operators, standard built-in objects, and methods
* Vue - Progressive framework for building user interfaces
* GitHub - A code hosting platform for version control and collaboration
* Git - Version control system
* Frontend Languages: HTML, CSS, JS, Vue


Features:
* Login and logout of account
* Get help for changing password
* Delete account permanentley.
* Add new courses for schedule
* Delete new courses for schedule
* Set full schedule
* Save schedule and access through all devices
* Check avaliable parking spaces
* Added web application to home screen for easy access


## Interface Documentation

### Frontend Interfaces:

`index.php` - Dashboard for this app, displays links to pages

`login.php` - Login page for users

`register.php` - Registration page for users

`my_schedule.php` - Displays courses in order for each day of the week

`add_course.php` - Allows users to add courses to their schedule

`manage_schedule.php` - Allows users to delete added schedule from the courses list


### Backend Interfaces:
| URL  | Method  | Request Params  |  Responses |  Description |
| ------------ | ------------ | ------------ | ------------ | ------------ |
|  /api/check_session |  GET |  - | `yes`/`no`  | Returns yes or no, if the user is logged in  |
| /api/login.php  | POST  | name, password  | `logged_in` / error_msg   | Returns logged_in on success and error message if failed  |
|  /api/register.php |  POST | name, password  | `success`/error_msg  | Returns success on success and error message if failed.  |
| /api/get_schedule.php  |  GET | -  | courses_gzipped  | Returns gzipped course informations in JSON  |
| /api/save_schedule.php  | POST  | sh  | `success`  | Saves Gzipped courses into JSON database returns success if saved correctly  |


 ## Screenshots
 ![Screenshots](https://raw.githubusercontent.com/CS180-spring/cs180-21-gohighlander/main/screenshots/cs180.jpg)
 ## Installation/Usage
 > pip install -r requirements.txt
 
 > pip main.py
 ## Testing
 > TBD

