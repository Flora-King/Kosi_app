# KOSI

**Links to other content**

- [Live website](https://kosi-app-9673f8ad46df.herokuapp.com/)
- [GitHub Repository](https://github.com/Flora-King/Kosi_app)
- [The README.md file](https://github.com/Flora-King/Kosi_app)
- [Project Board](https://github.com/Flora-King/Kosi_app/projects?query=is%3Aopen)
- [Manual Testing](https://github.com/Flora-King/Kosi_app)
- [Tasks](https://github.com/Flora-King/Kosi_app)
- [Wireframes](https://github.com/Flora-King/Kosi_app)


## INTRODUCTION
*`Kosi`* is a website app aimed at those looking to book courses. In this instance,

This website app provides an opportunity to users looking for short IT and computer programming courses.

[README.md file](https://github.com/Flora-King/Kosi_app)

### Below is the list of User Stories with their related tasks.

These user stories have been elaborated with acceptance criteria. 

For detailed view of the user stories please visit the [project board](https://github.com/Flora-King/Kosi_app/projects?query=is%3Aopen)


| REF | USER STORY TITLE            | USER STORY DESCRIPTION                                                                                                       | PRIORITY    | TASKS [summarised]                                                      | STATUS | SCOPE |
|-----|-----------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------|-------------------------------------------------------------------------|--------|-------|
| 18  | User login process          | As a site user I can log into the website so that I can add or update my reviews                                             | MUST HAVE   | create login html and CSS,                                              | DONE   | IN    |
|     |                             |                                                                                                                              |             | define login url and add to urls.py file                                |        |       |
|     |                             |                                                                                                                              |             | create notification messages,                                           |        |       |
|     |                             |                                                                                                                              |             | add messages to views.py                                                |        |       |
|     |                             |                                                                                                                              |             | check settings.py for email settings                                    |        |       |
|     |                             |                                                                                                                              |             | test full code to ensure completion                                     |        |       |
| 10  | Account registration        | As a site user I can register an account so that I can have access to personal profile                                       | MUST HAVE   | create signup html and CSS,                                             | DONE   | IN    |
|     |                             |                                                                                                                              |             | define signup url and add to urls.py file                               |        |       |
|     |                             |                                                                                                                              |             | create notification messages,                                           |        |       |
|     |                             |                                                                                                                              |             | add messages to views.py                                                |        |       |
|     |                             |                                                                                                                              |             | check settings.py for email settings                                    |        |       |
|     |                             |                                                                                                                              |             | test full code to ensure completion                                     |        |       |
| 15  | manage course content       | As a site admin I can create, read, update, and delete course content so that all the course content is up to date           | MUST HAVE   | Ensure Django project is already set up                                 | DONE   | IN    |
|     |                             |                                                                                                                              |             | link database                                                           |        |       |
|     |                             |                                                                                                                              |             | create admin site                                                       |        |       |
|     |                             |                                                                                                                              |             | create admin user as superuser                                          |        |       |
|     |                             |                                                                                                                              |             | set up course and review models in models.py                            |        |       |
|     |                             |                                                                                                                              |             | define related views in views.py                                        |        |       |
|     |                             |                                                                                                                              |             | add course_detail html and style with CSS                               |        |       |
|     |                             |                                                                                                                              |             | test all for completion                                                 |        |       |
|     |                             |                                                                                                                              |             | Define JavaScript code to enhance the update and delete functionalities |        |       |
| 16  | create draft course content | As a site admin I can create draft courses so that I can complete writing content later                                      | SHOULD HAVE | complete user story 15                                                  | DONE   | IN    |
|     |                             |                                                                                                                              |             | Add draft course content to admin site                                  |        |       |
|     |                             |                                                                                                                              |             | test all for completion                                                 |        |       |
| 6   | View course details         | As a site user I can view course details so that I can view full course details                                              | SHOULD HAVE | complete user story 15 and 16                                           | DONE   | IN    |
|     |                             |                                                                                                                              |             | Add course content to admin site and set to Published                   |        |       |
|     |                             |                                                                                                                              |             | Create course_detail html and CSS                                       |        |       |
|     |                             |                                                                                                                              |             | test to ensure you can see course                                       |        |       |
| 4   | course list pagination      | As a site user I can navigate easily through the course list so that I can see all courses on different pages of the website | SHOULD HAVE | complete user story 15, 6                                               | DONE   | IN    |
|     |                             |                                                                                                                              |             | add pagination code to course_detail html and style                     |        |       |
|     |                             |                                                                                                                              |             | test all for completion                                                 |        |       |
| 11  | add a star rating           | As a site user I can add rating stars against any course so that I share my star rating for a course                         | MUST HAVE   | complete user story 15, 6                                               | DONE   | IN    |
|     |                             |                                                                                                                              |             | add rating code to course_detail html and style                         |        |       |
|     |                             |                                                                                                                              |             | test all for completion                                                 |        |       |
| 12  | add a review                | As a site user I can add a review against any course so that I can share my experience                                       | MUST HAVE   | complete user story 15, 6                                               | DONE   | IN    |
|     |                             |                                                                                                                              |             | Add extra code for adding a review to course_detail html and style      |        |       |
|     |                             |                                                                                                                              |             | test all for completion                                                 |        |       |
| 17  | approve posted reviews      | As a site admin I can approve or disapprove posted reviews so that I can remove subjective or rude commentary                | MUST HAVE   | complete user stories 12, 15, 16, 17, 18                                | DONE   | IN    |
|     |                             |                                                                                                                              |             | add test reviews to any course                                          |        |       |
|     |                             |                                                                                                                              |             | approve reviews in admin site                                           |        |       |
|     |                             |                                                                                                                              |             | test if able to see reviews                                             |        |       |
| 14  | view reviews                | As all users we can view course reviews details against each course so that we can read reviews left by other users          | MUST HAVE   | complete user stories 12, 15, 16, 17, 18                                | DONE   | IN    |
|     |                             |                                                                                                                              |             | add test reviews to any course                                          |        |       |
|     |                             |                                                                                                                              |             | test if able to see reviews                                             |        |       |
| 13  | view star ratings           | As all users we can view star ratings against each course so that we can view courses by star rating                         | MUST HAVE   | complete user stories 12, 15, 16, 17, 18                                | DONE   | IN    |
|     |                             |                                                                                                                              |             | add star ratings to any course                                          |        |       |
|     |                             |                                                                                                                              |             | test if able to see stars added                                         |        |       |


***
**Return to the [README.me](https://github.com/Flora-King/Kosi_app) file for the rest of the readme content**