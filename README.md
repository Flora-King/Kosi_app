# KOSI

## Table of contents

1. [Helpful links](#helpful-links)
2. [Introduction](#introduction)
    - [Scope](#scope)
3. [UX Design](#ux-design)
    - [Wireframes](#wireframes)
    - [Colour palette](#colour-palette-used)
    - [Data Diagram](#data-schema)
4. [Features](#features)
5. [User Stories](#user-stories)
6. [Templates](#templates)
7. [Technologies used](#technologies-used)
8. [Testing](#testing)
    - [Usability Testing](#usability-testing)
    - [Code validation](#code-validation)
    - [Features testing](#features-testing)
    - [Bugs](#bugs-and-issues-encountered)
        - [Unresolved issues](#unresolved-errorsissues)
9. [Deployment](#deployment)
10. [References](#references)


### Helpful links

- [Live website](https://kosi-app-9673f8ad46df.herokuapp.com/)
- [GitHub Repository](https://github.com/Flora-King/Kosi_app)
- [The README.md file](https://github.com/Flora-King/Kosi_app)
- [Project Board](https://github.com/Flora-King/Kosi_app/projects?query=is%3Aopen)
- [Manual Testing](https://github.com/Flora-King/Kosi_app)
- [Tasks](https://github.com/Flora-King/Kosi_app)
- [Wireframes](https://github.com/Flora-King/Kosi_app)

***

## INTRODUCTION
*`Kosi`* is a website app aimed at those looking to book courses. In this instance,

This website app provides an opportunity to users looking for short IT and computer programming courses.

**TARGETED USERS:**
* people interested in taking courses 
* people of any age with preference for either online and/or in person course delivery

### SCOPE

`The scope` for the Kosi web app 

* Viewing course content whether logged in or not
* Adding a review when logged in 
* Adding a rating when logged in 
* Updating and Deleting own reviews before approval


## UX DESIGN

![Kosi web app appearance on all devices](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/0b9a8253-e2ea-43cc-80c6-d059f3cdcf58)

### Wireframes
The Kosi web app has been built with a simple but highly impactful design.

Below are the wireframes I created to aid the initial concept layout planning.

![Navbar wireframe](https://github.com/Flora-King/fancy-trivia/assets/106548101/4a1b7c02-811a-4422-8f6a-90e2d26c2505)

![Register page wireframe](https://github.com/Flora-King/fancy-trivia/assets/106548101/f971bb81-0ee2-4efc-a71d-2835383a3b22)

![login page - wireframe](https://github.com/Flora-King/fancy-trivia/assets/106548101/e78c9f75-c7c2-497b-99e5-042c74223444)

![Course List page wireframe](https://github.com/Flora-King/fancy-trivia/assets/106548101/b845375d-2978-4c06-a4d4-f7301226e356)

![Course content page wireframe](https://github.com/Flora-King/fancy-trivia/assets/106548101/5d89cbbf-7535-4888-b8ab-b903060595b5)

### Colour palette used
I chose to use the colour palette below in order to give my web app a simple but trendy look so as to expand its appeal.

![Colour palette](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/75a997e0-f335-480a-af08-41e69e1b4ab3)

### Data Schema 

The Diagram illustrates the data relationship between the three main entities /models on which the Kosi web app is founded.

![ERD Diagram](https://github.com/Flora-King/fancy-trivia/assets/106548101/f41d529a-f8f5-4c07-8a18-e6f134576462)

## FEATURES

To achieve the goals and scope of this project, I have implemented the following features

1. **Navigation**
    - the navigation for the Kosi web app is very simple and easy. it is made simple to ensure complete ease of use by anyone using any type of device.
    - the navigation bar has the following
        - Kosi Logo - when clicked, routes the user to the courses list page 
        - Courses - when clicked, routes the user to the courses list page
        - Login - when clicked routes the user to the login page
        - Register - when clicked routes the user to the Sign-up page

![Navbar and Footer](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/b33b1e84-b5ba-43d0-b47a-33d5e24e1e74)

2. **Registration**
- To register, the user can click on the Register button in the navigation bar or use the Sign-Up button located on the login page

![Register Page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/d386763d-e8ce-4759-bf45-54db997b4e9b)

3. **Logging in**
- To login, the user can click on the Login button in the navigation bar; or use the login button located on the Sign-Up page or one on the course content page

![Log in page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/e0140b77-f666-4e32-b32b-d9cf02fe5fa3)

4. **Creating a review and adding a rating**
- To create a review/add a rating, the user needs to log in first and navigate to the bottom of their chosen course content page

![Newly created review awaiting approval](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/9f74cdba-f63f-4799-b879-220e86d496ff)

5. **Viewing content**
- The courses page displays the course list where each course has an image, excerpt, price, delivery and delivery_date

![Course List](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/89d745cb-38eb-4534-bc05-c254cfb04f00)

    - further course content is accessible via the course content page when the user clicks on any course's excerpt
    - the user is able to view course content without logging in first
    - the user is also able to view approved reviews  and star ratings added against a course whether logged in or not

![Course content](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/e9c0712e-5084-4d4c-99e1-aeec512882f4)

6. **Updating reviews and star ratings**
- the user can only update their own reviews or star ratings
- to update reviews, the user needs to log in first and navigate to the bottom of their chosen course content page
- to update a review, the review must still be pending approval
- star ratings can be removed by the user without approval. However, the user must be logged into the web app.

![Reviews when logged in](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/50d1c8a1-12a1-4d7b-a2c8-9004a43be626)

![Updating a review awaiting approval](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/6e84bb21-d095-4cb4-b575-1861dada5871)

![Review update completed](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/ba5db783-f5be-488f-a2cc-73c42479ec15)

7. **Deleting reviews**
- the user can only delete their own reviews or remove star ratings they added
- to delete reviews, the user needs to log in first and navigate to the bottom of their chosen course content page
- to delete a review, the review must still be pending approval
- star ratings can be removed by the user without approval. However, the user must be logged into the web app.

![Ready to delete a review](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/d5bc7ad7-665b-4b9b-a995-8a0065820a53)

![Review successfully deleted](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/11f077be-be5c-49f5-a61d-342ba616a821)

8. **Viewing notifications/messages**

- I have added messages/notifications to be presented for up to 3 seconds to the user following the activities below

| Actions                           | Message                              |
|-----------------------------------|--------------------------------------|
| Successful log in                 | Successfully signed in as username   |
| Successful sign up                | successfully signed in as username   |
| log out                           | successfully logged out              |
| adding a review                   | Review awaiting check                |
| Successful updating a review      | Review Updated!                      |
| Unsuccessful updating of a review | Error updating review!               |
| deleting a review                 | Review deleted                       |

## USER STORIES

- The user stories below have also been elaborated with acceptance criteria in the [Project Board](https://github.com/Flora-King/Kosi_app/projects?query=is%3Aopen)

- Also linked **tasks** have been detailed in the [TASKS.md](/workspace/Kosi_app/StoriesandTasks.md)

| REF No | USER STORY TITLE            | USER STORY DESCRIPTION                                                                                                        | PRIORITY    | STATUS   | SCOPE  |
|--------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------|----------|--------|
| 18     | User login process          | As a site user I can log into the website so that I can add or update my reviews                                              | MUST HAVE   | DONE     | IN     |
| 10     | Account registration        | As a site user I can register an account so that I can have access to personal profile                                        | MUST HAVE   | DONE     | IN     |
| 15     | manage course content       | As a site admin I can create, read, update, and delete course content so that all the course content is up to date             | MUST HAVE   | DONE     | IN     |
| 16     | create draft course content | As a site admin I can create draft courses so that I can complete writing content later                                       | SHOULD HAVE | DONE     | IN     |
| 6      | View course details         | As a site user I can view course details so that I can view full course details                                               | SHOULD HAVE | DONE     | IN     |
| 4      | course list pagination       | As a site user I can navigate easily through the course list so that I can see all courses on different pages of the website | SHOULD HAVE | DONE     | IN     |
| 11     | add a star rating           | As a site user I can add rating stars against any course so that I share my star rating for a course                          | MUST HAVE   | DONE     | IN     |
| 12     | add a review                | As a site user I can add a review against any course so that I can share my experience                                        | MUST HAVE   | DONE     | IN     |
| 17     | approve posted reviews      | As a site admin I can approve or disapprove posted reviews so that I can remove subjective or rude commentary                 | MUST HAVE   | DONE     | IN     |
| 14     | view reviews                | As all users we can view course recommendations details against each course so that we can read reviews left by other users   | MUST HAVE   | DONE     | IN     |
| 13     | view star ratings           | As all users we can view star ratings against each course so that we can view courses by star rating                          | MUST HAVE   | DONE     | IN     |
| 7      | Register for a course       | As a site user I can register for a course so that I can attend that course                                                   | COULD HAVE  | NOT DONE | Future |
| 8      | View my booked courses      | As a site user I can view courses I have booked/registered for so that I am aware of my course schedule                       | COULD HAVE  | NOT DONE | Future |

## TEMPLATES

 **Templates** created for this web app include

- **base.html** - loads bootstrap and fonts and also contains structuring for the navigation and footer, plus also contains block content tags 
        [where content from the rest of the templates will be injected]

- **signup.html** - extends base.html and also has code to enable the user to create an account for accessing various areas of this web app

- **login.html** - extends base.html and also code to enable the user to log into the web app and add a review and/or a star rating

- **course_detail.html** - extends base.html and holds the course list and the course content details

- **index.html** -extends base.html and has a for loop that enables iteration through the courses.

## TECHNOLOGIES USED

* **HTML** - To create the Django templates for the associated views and models in the project applications.
* **CSS** - To style the website.
* **JavaScript** - To enable a dynamic update and delete functions for the user on reviews awaiting approval. And used to enable a timed appearance of the messages/notifications
* **Python** – Is the primary language of Django and used to create all forms, models and views.
* **Bootstrap** - To provide extra styling and out-of-the-box elements e.g., burger menu.
* **Google Fonts** - fonts used in the web app
* **ElephantSQL** - the database used to deploy the web app to Heroku
* **Cloudinary** - used to store images linked to the web app
* **W3C HTML Validator** - to validate the Html code generated from the page source of the web app
* **W3C CSS Validator** - to validate the CSS code used/applied to web app
* **JS Hint** - to validate the JavaScript code applied for this web app
* **CI Python Linter** to validate the python code used in this web app
* **Lighthouse** - to assess that the performance, accessibility and best practices applied in this web app are of higher quality.
* **lucid.app** - for wireframing

## TESTING 

### Usability testing

* **Responsive testing**

![Responsive Testing](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/0b9a8253-e2ea-43cc-80c6-d059f3cdcf58)

- Also tested how the different pages render on all different sized devices and found no issues at all.

* **Lighthouse Test Results**

![Lighthouse Testing](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/35568f2c-d9a1-4f28-89ff-afea8f299a13)

### Code Validation

* **W3C HTML Validator**

![image](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/6fc952d0-c360-4099-b757-32ee54861916)

The HTML validator also showed a warning regarding a *<hr>* tag that I used to create a separators between the course content and the reviews container. 
This doesn’t affect my code and therefore I have left it in.

![hr tag information](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/790e4c97-e549-4417-bf02-675b573c3162)

* **W3C CSS Validator**

![CSS Validation results](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/876fda07-960e-4353-ad05-cb41d5785ad2)

* **JS Hint**

![JavaScript code validation results](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/e7384ebb-4aa1-4688-b112-a16b62a26546)

- two undefined variables
    - **bootstrap** 
        - This loads bootstrap modal utilised in the course_detail.html template to facilitate the deletion of a review

    - **submitButton**
        - This variable in placed in course_detail.html template and it is an event listener

- one unused variable
    - **submitForm** 
        - this variable is used to submit a form once id of submitButton is identified

* **CI Python Linter**

![CI Python Linter results](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/c6ef26c5-daf0-4113-a5f1-f4c07f21a37b)

- the python code has no errors from the code i wrote personally. The two errors about long lines in settings.py were generated automatically when Django project was created.

### **Features Testing**

 All features have been tested as part of the **User stories testing**. 
 
 For a detailed view of the manual testing carried out for all the user stories, see [the MANUALTESTING.md file](https://github.com/Flora-King/Kosi_app)

### **Bugs and issues encountered**

1. The animations on the register and login pages didn't work when app was first deployed to Heroku.  
    
    - **solution** - added logo image to cloudinary and wrote added cloudinary link to CSS code for background image

![Animations did not load deployed to Heroku](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/686ad7d8-5534-4471-9e68-dbd0d8c690a4)

2. CSS style text was visible on course content page 

    - **solution** -manually removed the style text in admin site

![style code visible on front end app](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/5098b93f-4046-4c7c-acd5-149f2dc31811)

3. There were bad/low accessibility mainly due to images not having alt text 
    
    - **solution** - added title and alt text in meta data of each image in cloudinary

![Accessibility issues](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/3a2f73d2-981f-44f3-95e4-6297ba241779)

#### Unresolved errors/issues

4. *`JavaScript console error`* 

- this appears when user is not logged in and is on the course content page. 
- it can be solved by removing a line of code from the reviews.js file that makes sure that the reviews text area is emptied whenever a review is created or edited, and still awaiting approval.
- removing this line of code makes the usage of the web app aesthetically not pleasing and in fact can be confusing to the end user. So, I have chosen to leave it in as it is not currently breaking the web app

![JavaScript console bug](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/dc3d8a79-7aa8-4d29-bbf1-0d0f1bd643bc)

## DEPLOYMENT

1. ### Create Repository and set up project in GitHub

    - Create repository in GitHub using provided Code institute template
    - Create Project board and add automated workflow <to add user stories to the TO DO lane once created in issues with status=open>
    - Create user story template and apply it to create user stories
    - Add detailed acceptance criteria to all user stories and priority labels
    - Define the layout of the webapp using wireframing
    - Create tasks against each user story [in separate word document for reference and progress management during build]

2. ### initial setup of the project in gitpod

    - Install Django using (pip3 install 'django<4') command
    - Create project using (django-admin startproject Kosi .) command
    - create new app using (python3 manage.py startapp Kosi_app) command
    - Add new app to installed apps in settings.py
    - Add the following supporting libraries: postgres and psycopg2 - using (pip3 install psycopg2-binary) command
    - Create requirements.txt file - using (pip3 freeze --local > requirements.txt) command
    - Install webserver using (pip3 install gunicorn) command
    - Create the Procfile
    - Create env.py file and make sure it is part of .gitignore file content
        - Add all to requirements.txt
        - Make migrations and migrate 
        - Runserver to test set up and commit changes

3. ### set up external Database in ElephantSQL

    - Create account in ElephantSQL using GitHub login details
    - Create new instance with Europe as region
    - Take note of the url for use later when setting up Heroku app

4. ### set up Cloudinary storage for my images

    - Create Cloudinary account using GitHub login details
    - Take note of API and Secret key for use later

5. ### create Heroku app

    - Log into Heroku and create new app
    - Set Europe as region and connect Heroku app to GitHub repository for this project

6. ### connect remote database to Heroku app

    - From the Reveal config vars tab under settings module in Heroku, I added the keys below:
        - Elephant SQL database url, 
        - Cloudinary storage url,  
        - Postgres url, 
        - Secret key, 
        - Allowed host value,
        - Disablecollectstatic value

7. ### Continue development in gitpod workspace 
    - In settings.py file
        - Under installed apps, add Cloudinary app, postgres, crispy forms, summernote, et al. 
        - Amend default database url to point to database_url value already set up in Heroku
    
    - following the MTV [Models, Templates and Views] architectural guidance
        - Create views in the a views.py file
        - Create a models.py file and add models relating to the views
        - Create admin.py to manage the created models and views
        - Create templates folders and proceed to amend code as needed
        - Create forms.py file
        - Create a urls.py file and add urls relating to the above
        - Create static folder in the root directory to house CSS, js and images folders
        - Add JavaScript code for edit and delete buttons on reviews
        - Create superuser details to access admin site
    - add all to requirements.txt
    - make migrations and migrate 
    - runserver to test set up and commit changes            

8. ### Access admin site and create course content in admin site
    - Add course content 
    - check front end web app to ensure course data is presented as needed 
        - add all to requirements.txt
        - make migrations and migrate 
        - runserver to test set up and commit changes 

9. ### Continue to amend/tweak code in templates, urls and models in line with desired outcome  
    - add all to requirements.txt
    - make migrations and migrate 
    - runserver to test set up and commit changes 

10. ### Deploy to Heroku
    - ensure all code is structured and runs as desired
    - change DEBUG value to False
        - add all to requirements.txt
        - make migrations and migrate 
        - runserver to test set up and commit changes
    - log into Heroku app
    - delete value for DiSABLECOLLECTABLESTATICS
    - navigate to deploy tab and choose desired deployment method - manual or automatic 
    -   I chose to use manual deployment in order to monitor any rising errors before final deployment

11. ### Final deployment to Heroku

![complete before submission](WILL ADD LATER AFTER FEEDBACK BUT BEFORE SUBMISSION)


## REFERENCES

* Harry Dhillon - my code institute mentor provided a lot of guidance and advice
* Code institute tutors - were very helpful when it came to understanding issues I faced throughout the build
* Stackoverflow - used as a resource for guidance on any errors or issues I encountered
* followed the steps provided by the Code institute 'I Think therefore I Blog' walkthrough tutorial to build my web app
* reviewed several YouTube tutorials to understand how to execute certain functionalities in Django e.g. 
* reviewed and referenced the information from below resources for guidance during build
    - https://docs.djangoproject.com/en/
    - https://www.w3schools.com/
    - https://getbootstrap.com/docs/5.3/getting-started/introduction/
    - https://www.geeksforgeeks.org/  

