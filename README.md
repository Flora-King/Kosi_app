# KOSI

**Helpful links**

- Live website for Kosi
- [project board](https://github.com/Flora-King/Kosi_app/projects?query=is%3Aopen)
- [Manual testing write up](../Kosi_app/ManualTestswriteup.md)
- [Wireframes]()

## INTRODUCTION
*`Kosi`* is a website app aimed at those looking to book courses. In this instance,

This website app provides an opportunity to users looking for short IT and computer programming courses.

**TARGETED USERS:**
* people looking for IT courses
* people of any age
* people looking for online and/or in person courses

**SCOPE**

`The original scope` for the Kosi web app was to build and deliver a course booking webapp where users can

* View course content [whether logged in or not]
* Add a review 
* Add a rating
* search through the course list [by either title or description]
* add desired courses to a basket for purchasing immediately or save and return later
* view purchases courses in personal profile when logged in

However, due to time and resources, the `current scope` has been reduced to 

* View course content [whether logged in or not]
* Add a review 
* Add a rating

*A reduced scope does not mean a less useful and/or impactful web app but rather one whose delivery is manageable within the given time. 
And it is my hope that this built webapp will form a foundation to fullfill the original scope in the very near future.*


The live website can be found here [kosi_app](bbbbbbbbbbbbbbbbbbbbbbbb)

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

1. Navigation
    - the navigation for the Kosi web app is very simple and easy. it is made simplae to ensure complete ease of use by anyone using any type of device.
    - the navigation bar has the following
        - Kosi Logo - when clicked, routes the user to the courses list page 
        - Courses - when clicked, routes the user to the courses list page
        - Login - when clicked routes the user to the login page
        - Register - when clicked routes the user to the Sign up page


2. Registration
    - to register, the user can click on the Register button in the navigation bar or use the Sign Up button located on the login page

3. Logging in
    - to login, the user can click on the Login button in the navigation bar; or use the login button located on the Sign Up page or one on the course content page

4. Creating a review/add a rating
    - to create a review/add a rating, the user needs to log in first and navigate to the bottom of their chosen course content page

5. Viewing content
    - the courses page displays the course list where each course has an image, excerpt, price, delivery and delivery_date
    - further course content is accessible via the course content page when the user clicks on any course's excerpt
    - the user is able to view course content without logging in first
    - the user is also able to view approved reviews  and star ratings added against a course whether logged in or not.

6. Updating content
   - the user can only update their own reviews or star ratings
   - to update reviews, the user needs to log in first and navigate to the bottom of their chosen course content page
   - to update a review, the review must still be pending approval
   - star ratings can be removed by the user without approval. However, the user must be logged into the web app.

7. Deleting content
   - the user can only delete their own reviews or remove star ratings they added
   - to delete reviews, the user needs to log in first and navigate to the bottom of their chosen course content page
   - to delete a review, the review must still be pending approval
   - star ratings can be removed by the user without approval. However, the user must be logged into the web app.

8. Viewing notifications/messages
    - I have added messages/notifications to be presented for a short time to the user following the activities below
        - Successful log in -
        - Successful registeration - 
        - adding a review
        - Successful updating a review - Review Updated!
        - Unssucessful updatinf of a review - Error updating review!
        - deleting a review


### Below is the list of User Stories for this project

These user stories have also been elaborated with acceptance criteria.  Visit the [project board](https://github.com/Flora-King/Kosi_app/projects?query=is%3Aopen)

- For stories and linked `**tasks**` see the [Stories and Tasks file](/workspace/Kosi_app/StoriesandTasks.md)

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



### **`Templates`** created for this web app include:
    - User Registration - created to enable the user to create an account in order to access various areas of this web app
    - User Login - created to enable
    - Course_Detail
    - Base html
    - Course detail


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
* **Lighhouse** - to access that the perfomance, accessiblity and best practices applied in this web app are of higher quality.

## TESTING
* **Responsive testing**

![Responsive Testing](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/0b9a8253-e2ea-43cc-80c6-d059f3cdcf58)

**Lighthouse Testing Results**
![Lighthouse Testing](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/35568f2c-d9a1-4f28-89ff-afea8f299a13)


**Code Validation**

* **W3C HTML Validator**
![image](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/6fc952d0-c360-4099-b757-32ee54861916)

The HTML validator also showed a warning regarding a *<hr>* tag that i used to create a separators between the course content and the reviews container. 
This doesnt affect my code and therefore i have left it in.

![<hr> tag information](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/790e4c97-e549-4417-bf02-675b573c3162)

* **W3C CSS Validator**
![CSS Validation results](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/876fda07-960e-4353-ad05-cb41d5785ad2)

* **JS Hint**
![Javascript code validation results](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/e7384ebb-4aa1-4688-b112-a16b62a26546)
    - two undefine variables
    - one unused variable

* **CI Python Linter**

![CI Python Linter results](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/c6ef26c5-daf0-4113-a5f1-f4c07f21a37b)
    - the python code has no errors except for the two long lines that can not be helped and i am aware of. I have tried breaking them up but that just broke my code


* **Chrome Devtools**
![Javascript code error in Devtools console](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/915f0b06-bb28-4641-8983-dc755b2667ed)

### **Features Testing**
 All features have been tested as part of the **User stories testing**. For a detailed view of the manual tests carried out for all the user stories, see [the ManualTestswriteup.md file](https://github.com/Flora-King/Kosi_app)


## DEPLOYMENT
deployment, forking and cloning



## REFERENCES

* Harry Dillon
* CoSde institute tutors 
* Stackoverflow - to review error messages as well as guidance on executing some code
* followed the steps provided by the Code institute 'I Think therefore I Blog' walkthrough tutorial to build my web app
* reviewed several youtube tutorials to understand how to execute certain functionalities in Django e.g. 