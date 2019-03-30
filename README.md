# Sphinx-Portal

## Notes - For development

#### Installations
1. Collect Static files during the first run as theier copy in project root is bieng ignored - Rohit.

#### Templates
1. Each App has its own template folder.
2. Base templates are saved in sphinx_portal/base_templates
3. If you are extending the page **base.html** then there is **no need** to create space for showing any **warnings and errors**. Just include errors as `context['errors']` and the messages as `context['messages']` .
4. If page does not extends the **base.html** simply **include `messages.html`** to show errors and messages. - Rohit

#### Apps


#### Views

