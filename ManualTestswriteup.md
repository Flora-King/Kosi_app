
MANUAL TESTING WRITE UP FOR KOSI web app


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

ADD SCREENSHOT HERE

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


ADD SCREENSHOT HERE

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

ADD SCREENSHOT HERE


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


**TEST CASE NAME : 

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

























***
***
* Tests outstanding 

2. Test that a notification is sent to the user who created the review **`not achieved/not built`**


REFERENCES