# KOSI

**Links to other content**

- [Live website](https://kosi-app-9673f8ad46df.herokuapp.com/)
- [GitHub Repository](https://github.com/Flora-King/Kosi_app)
- [The README.md file](https://github.com/Flora-King/Kosi_app)
- [Project Board](https://github.com/Flora-King/Kosi_app/projects?query=is%3Aopen)
- [Manual Testing](https://github.com/Flora-King/Kosi_app)
- [Tasks](https://github.com/Flora-King/Kosi_app)
- [Wireframes](https://github.com/Flora-King/Kosi_app)

## MANUAL TESTING WRITE UP 

**NOTE:**

- **Site User** refers to end user who is not a super user
- **Site Admin user** refers to end user who is a super user

Below are the list of all manual tests undertaken

1. ### TEST CASE NAME: USER LOGIN PROCESS

**TEST SCENARIO 1:** ability to log in or sign in to the personal account following successful registration

**Preconditions**
- Django project is already set up
- Admin site already set up
- Site admin user already created 
- Course and review models and views already set up in Django project
- User already successfully registered

**Test steps**
1. Launch app/front end site
2. Navigate to the Login page
3. Complete all login fields suitably
4. Submit

**Expected outcome**
- Successfully signed in/logged in
- User logged in

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![login page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/49eccb53-e921-47d6-b4bc-2636c21aa3ab)
![successfully logged in](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/f5a55e2e-870f-4161-9535-41fa731daade)

**TEST SCENARIO 2:** ability to log out of the personal account

**Preconditions**
- Django project is already set up
- Admin site already set up
- Site admin user already created 
- course and review models and views already set up in Django project
- User already successfully registered and logged in successfully

**Test steps**
1. Navigate to the Logout page
2. Click on log out button

**Expected outcome**
- Successfully logged out

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![Warning before log out](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/9aeeb56c-234c-4348-b334-2152fe2d8c1b)
![successfully logged out](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/cf7a1a1c-4dbb-4a5d-84e0-56810872fd6d)

***

2. ### TEST CASE NAME: ACCOUNT REGISTRATION PROCESS

**TEST SCENARIO 1:** the ability to signup to the site and create a personal account

**Preconditions**
- Django project is already set up
- Admin site already set up
- Site admin user already created 
- Course and review models and views already set up in Django project

**Test steps**
1. Launch app/front end site
2. Navigate to the Register page
3. Complete all registration fields suitably
4. Signup

**Expected outcome**
- Successfully registered
- User logged in
- User profile is successfully created

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![Registration page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/e5a2ec95-b55f-4d50-ace8-244dd638fe31)

![succesfully registered and logged in ](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/2dbcd726-78cb-4f22-932b-52a0e6432341)

***

3. ### TEST CASE NAME: MANAGE COURSE CONTENT

**TEST CASE 1:** user can create a review whilst logged into site with personal profile

**Preconditions**
- Django project is already set up
- Admin site already set up
- Site admin user already created 
- Course and review models and views already set up in Django project

**Test steps**
1. Launch app/front end site
2. Navigate to the courses page
3. Login as a site user
4. Open course details by clicking on course excerpt
5. Navigate to Reviews sections
6. Add review in text area
7. Submit

**Expected outcome**
- Review is created 
- 'Review awaiting approval' is presented
- Review is presented in faded text with a 'delete' and 'edit' buttons

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![Logged in and ready to edit review](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/5feeb003-fa0a-4bd8-aca3-645e2d5e95b2)

**TEST CASE 2:** user can read a review whilst logged into site with personal profile

**Preconditions**
- Django project is already set up
- Admin site already set up
- Site admin user already created 
- Course and review models and views already set up
- Approved reviews already exist against some courses or all courses

**Test steps**
1. Launch app/front end site
2. Navigate to the courses page
3. Login as a site user
4. Open course details by clicking on course excerpt

**Expected outcome**
- Review is presented in non-faded text without 'delete' and 'edit' buttons

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![Reviews approved seen below course content](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/b5743164-d49a-49ef-8419-ea8f258d0de3)

**TEST CASE 3:** user can update a review whilst logged into site with personal profile

**Preconditions**
- Django project is already set up
- Admin site already set up
- Site admin user already created 
- Course and review models and views set up
- There are reviews awaiting approval

**Test steps**
1. Launch app/front end site
2. Navigate to the courses page
3. Login as a site user
4. Open course details by clicking on course excerpt
5. Reviews awaiting approval are presented in faded text with 'delete' and 'edit' buttons
6. Click on edit button
7. Review text is presented in the review text area 
8. Amend review text
9. Click on update button

**Expected outcome**
- 'Review awaiting approval' message is presented to user
- Review with updated text [awaiting approval] is presented in faded text with 'delete' and 'edit' buttons

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![Review successfully edited](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/05031dc1-6707-4b87-9ad9-5eae70fad6b0)

**TEST CASE 4:** user can delete a review whilst logged into site with personal profile

**Preconditions**
- Django project is already set up
- Admin site already set up
- Site admin user already created 
- Course and review models and views set up
- There are reviews awaiting approval

**Test steps**
1. Launch app/front end site
2. Navigate to the courses page
3. Login as a site user
4. Open course details by clicking on course excerpt
5. Reviews awaiting approval are presented in faded text with 'delete' and 'edit' buttons
6. Click on delete button
7. Confirm you want to delete review

**Expected outcome**
- 'Review deleted' message is presented to user
- Review is successfully deleted

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![Logged in and ready to delete a review](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/26be799d-ee94-4498-877a-dced12a83125)

![Review successfully deleted](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/ab4fb4fc-8aaf-490b-8ca5-227e87880cec)

***

4. ### TEST CASE NAME: CREATE DRAFT COURSE CONTENT

**TEST CASE 1**: ability to create draft content, and save to publish later

**Preconditions**
- Django project set up
- Admin site created
- Site admin user created and authenticated
- Course model set up in admin site

**Test steps**
1. Login as site admin
2. Navigate to courses in the app
3. Click on add course button
4. Complete course fields available
5. Set status to 'draft'
6. Save

**Expected outcome**

- Course is created in admin site with status set to draft
- Course is not visible in the front end by all users including Site admin

**Actual outcome**

- Expected outcome achieved 
- Test **PASSED**

![course list in admin site with status](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/c77df1d6-1882-4f40-ab8c-b65c6866b0d2)

![course still in draft state](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/b53425ff-d0e1-4886-b4e7-292a4fdc7cfe)

**TEST CASE 2:** ability to re-edit already published course content

**Preconditions**
- Django project is set up
- Admin site set up
- Site admin user created and authenticated
- Course model set up 

**Test steps**
1. Log into admin site
2. Navigate to courses in the app
3. Click on add course button
4. Complete course fields 
5. Set status to 'published'
6. Save
7. Select course to edit 
8. Amend content as desired
9. Save

**Expected outcome**
- Course is created in admin site with status set to published
- Course is also created in the front-end site and visible by all users including Site admin
- Amended course details are visible/accessible in the front-end site and admin site

**Actual outcome**

- Expected outcome achieved 
- Test **PASSED**

![course in published state but still editable in admin site](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/1bce2888-2980-4e1f-bb93-e7ae6e1f9e35)

***

5. ### TEST CASE NAME: VIEW COURSE DETAILS

**TEST CASE 1:** when a course excerpt is clicked on, full course details are revealed into full view

**Preconditions**
- Django project is set up
- Admin site set up
- Site admin user already created

**Test steps**
1. Launch app/front end site
2. Navigate to the courses page
3. Open course details by clicking on course excerpt
4. Scroll down to under the course content

**Expected outcome**
- Course content is revealed and clearly visible

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![course-excerpt link to course content](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/05715bd1-457b-49e6-86c5-37fd108567fe)

![Course content page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/7aaafa0a-ba64-4bb8-8b90-d6a35aade8aa)

***

6. ### TEST CASE NAME: ADD A REVIEW

**TEST CASE 1:** user can create a review whilst logged into site with personal profile

**Preconditions**
- Django project is already set up
- Admin site already set up
- Site admin user   created 
- Course and review models and views already set up in Django project

**Test steps**
1. Launch app/front end site
2. Navigate to the courses page
3. Login as a site user
4. Click on course excerpt
5. Navigate to 'Leave a review' area
6. Add review in text area
7. Submit

**Expected outcome**
- Review is created 
- 'Review awaiting approval' message/notification is presented to user
- Review is presented in faded text with a 'delete' and 'edit' buttons

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![logged in and ready to add a review](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/c96c12ad-bbc9-459c-8025-981ed6f6d1a5)

**TEST CASE 2:** the review is visible under the course following approval by the site admin

**Preconditions**
- Django project created
- Admin site created
- Site admin user created 
- Course and review models and views set up 

**Test steps**
1. Launch app/front end site
2. Navigate to the courses page
3. Login as a site user
4. Open course details by clicking on course excerpt
5. Navigate to 'Leave a review' area
6. Add review in text area
7. Submit
8. Log into admin site
9. Navigate to reviews
10. Find and approve recently created review

**Expected outcome**
- Review is presented in non-faded text without the 'delete' and 'edit' buttons
- Review cannot be edited/deleted by user in front end site

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![Reviews under course_content](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/7aaafa0a-ba64-4bb8-8b90-d6a35aade8aa)

***

7. ### TEST CASE NAME: APROVE POSTED REVIEWS

**TEST CASE 1:** Test ability to approve posted reviews by the site admin user

**Preconditions**
- Django project is set up
- Admin site set up
- Site admin user created and authenticated
- Reviews awaiting approval exist in admin site

**Test steps**
1. Login as site admin
2. Navigate to reviews in the app
3. Select reviews not yet approved
4. Proceed to 'approve reviews' and click on Go button

**Expected outcome**

- Selected review is successfully approved 

**Actual outcome**

- Expected outcome achieved 
- Test **PASSED**

![reviews with approval status](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/80c85ee3-3fdd-41f5-bd7c-30dbad49d942)

![Review selected for approval](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/c80af507-5fdf-447a-b9d5-dd2a1dd551d2)

![review approved](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/4e447372-0ef3-4342-8191-5c05d9d9d60c)

***

8. ### TEST CASE NAME: VIEW REVIEWS

**TEST CASE 1:** all users can view reviews against any course without logging into site first

**Preconditions**
- Django project set up
- Admin site set up
- Site admin user created 
- Course and review models and views set up

**Test steps**
1. Launch app/front end site
2. Navigate to the courses page
3. Open course details by clicking on course excerpt
4. Scroll down to under the course content

**Expected outcome**
- Reviews are visible under each course

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![Reviews under course_content](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/7aaafa0a-ba64-4bb8-8b90-d6a35aade8aa)

**TEST CASE 2:** all users can only see approval status of reviews they posted if logged into site with personal profile

**Preconditions**
- Django project set up
- Admin site set up
- Site admin user created 
- Course and review models and views already set up in Django project

**Test steps**
1. Launch app/front end site
2. Navigate to the courses page
3. Open course details by clicking on course excerpt
4. Scroll down to under the course content

**Expected outcome**
- Reviews awaiting approval are not visible to users not logged into front end site

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![reviews when logged before approval](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/31077b44-2b0a-4d29-ac29-3f4e23c2be65)

***

9. ### TEST CASE NAME: ADD STAR RATING

**TEST CASE 1:** can only add a star rating if logged into site with personal profile

**Preconditions**
- Django project set up
- Admin site set up
- Site admin user already created 
- Course and review models and views already set up in Django project

**Test steps**
1. Launch app/front end site
2. Navigate to the courses page
3. Login as a site user
4. Open course details by clicking on course excerpt
5. Click on the star symbol under the course content

**Expected outcome**
- A star rating is successfully added
- Star counter can be toggled up and down
- Star rating count is visible

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![star rating counting before adding another one](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/f9a9c8bc-fdc8-44fe-8c33-14bf1e7e15c3)
![increased star count after adding a star](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/76ee5613-f96a-4273-853f-26e644f30912)

***

10. ### TEST CASE NAME: VIEW STAR RATING

**TEST CASE 1:** all users can see star ratings against each course without logging into their profile first

**Preconditions**
- Django project set up
- Admin site set up
- Site admin user created 
- Course and review models and views already set up in Django project
- Star ratings exist against courses

**Test steps**
1. Launch app/front end site
2. Navigate to the courses page
3. Open course details by clicking on course excerpt
4. Scroll down to under the course content

**Expected outcome**
- Star ratings are visible under a course

**Actual outcome**
- Expected outcome achieved 
- Test **PASSED**

![star ratings on course list page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/b8e5a2bb-2877-47aa-a3d9-a6aaa7480668)
![star ratings on course content page](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/assets/106548101/aa96c8c2-8271-43a4-a27c-2caa047b5b42)

***

**Return to the [README.me](https://github.com/Flora-King/Kosi_app) file for the rest of the readme content**


