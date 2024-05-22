## User Model

- The user model is crucial for handling authentication, authorization, and user profile information.

- built-in user model through django.contrib.auth.models.User

- Fields:

  - **`username`**: A unique identifier for the user.
  - **`password`**: The user's hashed password.
  - **`email`**: The user's email address.
  - **`first_name`** and last_name: The user's first and last names.
  - **`is_active`**: A boolean flag indicating whether the user is active.
  - **`is_staff`**: A boolean flag indicating whether the user can log into the admin site.
  - **`is_superuser`**: A boolean flag indicating whether the user has all permissions without explicitly assigning them.
  - **`last_login`**: A timestamp of the user's last login.
  - **`date_joined`**: A timestamp of when the user was created.

- Methods:

  - **`set_password(raw_password)`**: Hashes and sets the user's password.
  - **`check_password(raw_password)`**: Checks if the provided password matches the stored hashed password.
  - **`get_full_name()`**: Returns the user's full name.
  - **`get_short_name()`**: Returns the user's short name (first name).
  - **`email_user(subject, message, from_email=None, **kwargs)`\*\*: Sends an email to the user.

> To create a custom user model in Django, you typically need to define two main classes: a `custom user model` and a `custom user manager`.

## Custom User Model

- This class defines the structure of your custom user model, including the fields and any additional methods you need.
- It extends `AbstractBaseUser` and optionally `PermissionsMixin`.

- `USERNAME_FIELD` is an attribute defined in a custom user model that specifies the field used to uniquely identify users.
- By default, Django uses the username field to uniquely identify users. However, when creating a custom user model, you may want to use a different field, such as an email address,

### 1. AbstractBaseUser

- The AbstractBaseUser class in Django provides the core implementation for a custom user model but includes only a few essential fields and methods.

- **Fields** Provided by AbstractBaseUser

  - AbstractBaseUser itself provides only **two fields**:
  - **`password`**: A CharField that stores the hashed password for the user.
  - **`last_login`**: A DateTimeField that records the timestamp of the user's last login.

- **Methods** Provided by AbstractBaseUser

  - **`set_password(raw_password)`**: Hashes and sets the user's password.
  - **`check_password(raw_password)`**: Checks if the provided password matches the stored hashed password.
  - **`get_session_auth_hash()`**: Returns a hash of the password to track session validity.
  - **`get_username()`**: Returns the identifier for the user, which is usually the username.

> If you do not define the **`__str__`** method in your Django models, This default representation is typically not very informative and looks something like this: ModelName object (primary_key). For example, if your model is named CustomUser and its primary key is 1, the string representation would be CustomUser object (1).

### 2. PermissionsMixin

- This mixin class provided by Django to add the functionality of handling `permissions` and `groups` to your custom user model.

- The Django default user model (django.contrib.auth.models.User) comes with built-in support for permissions and groups.

- When creating a custom user model using `AbstractBaseUser`, you need to manually add this support by including PermissionsMixin.

- This mixin adds essential fields like `is_superuser`, `groups`, and `user_permissions`, as well as methods for checking permissions.

- Types of Permissions:

  - **`Default Permissions`**: Django automatically creates three default permissions for each model

    - `add_<modelname>`: Permission to add an instance of the model.
    - `change_<modelname>`: Permission to change an instance of the model.
    - `delete_<modelname>`: Permission to delete an instance of the model.

  - **`Custom Permissions`**

- Managing Permissions:

  - **`Assigning Permissions`**
  - **`Checking Permissions`**

- Fields Added by PermissionsMixin:

  - **`is_superuser`**: A boolean field that indicates whether the user has all permissions without explicitly assigning them.
  - **`groups`**: A many-to-many relationship to the Group model, allowing users to be members of multiple groups.
  - **`user_permissions`**: A many-to-many relationship to the Permission model, allowing users to have specific permissions assigned.

- Methods Added by PermissionsMixin
  - **`get_user_permissions(obj=None)`**: Returns a set of permission strings that the user has.
  - **`get_group_permissions(obj=None)`**: Returns a set of permission strings that the user has through their groups.
  - **`get_all_permissions(obj=None)`**: Returns a set of all permission strings that the

## Custom User Manager

- manager class is a specialized class that handles the creation and management of user instances

- The user manager class is essential for creating user and superuser instances correctly, ensuring that required fields are set and passwords are hashed.

- The user manager class typically inherits from `BaseUserManager`

- Purpose of a User Manager Class

  - **`Creating Users`**: Ensures that user instances are created with necessary fields and that passwords are properly hashed.
  - **`Creating Superusers`**: Ensures that superuser instances are created with appropriate permissions and staff status.
  - **`Custom Behavior`**: Implements any additional logic required during user creation, such as validating fields or normalizing data.

- Key Methods in a User Manager Class

  - **`create_user`**
  - **`create_superuser`**

- To use the custom user manager in your custom user model, you need to assign it to the objects attribute of your custom user model

---

- configuring custom user model in project

  - in setting.py add `AUTH_USER_MODEL='user.UserProfile'`
