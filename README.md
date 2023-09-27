# KOSI

## Table of contents

1. [Introduction](#introduction)
    - [Scope](#scope)
2. [UX Design](#ux-design)
    - [Wiframes](#wireframes)
    - [Colour palette](#colour-palette-used)
    - [Data Diagram](#data-schema)
3. [Features](#features)
4. [User Stories](#user-stories)
5. [Templates](#templates)
5. [Technologies used](#technologies-used)
6. [Testing](#testing)
    - [Usability Testing](#usability-testing)
    - [Code validation](#code-validation)
    - [Features testing](#features-testing)
    - [Bugs](#bugs-and-issues-encountered)
        - [Unresolved issues](#unresolved-errorsissues)
7. [Deployment](#deployment)
8. [References](#references)



**Helpful links**

- [Live website](https://kosi-app-9673f8ad46df.herokuapp.com/)
- [Github repository](https://github.com/Flora-King/Kosi_app)
- [The README.md file](https://github.com/Flora-King/Kosi_app)
- [Project board](https://github.com/Flora-King/Kosi_app/projects?query=is%3Aopen)
- [Manual testing write up](https://github.com/Flora-King/Kosi_app)
- [Wireframes](https://github.com/Flora-King/Kosi_app)

***

## INTRODUCTION
*`Kosi`* is a website app aimed at those looking to book courses. In this instance,

This website app provides an opportunity to users looking for short IT and computer programming courses.

**TARGETED USERS:**
* people interested in taking courses 
* people of any age with preference for either online and/or in person course delivery

### SCOPE

`The original scope` for the Kosi web app was to build and deliver a course booking webapp where users can

* View course content [whether logged in or not]
* Add a review 
* Add a rating
* Edit and Delete content
* search through the course list
* add desired courses to a basket for purchasing immediately or save and return later
* view purchases courses in personal profile when logged in

However, due to time and resources, the `current scope` has been reduced to 

* Read course content [whether logged in or not]
* Add a review 
* Add a rating
* Edit content
* Delete content

**A reduced scope does not mean a less useful and/or impactful web app but rather one whose delivery is manageable within the given time. 
And it is my hope that this built web app will form a foundation for future web app whose functionality will be extended to fullfill the original scope.**


## UX DESIGN

### Wireframes
The Kosi web app has been built with a very simple but highly impactful design.

Below are the wireframes i created to aid the initial concept layout planning.

![Navbar wireframe](https://github.com/Flora-King/fancy-trivia/assets/106548101/4a1b7c02-811a-4422-8f6a-90e2d26c2505)

![Register page wireframe](https://github.com/Flora-King/fancy-trivia/assets/106548101/f971bb81-0ee2-4efc-a71d-2835383a3b22)

![login page - wireframe](https://github.com/Flora-King/fancy-trivia/assets/106548101/e78c9f75-c7c2-497b-99e5-042c74223444)

![Course List page wireframe](https://github.com/Flora-King/fancy-trivia/assets/106548101/b845375d-2978-4c06-a4d4-f7301226e356)

![Course content page wireframe](https://github.com/Flora-King/fancy-trivia/assets/106548101/5d89cbbf-7535-4888-b8ab-b903060595b5)


### Colour palette used
I chose to use the color palette below in order to give my web app a simple but trendy look that would appeal to alot of users whether trendy or not.

![Colour palette](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/75a997e0-f335-480a-af08-41e69e1b4ab3)

### Data Schema 

The Diagram illustrates the data relationship between the three main entities /models on which the kosi web app is founded.

![ERD Diagram](https://github.com/Flora-King/fancy-trivia/assets/106548101/f41d529a-f8f5-4c07-8a18-e6f134576462)

## FEATURES

To achieve the goals and scope of this project, i have implemented the following features

1. **`Navigation`**
    - the navigation for the Kosi web app is very simple and easy. it is made simplae to ensure complete ease of use by anyone using any type of device.
    - the navigation bar has the following
        - Kosi Logo - when clicked, routes the user to the courses list page 
        - Courses - when clicked, routes the user to the courses list page
        - Login - when clicked routes the user to the login page
        - Register - when clicked routes the user to the Sign up page

![Nav bar and footer](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/b33b1e84-b5ba-43d0-b47a-33d5e24e1e74)

2. **`Registration`**
- To register, the user can click on the Register button in the navigation bar or use the Sign Up button located on the login page

![Register Page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/d386763d-e8ce-4759-bf45-54db997b4e9b)

3. **`Logging in`**
- To login, the user can click on the Login button in the navigation bar; or use the login button located on the Sign Up page or one on the course content page

![Log in page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/e0140b77-f666-4e32-b32b-d9cf02fe5fa3)


4. **`Creating a review/add a rating`**
- To create a review/add a rating, the user needs to log in first and navigate to the bottom of their chosen course content page

![newly created review awating approval](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/9f74cdba-f63f-4799-b879-220e86d496ff)

5. **`Viewing content`**
- The courses page displays the course list where each course has an image, excerpt, price, delivery and delivery_date

![Course List](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/89d745cb-38eb-4534-bc05-c254cfb04f00)

    - further course content is accessible via the course content page when the user clicks on any course's excerpt
    - the user is able to view course content without logging in first
    - the user is also able to view approved reviews  and star ratings added against a course whether logged in or not

![Course content](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/e9c0712e-5084-4d4c-99e1-aeec512882f4)

6. **`Updating content`**
- the user can only update their own reviews or star ratings
- to update reviews, the user needs to log in first and navigate to the bottom of their chosen course content page
- to update a review, the review must still be pending approval
- star ratings can be removed by the user without approval. However, the user must be logged into the web app.

![Reviews when logged in](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/50d1c8a1-12a1-4d7b-a2c8-9004a43be626)

![Updating a review awaiting approval](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/6e84bb21-d095-4cb4-b575-1861dada5871)

![Review update completed](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/ba5db783-f5be-488f-a2cc-73c42479ec15)

7. **`Deleting content`**
- the user can only delete their own reviews or remove star ratings they added
- to delete reviews, the user needs to log in first and navigate to the bottom of their chosen course content page
- to delete a review, the review must still be pending approval
- star ratings can be removed by the user without approval. However, the user must be logged into the web app.

![Ready to delete a review](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/d5bc7ad7-665b-4b9b-a995-8a0065820a53)

![Review successfully deleted](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/11f077be-be5c-49f5-a61d-342ba616a821)

8. **`Viewing notifications/messages`**
- I have added messages/notifications to be presented for upto 3 seconds to the user following the activities below

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

- The user stories below have also been elaborated with acceptance criteria in the [Project board](https://github.com/Flora-King/Kosi_app/projects?query=is%3Aopen)

- Also linked `**tasks**` have been detailed in the [Stories and Tasks file](/workspace/Kosi_app/StoriesandTasks.md)

| REF No | USER STORY TITLE            | USER STORY DESCRIPTION                                                                                                        | PRIORITY    | STATUS   | SCOPE  |
|--------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------|----------|--------|
| 18     | User login process          | As a site user I can log into the website so that i can add or update my reviews                                              | MUST HAVE   | DONE     | IN     |
| 10     | Account registration        | As a site user I can register an account so that i can have access to personal profile                                        | MUST HAVE   | DONE     | IN     |
| 15     | manage course content       | As a site admin I can create, read, update, and delete course content so that all the course content is upto date             | MUST HAVE   | DONE     | IN     |
| 16     | create draft course content | As a site admin I can create draft courses so that i can complete writing content later                                       | SHOULD HAVE | DONE     | IN     |
| 6      | View course details         | As a site user I can view course details so that i can view full course details                                               | SHOULD HAVE | DONE     | IN     |
| 4      | couse list pagination       | As a site user I can naviigate easily through the course list so that i can see all courses on different pages of the website | SHOULD HAVE | DONE     | IN     |
| 11     | add a star rating           | As a site user I can add rating stars against any course so that i share my star rating for a course                          | MUST HAVE   | DONE     | IN     |
| 12     | add a review                | As a site user I can add a review against any course so that i can share my experience                                        | MUST HAVE   | DONE     | IN     |
| 17     | approve posted reviews      | As a site admin I can approve or disapprove posted reviews so that i can remove subjective or rude commentary                 | MUST HAVE   | DONE     | IN     |
| 14     | view reviews                | As a all users I can view course recommendations details against each course so that i can read reviews left by other users   | MUST HAVE   | DONE     | IN     |
| 13     | view star ratings           | As a all users I can view star ratings against each course so that i can view courses by star rating                          | MUST HAVE   | DONE     | IN     |
| 7      | Register for a course       | As a site user I can register for a course so that i can attend that course                                                   | COULD HAVE  | NOT DONE | Future |
| 8      | View my booked courses      | As a site user I can view courses i have booked/registered for so that i am aware of my course schedule                       | COULD HAVE  | NOT DONE | Future |


## TEMPLATES

 **Templates** created for this web app include

- **base.html** - loads bootstrap and fonts and also contains structuring for the navigation and footer, plus also contains block content tags 
        [where content from the rest of the templates will be injected]

- **signup.html** - extends base.html and also has code to enable the user to create an account for accessing various areas of this web app

- **login.html** - extends base.html and also code to enable the user to log into the web app and add a review and/or a star rating

- **course_detail.html** - extends base.html and holds the course list and the course content details

- **index.html** -extends base.html and has a forloop that enables iteration through the courses.


## TECHNOLOGIES USED

* **HTML** - To create the Django templates for the associated views and models in the project applications.
* **CSS** - To style the website.
* **JavaScript** - To enable a dynamic update and delete functions for the user on reviews awaiting approval. Also used to enable a timed appearance of the messages/notifications
* **Python** – Is the primary language of Django and used to create all forms, models and views.
* **Bootsrap** - To provide extra styling and out-of-the-box elements e.g. burger menu.
* **Google Fonts** - fonts used in the web app
* **ElephantSQL** - the database used to deploy the web app to Heroku
* **Cloudinary** - used to store images linked to the web app
* **W3C HTML Validator** - to validate the Html code generated from the page source of the web app
* **W3C CSS Validator** - to validate the css code used/appled to web app
* **JS Hint** - to validate the javascript code appled for this web app
* **CI Python Linter** to validate the python code used in this web app
* **Lighhouse** - to assess that the perfomance, accessiblity and best practices applied in this web app are of higher quality.
* **lucid.app** - for wireframing

## TESTING 

### Usability testing

* **Responsive testing**
- used Dev tools to tetsing how the different data and pages render on all different sized devices and found no issues at all.
![Responsive Testing](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/0b9a8253-e2ea-43cc-80c6-d059f3cdcf58)

* **Lighthouse Test Results**

![Lighthouse Testing](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/35568f2c-d9a1-4f28-89ff-afea8f299a13)


### Code Validation

* **W3C HTML Validator**

![image](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/6fc952d0-c360-4099-b757-32ee54861916)

The HTML validator also showed a warning regarding a *<hr>* tag that i used to create a separators between the course content and the reviews container. 
This doesnt affect my code and therefore i have left it in.

![hr tag information](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/790e4c97-e549-4417-bf02-675b573c3162)

* **W3C CSS Validator**

![CSS Validation results](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/876fda07-960e-4353-ad05-cb41d5785ad2)

* **JS Hint**

![Javascript code validation results](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/e7384ebb-4aa1-4688-b112-a16b62a26546)

- two undefined variables
    - **bootsrap** 
        - This loads bootsrap modal utilised in teh course_detail.html template to facilitate the deletion of a review

    - **submitButton**
        - This variable in placed in course_detail.html template and it is an event listener

- one unused variable
    - **submitForm** 
        - this variable is used to submit a form once id of submitButton is identified

* **CI Python Linter**

![CI Python Linter results](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/c6ef26c5-daf0-4113-a5f1-f4c07f21a37b)

- the python code has no errors except for the two long lines that i am aware of and are not affecting my code. I have tried breaking them up but that just broke my code, so decided to leave them 

* **Chrome Devtools**

![Javascript code error in Devtools console](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/915f0b06-bb28-4641-8983-dc755b2667ed)

### **Features Testing**

 All features have been tested as part of the **User stories testing**. 
 
 For a detailed view of the manual tests carried out for all the user stories, see [the ManualTestswriteup.md file](https://github.com/Flora-King/Kosi_app)

### **Bugs and issues encountered**

1. The animations on the register and login pages didn't work when app was first deployed to Heroku.  
    
    - **solution** - added logo image to cloudinary and wrote added cloudinary link to css code for background image

![Animations didnt load when app deployed to Heroku](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/686ad7d8-5534-4471-9e68-dbd0d8c690a4)

2. css style text was visible on course content page 

    - **solution** -manaually removed the style text in admin site

![style code visible on front end app](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/5098b93f-4046-4c7c-acd5-149f2dc31811)


3. There were bad/low accessibility mainly due to images not having alt text 
    
    - **solution** - added title and alt text in meta data of each image in cloudinary

![Accessibility issues](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/3a2f73d2-981f-44f3-95e4-6297ba241779)

#### Unresolved errors/issues

4. *`Pep8 problems`* 
    - there are two errors that relate to the need for installation of "Jupyter" extension in VS Code which is ot a requirement for this project. Also they are not causing any issues at the moment for my project so have chosen to leave them

![pep8 errors](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/600218cd-b6cd-47f7-a31d-6e815831a373)

5. *`Javascript console error`* 

- this appears when user is not logged in and is on the course content page. 
- it can be solved by removing a line of code from the reviews.js file that makes sure that the reviews textarea is emptied whenever a review is created or edited, and still awaiting approval.
- removing this line of code makes the usage of the web app aesthetically not pleasing and in fact can be confusing to the end user. So, i have chosen to leave it in as it is not currently breaking the web app

![Javascript console bug](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/dc3d8a79-7aa8-4d29-bbf1-0d0f1bd643bc)

## DEPLOYMENT

1. ### Create Repository and set up project in GitHub

    - Create repository in Github using provided Code institute template
    - Create Project board and add automated workflow <to add user stories to the TO DO lane once created in issues with status=open>
    - Create user story template and apply it to create user stories
    - Add detailed acceptance criteria to all user stories and priority labels
    - define the layout of the webapp using wireframing
    - create tasks against each user story [in separate word document for reference and progress management during build]

2. ### initial setup of the project in gitpod

    - Install Django using (pip3 install 'django<4') command
    - Create project using (django-admin startproject Kosi .) command
    - create new app using (python3 manage.py startapp Kosi_app) command
    - add new app to installed apps in settings.py
    - Add the following supporting libraries: postgres and psycopg2 - using (pip3 install psycopg2-binary) command
    - create requirements.txt file - using (pip3 freeze --local > requirements.txt) command
    - install webserver using (pip3 install gunicorn) command
    - create the Procfile
    - Create env.py file and make sure it is part of .gitignore file content
        - add all to requirements.txt
        - make migrations and migrate 
        - runserver to test set up and commit changes

3. ### set up external Database in ElephantSQL

    - Create account in ElephantSQL using github login details
    - Create new instance with Europe as region
    - Take note of the url for use later when sett ing up Heroku app

4. ### set up Cloudinary storage for my images

    - Create Cloudinary account using github login details
    - Take note of API and Secret key for use later

5. ### create Heroku app

    - log into Heroku and create new app
    - Set Europe as region and connect Heroku app to github repository for this project

6. ### connect remote database to Heroku app

    - From the Reveal config vars tab under settings module in Heroku, i added the keys below:
        - Elephant SQL database url, 
        - cloudinary storage url,  
        - postgres url, 
        - secret key, 
        - allowed host value,
        - Disablecollectstatic value

7. ### Continue development in gitpod workspace 
    - in settings.py file
        - under installed apps, add Cloudinary app, postgres, crispy forms, summernote, et al. 
        - Amend default database url to point to database_url value already set up in Heroku
    
    - following the MTV [Models, Templates and Views] architectural guidance
        - Create views in the a views.py file
        - create a models.py file and add models relating to the views
        - create admin.py to manage the created models and views
        - create templates folders and proceed to amend code as needed
        - create forms.py file
        - create a urls.py file and add urls relating to the above
        - create static folder in the root directory to house css, js and images folders
        - add javascript code for edit and delete buttons on reviews
        - create superuser details to access admin site
    - add all to requirements.txt
    - make migrations and migrate 
    - runserver to test set up and commit changes            

8. ### Access admin site and create course content in admin site
    - add course content 
    - check front end web app to ensure course data is presented as needed 
        - add all to requirements.txt
        - make migrations and migrate 
        - runserver to test set up and commit changes 

9. ### Continue to amend/tweak code in templates, urls and models in line with desired outcome	
    - add all to requirements.txt
    - make migrations and migrate 
    - runserver to test set up and commit changes 

10.	### Deploy to Heroku
    - ensure all code is structured and runs as desired
    - change DEBUG value to False
        - add all to requirements.txt
        - make migrations and migrate 
        - runserver to test set up and commit changes
    - log into Heroku app
    - delete value for DiSABLECOLLECTABLESTATICS
    - navigate to deploy tab and choose desired deployment method - manual or automatic 
    -   i chose to use manual deployment 

11. ### Final deployment to Heroku

![complete before submission](WILL ADD LATER AFTER FEEDBACK BUT BEFORE SUBMISSION)



## REFERENCES

* Harry Dillon - my code institute mentor provided a lot of guidance and advice
* Code institute tutors - he code institute tutors were also very helpful when it came to understanding issues that i was facing throughout the build
* Stackoverflow - used as a resource for guidance on any errors or issues i encountered
* followed the steps provided by the Code institute 'I Think therefore I Blog' walkthrough tutorial to build my web app
* reviewed several youtube tutorials to understand how to execute certain functionalities in Django e.g. 
* reviewed and referenced the information from below resouces for guidance during build
    - https://docs.djangoproject.com/en/
    - https://www.w3schools.com/
    - https://getbootstrap.com/docs/5.3/getting-started/introduction/
    - https://www.geeksforgeeks.org/  