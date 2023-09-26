MANUAL TESTING WRITE UP FOR KOSI web app

[Live website](https://kosi-app-9673f8ad46df.herokuapp.com/)

[The README.md file](https://github.com/Flora-King/Kosi_app)

***
***

**TEST CASE NAME: USER LOGIN PROCESS**

**`TEST SCENARIO 1: the ability to log in or sign in to the personal account following successful registration`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project
- [ ] user already successfully registered

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the Login page
- [ ] complete all login fields suitably
- [ ] submit

**`Expected outcome`**
- [ ] successfully signed in/logged in
- [ ] user logged in

**`Actual outcome`**
- [ ] successfully signed in/logged in
- [ ] user logged in

![login page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/49eccb53-e921-47d6-b4bc-2636c21aa3ab)
![successfully logged in](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/f5a55e2e-870f-4161-9535-41fa731daade)

**`TEST SCENARIO 2: ability to log out of the personal account`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project
- [ ] user already successfully registered and logged in successfully

`Test steps`
- [ ] navigate to the Logout page
- [ ] click on log out button

**`Expected outcome`**
- [ ] successfully logged out

**`Actual outcome`**
- [ ] successfully logged out


![Warning before log out](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/9aeeb56c-234c-4348-b334-2152fe2d8c1b)
![successfully logged out](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/cf7a1a1c-4dbb-4a5d-84e0-56810872fd6d)

***

**TEST CASE NAME: ACCOUNT REGISTRATION PROCESS**

**`TEST CASE 1: the ability to signup to the site and create a personal account`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the Register page
- [ ] complete all registration fields suitably
- [ ] signup

**`Expected outcome`**
- [ ] successfully registered
- [ ] user logged in
- [ ] user profile is successfully created

**`Actual outcome`**
- [ ] successfully registered
- [ ] user logged in
- [ ] user profile is successfully created

![Registration page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/e5a2ec95-b55f-4d50-ace8-244dd638fe31)

![succesfully registered and logged in ](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/2dbcd726-78cb-4f22-932b-52a0e6432341)


***
**TEST CASE NAME: MANAGE COURSE CONTENT**

**`TEST CASE 1: user can create a review whilst logged into site with personal profile`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the courses page
- [ ] login as a site user
- [ ] open course details by clicking on course excerpt
- [ ] navigate to 'Leave a review' tab
- [ ] add review in textarea
- [ ] click submit

**`Expected outcome`**
- [ ] review is created 
- [ ] 'Review awaiting approval' is presented
- [ ] review is presented in faded text with a 'delete' and 'edit' buttons

**`Actual outcome`**
- [ ] review is created 
- [ ] 'Review awaiting approval' is presented
- [ ] review is presented in faded text with a 'delete' and 'edit' buttons

![Logged in and ready to edit review](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/5feeb003-fa0a-4bd8-aca3-645e2d5e95b2)

**`TEST CASE 2: user can read a review whilst logged into site with personal profile`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project
- [ ] approved reviews already exist against some courses or all courses

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the courses page
- [ ] login as a site user
- [ ] open course details by clicking on course excerpt

**`Expected outcome`**
- [ ] review is presented in non-faded text without 'delete' and 'edit' buttons

**`Actual outcome`**
- [ ] review is presented in non-faded text without 'delete' and 'edit' buttons

![Reviews approved seen below course content](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/b5743164-d49a-49ef-8419-ea8f258d0de3)

**`TEST CASE 3: user can update a review whilst logged into site with personal profile`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project
- [ ] there are reviews awaiting approval

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the courses page
- [ ] login as a site user
- [ ] open course details by clicking on course excerpt
- [ ] reviews awaiting approval are presented in faded text with 'delete' and 'edit' buttons
- [ ] click on edit button
- [ ] review text is presented in the review textarea 
- [ ] amend review text
- [ ] click on update button

**`Expected outcome`**
- [ ] 'Review awaiting approval' message is presented to user
- [ ] review with updated text [awaiting approval] is presented in faded text with 'delete' and 'edit' buttons

**`Actual outcome`**
- [ ] 'Review awaiting approval' message is presented to user
- [ ] review  with updated text [awaiting approval] is presented in faded text with 'delete' and 'edit' buttons

![Review successfully edited](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/05031dc1-6707-4b87-9ad9-5eae70fad6b0)

**`TEST CASE 4: user can delete a review whilst logged into site with personal profile`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project
- [ ] there are reviews awaiting approval

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the courses page
- [ ] login as a site user
- [ ] open course details by clicking on course excerpt
- [ ] reviews awaiting approval are presented in faded text with 'delete' and 'edit' buttons
- [ ] click on edit button
- [ ] review text is presented in the review textarea 
- [ ] amend review text
- [ ] click on delete button

**`Expected outcome`**
- [ ] 'Review deleted' message is presented to user
- [ ] review is successfully deleted

**`Actual outcome`**
- [ ] 'Review deleted' message is presented to user
- [ ] review is successfully deleted

![Logged in and ready to delete a review](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/26be799d-ee94-4498-877a-dced12a83125)


![Review successfully deleted](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/ab4fb4fc-8aaf-490b-8ca5-227e87880cec)

***
**TEST CASE NAME: CREATE DRAFT COURSE CONTENT**

**`TEST CASE 1`**:ability to create draft content, and save to publish later

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created and authenticated
- [ ] course model already set up in admin site

`Test steps`
- [ ] login as site admin
- [ ] navigate to courses in the app
- [ ] click on add course button
- [ ] complete/fill in course fields available
- [ ] set status to 'draft'
- [ ] save

**`Expected outcome`**

- [ ] course is created in admin site with status set to draft
- [ ] course is not visible in the front end by all users including Site admin

**`Actual outcome`**

- [ ] course is created in admin site with status set to draft
- [ ] course is not visible in the front end by all users including Site admin

![course list in admin site with status](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/c77df1d6-1882-4f40-ab8c-b65c6866b0d2)

![course still in draft state](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/b53425ff-d0e1-4886-b4e7-292a4fdc7cfe)

**`TEST CASE 2:`** ability to re-edit already published course content

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created and authenticated
- [ ] course model already set up 

`Test steps`
- [ ] log into admin site
- [ ] navigate to courses in the app
- [ ] click on add course button
- [ ] complete/fill in course fields available
- [ ] set status to 'published'
- [ ] save
- [ ] select course to edit 
- [ ] amend content as needed
- [ ] save

**`Expected outcome`**

- [ ] course is created in admin site with status set to published
- [ ] course is also created in the front end site and visible by all users including Site admin
- [ ] amended course details are visible/accessible in the front end site and admin site

**`Actual outcome`**

- [ ] course is created in admin site with status set to published
- [ ] course is also created in the front end site and visible by all users including Site admin
- [ ] amended course details are visible/accessible in the front end site and admin site

![course in published state but still editable in admin site](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/1bce2888-2980-4e1f-bb93-e7ae6e1f9e35)

***
**TEST CASE NAME: VIEW COURSE DETAILS**

**`TEST CASE 1: when a course title is clicked on, full course details are revealed into full view`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the courses page
- [ ] open course details by clicking on course excerpt
- [ ] scroll down to under the course content

**`Expected outcome`**
- [ ] course content is revealed and clearly visible

**`Actual outcome`**
- [ ] course content is revealed and clearly visible

![course-excerpt link to course content](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/05715bd1-457b-49e6-86c5-37fd108567fe)

![Course_content page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/7aaafa0a-ba64-4bb8-8b90-d6a35aade8aa)

***
**TEST CASE NAME: ADD A REVIEW**

**`TEST CASE 1: user can create a review whilst logged into site with personal profile`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the courses page
- [ ] login as a site user
- [ ] open course details by clicking on course excerpt
- [ ] navigate to 'Leave a review' tab
- [ ] add review in textarea
- [ ] click submit

**`Expected outcome`**
- [ ] review is created 
- [ ] 'Review awaiting approval' message/notification is presented to user
- [ ] review is presented in faded text with a 'delete' and 'edit' buttons

**`Actual outcome`**
- [ ] review is created 
- [ ] 'Review awaiting approval' is presented
- [ ] review is presented in faded text with a 'delete' and 'edit' buttons

![logged in and ready to add a review](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/c96c12ad-bbc9-459c-8025-981ed6f6d1a5)

**`TEST CASE 2: the review is visible under the course following approval by the site admin`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the courses page
- [ ] login as a site user
- [ ] open course details by clicking on course excerpt
- [ ] navigate to 'Leave a review' tab
- [ ] add review in textarea
- [ ] click submit
- [ ] log into admin site as site admin
- [ ] navigate to reviews
- [ ] find and approve recently created review

**`Expected outcome`**
- [ ] review is presented in non-faded text without the 'delete' and 'edit' buttons
- [ ] review can not be edited/delted by user in front end site

**`Actual outcome`**
- [ ] review is presented in non-faded text without the 'delete' and 'edit' buttons
- [ ] review can not be edited/delted by user in front end site

![Reviews under course_content](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/7aaafa0a-ba64-4bb8-8b90-d6a35aade8aa)

***

**TEST CASE NAME: APROVE POSTED REVIEWS**

**`TEST CASE 1**:`Test ability to approve posted reviews by the site admin user

**`Preconditions`**
- [ ] Django project is set up
- [ ] Admin site already set up
- [ ] site admin user already created and authenticated
- [ ] reviews awaiting approval exist in the reviews table in admin site

`Test steps`
- [ ] login as site admin
- [ ] navigate to reviews in the app
- [ ] select review not yet approved
- [ ] select 'approve reviews' and click on Go button

**`Expected outcome`**

- [ ] selected review is successfully approved 

**`Actual outcome`**

- [ ] selected review is successfully approved 

![reviews with approval status](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/80c85ee3-3fdd-41f5-bd7c-30dbad49d942)
![Review selected for approval](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/c80af507-5fdf-447a-b9d5-dd2a1dd551d2)
![review approved](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/4e447372-0ef3-4342-8191-5c05d9d9d60c)


***

**TEST CASE NAME: VIEW REVIEWS**

**`TEST CASE 1: all users have the ability to view reviews against any course without logging into site first`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the courses page
- [ ] open course details by clicking on course excerpt
- [ ] scroll down to under the course content

**`Expected outcome`**
- [ ] reviews are visible under a course

**`Actual outcome`**
- [ ] reviews are visible under a course

![Reviews under course_content](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/7aaafa0a-ba64-4bb8-8b90-d6a35aade8aa)

**`TEST CASE 2: all users can only see approval status of reviews they posted if logged into site with personal profile`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the courses page
- [ ] open course details by clicking on course excerpt
- [ ] scroll down to under the course content

**`Expected outcome`**
- [ ] reviews awaiting approval are not visible to users not logged into front end site

**`Actual outcome`**
- [ ] reviews awaiting approval are not visible to users not logged into front end site

![own reviews when logged before approval](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/31077b44-2b0a-4d29-ac29-3f4e23c2be65)
***

**TEST CASE NAME: ADD STAR RATING**

**`TEST CASE 1: can only add a star rating if logged into site with personal profile`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the courses page
- [ ] login as a site user
- [ ] open course details by clicking on course excerpt
- [ ] click on the star under the course content

**`Expected outcome`**
- [ ] a star is successfully added
- [ ] star counter can be toggled up and down
- [ ] the star count is visible

**`Actual outcome`**
- [ ] a star is successfully added
- [ ] star counter can be toggled up and down
- [ ] the star count is visible

![star rating counting before adding another one](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/f9a9c8bc-fdc8-44fe-8c33-14bf1e7e15c3)
![increated star count after adding a star](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/76ee5613-f96a-4273-853f-26e644f30912)

***

**TEST CASE NAME: VIEW STAR RATING**

**`TEST CASE 1: all users can see star ratings against each course without logging into their profile first`**

**`Preconditions`**
- [ ] Django project is already set up
- [ ] Admin site already set up
- [ ] site admin user already created 
- [ ] course and review models and views already set up in django project
- [ ] stars have already been added to courses

`Test steps`
- [ ] launch app/front end site
- [ ] navigate to the courses page
- [ ] open course details by clicking on course excerpt
- [ ] scroll down to under the course content

**`Expected outcome`**
- [ ] star/s are visible under a course

**`Actual outcome`**
- [ ] star/s are visible under a course

![star ratings on course list page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/b8e5a2bb-2877-47aa-a3d9-a6aaa7480668)
![star ratings on course content page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/aa96c8c2-8271-43a4-a27c-2caa047b5b42)


***
***
**Return to the [README.me](https://github.com/Flora-King/Kosi_app) file for the rest of the readme content**
