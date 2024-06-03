# Login App

## Add rest_framework and rest_framework.authtoken to INSTALLED_APPS:

- why to add `apps inside INSTALLED_APPS` in settings.py:-

  - DRF provides a suite of tools and components (serializers, viewsets, routers, etc.) necessary for building APIs. By adding rest_framework to INSTALLED_APPS, you enable Django to use these components.
  - DRF includes custom model fields and validators that extend Django's built-in capabilities. Registering the app ensures these fields and validators are available.
  - If you use DRF's token authentication system, it requires specific database tables to store tokens. Adding rest_framework to INSTALLED_APPS ensures these tables are created when you run manage.py migrate.

```
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    ...
]
```

-

## Configure DRF to Use Token Authentication:

- When you `set` up `DEFAULT_AUTHENTICATION_CLASSES` in `settings.py`, you are specifying the `default methods DRF` will use to `authenticate` requests. This can include `token authentication`, `session authentication`, `basic authentication`, and more.
- Using `rest_framework.authentication.TokenAuthentication` means that users must `provide` a valid `token` with each `request to authenticate`. This is a common method for securing APIs.
- `Token-based authentication` is stateless, meaning the server does `not` need to `store session` data between `requests`. Each request is authenticated independently using the token, which is more scalable and easier to manage.

```
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

- If you do not add the DEFAULT_AUTHENTICATION_CLASSES setting in your Django Rest Framework (DRF) configuration in settings.py, the framework will use its default authentication classes. By default, DRF uses SessionAuthentication and BasicAuthentication.

## Setting User Model:

- AUTH_USER_MODEL is used to specify a custom user model to replace the default user model provided by Django.

```
AUTH_USER_MODEL = 'yourapp.UserProfile'
```

## create function in serializer:

- why do we have to add a create function in serializer

```
 def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
```

- This create method relies on the custom user manager's create_user method to handle password hashing.

- when we define a serializer without adding any custom methods, the default behavior provided by Django Rest Framework's ModelSerializer will be used for the create, update, and validation processes.

- The default ModelSerializer will automatically generate field-level validation based on the model fields.

- It will ensure that all required fields are provided and that the data conforms to the types and constraints defined in the model.

- When using serializers.Serializer, the serializer does not automatically know how to create or update instances of your model. Unlike serializers.ModelSerializer, which automatically handles create and update operations based on the model fields, serializers.Serializer requires you to explicitly define these methods.

- When you attempt to save a new instance using this serializer, you will likely encounter an error because the default create method in serializers.Serializer raises a NotImplementedError.

> While serializers.ModelSerializer is useful for CRUD operations directly related to models, serializers.Serializer provides greater flexibility and control for custom tasks like authentication, where data processing and validation do not involve creating or updating model instances.
