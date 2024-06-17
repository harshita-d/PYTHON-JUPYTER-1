Certainly! Below is the GitHub Markdown file with the instructions for creating a virtual environment, project, and app in Django, along with explanations of `__init__.py`, WSGI, and ASGI concepts:

````markdown
# Setting Up Django Project with Virtual Environment

## Creating Virtual Environment

Before starting a new Django project, it's recommended to set up a virtual environment to isolate project dependencies.

### Installation

```bash
pip install virtualenv
```
````

### Creating Virtual Environment

```bash
virtualenv venv
```

- **Note**: Run these commands in the command prompt and not in PowerShell.
- **Explanation**: `virtualenv` is a tool used to create isolated Python environments. Here, we create a new virtual environment named `venv`.

### Activating Virtual Environment

```bash
cd venv
cd Scripts
activate
```

- **Note**: Run `activate` inside the `Scripts` directory.
- **Explanation**: Activating the virtual environment ensures that the Python interpreter and installed packages are isolated from the system environment.

### Navigating Back

```bash
cd ..
cd ..
```

- **Explanation**: Navigate back to the project directory.

## Creating Django Project

Now, let's create a new Django project named `core`.

```bash
python -m django startproject core
```

- **Explanation**: This command initializes a new Django project named `core`.

## Creating Django App

After creating the project, let's create a Django app named `home`.

```bash
python manage.py startapp home
```

- **Explanation**: This command creates a Django app named `home` within the `core` project.

## Run Server

```
python manage.py runserver
```

to run the django app on custom server

```
python manage.py runserver 0.0.0.0:5000
```

---

## Understanding `__init__.py`, WSGI, and ASGI

### `__init__.py`:

In Python, `__init__.py` files are used to indicate that a directory should be considered a Python package. These files can be empty or contain initialization code. When a package is imported, Python executes the code within its `__init__.py` file.

### WSGI (Web Server Gateway Interface):

WSGI is a standard interface between web servers and Python web applications or frameworks. WSGI servers communicate with web applications using the WSGI protocol, allowing them to handle HTTP requests and responses.

### ASGI (Asynchronous Server Gateway Interface):

ASGI is an asynchronous variation of WSGI designed for handling long-lived connections and asynchronous operations. ASGI servers support asynchronous web applications, WebSockets, HTTP/2, and server-sent events.

In Django, `wsgi.py` and `asgi.py` files provide entry points for WSGI and ASGI servers to communicate with Django applications respectively. These files define application objects that the servers use to handle incoming requests and responses, allowing Django projects to be deployed in various server environments.

### App Directory in Django

- In Django, think of an "app" as a separate toolbox for handling specific tasks in your website or web application. For example, you might have one app for managing user accounts, another for blog posts, and yet another for handling photos.

1. **Migrations**:

   - This folder keeps track of any changes you make to your app's database structure. It's like a logbook that records what's been added, changed, or removed over time.

2. \***\*init**.py\*\*:

   - This empty file tells Python that the directory is a special place containing Python code. It's a bit like putting up a sign that says, "Hey Python, pay attention, there's stuff here!"

3. **admin.py**:

   - Here, you can customize how your app appears and behaves in Django's admin interface. For example, you might want to tweak how user accounts or blog posts are displayed and managed by site administrators.

4. **apps.py**:

   - This file holds some basic information about your app, like its name and configuration settings. It's like an ID card for your app that Django can use to identify and work with it.

5. **models.py**:

   - This is where you define the data structure of your app. Let's say you're building a blog app; here, you'd define what a blog post looks like, including things like the title, content, and publication date.

6. **tests.py**:

   - Django encourages testing your code to make sure it works as expected. In this file, you can write test cases to check that your app behaves correctly in different scenarios.

7. **views.py**:
   - This file is where you put the logic for handling web requests. For example, when someone visits a page on your site, Django looks here to find out what to do next—like showing a list of blog posts or letting a user log in.

### Note: we need to add apps name in installedapps inside settings.py in project folder

moreover we can write like

```
EXTERNAL_APPS=['home','accounts'...]
INSTALLED_APPS+=EXTERNAL_APPS
```

## which logic to put in which file

- Model (models.py):

  - Ensure data integrity at the database level.
  - Define the Product model with fields like name, price, quantity, etc.
  - Implement methods like get_discounted_price() or calculate_total_cost() within the model.
  - When you want to enforce rules on the data regardless of where it's being manipulated

  - How to implement:

    - Field-level validations: Use field options like max_length, blank, null, unique, etc.
    - Model-level validations: Override the clean method or use clean\_<fieldname> methods.
    - Unique Constraints: Use unique or unique_together

- View (views.py):

  - Implement business logic validations that are specific to certain views.
  - Receive search queries from users.
  - Use the Product model's query methods to search for products matching the query.
  - Return search results to users.

- Serializer (serializers.py) (If using Django REST Framework):

  - Validate data when interacting through the API.
  - When you want to enforce rules on data input through API endpoints, ensuring that invalid data is not processed further.
  - Validate search query parameters if the view is an API endpoint.
  - Serialize product data for API responses if necessary.
## APIs deployed at
- https://hrsd123.pythonanywhere.com/movie/list/
- https://hrsd123.pythonanywhere.com/forbes/people/
- https://hrsd123.pythonanywhere.com/admin/
- https://hrsd123.pythonanywhere.com/login/
- https://hrsd123.pythonanywhere.com/signin/
