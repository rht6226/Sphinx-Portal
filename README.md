# Sphinx-Portal

## Notes - For development

#### Installations
1. Collect Static files during the first run as their copy in project root is being ignored

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


#### Views

