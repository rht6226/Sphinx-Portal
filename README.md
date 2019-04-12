# Sphinx-Portal

## Notes - For development

#### Features
1. Registration System(Login/Signup).
2. Student registration system for quiz.
3. Separate dashboard for admin and student.
4. Test can have any pattern of question : Single-correct MCQs,Multi-correct MCQs,Subjective type.
5. Image field and code field for each question.
6. Questions come one by one without an option to go back.
7. Time Limit for each question.
8. An automated interface to check answers and give marks(MCQs are graded automatically).
9. A student can only have single session on the website.
10. Questions are shuffled up for each user.
11. A mail with credentials is sent to the quizmaster after creation of quiz.

#### Technology Stack
* **FRONTEND** : HTML5 , CSS, BOOTSTRAP 4 ,JAVASCRIPT,JQUERY,AJAX
* **BACKEND** : Django


#### Installations
1. pip install requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver
5. visit 127.0.0.1:8000
**Collect Static files during the first run as their copy in project root is being ignored**

#### Templates
1. Each App has its own template folder.
2. Base templates are saved in sphinx_portal/base_templates
3. If you are extending the page **base.html** then there is **no need** to create space for showing any **warnings and errors**. Just include errors as `context['errors']` and the messages as `context['messages']` .
4. If page does not extends the **base.html** simply **include `messages.html`** to show errors and messages.

#### Apps
1. Accounts - For managing signup and authentication of both the admins and the users
2. quiz - For conducting quizzes
3. admin_panel - For creating quizzes and grading them

## Models
| S. No	| Model 	    | App  	  | Description                     |
|-------|---------------|---------|---------------------------------|
|   1.	| User 		    | Account |  AbstractBaseUser               |
|   2.	| Quiz  	    |   Quiz  |  The Quiz model generalised for all kinds of quizzes.   |
|   3.	| Questions  	|   Quiz  |  Each Question will be connected to its Quiz and Each question is generalised to contain all kinds of questions. Subjective as well as objective.|
|   4.  | Answersheet   | Admin Panel | An answersheet for each contestant for every quiz. The Sheet will be created when user registers for the quiz. It will store the marks obtained, time elapsed etc. |
|   5.  | Answer        | Admin Panel | This model will be used to store answers to the questions as well as time elapsed in each questions |


#### Views

