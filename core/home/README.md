# Serializers

- In Django REST Framework (DRF), serializers is used to convert Django models, into JSON and vice versa.

- They are essential for `validating input data`, `transforming it into the format` needed for storage, and `converting data from storage` into a format suitable for rendering.

## When to Use Serializers

- Creating, reading, updating, or deleting resources.

- Validating incoming data before performing operations on the database.

- Formatting outgoing data to be sent to clients.

- `Form Data to JSON`: When you need to convert data from forms or other non-JSON sources into JSON.

- `Custom Validation`: When you need custom validation logic beyond what Django forms provide.

## When You Do Not Need Serializers

- `Admin Interface`: When using Django's built-in admin interface for managing data, serializers are not used. The admin interface relies on Django forms and the model layer directly.

- `Non-API Views`: For traditional Django views (using templates and forms), you typically use Django forms and models directly instead of serializers.

## types of serializers

- In Django REST Framework (DRF), there are mainly two types of serializers:

  - `serializers.Serializer`:

    - This is a base class for defining custom serializers. It provides control over how validation and serialization are handled

    ```
    from rest_framework import serializers

    class CustomSerializer(serializers.Serializer):
       field1 = serializers.CharField()
       field2 = serializers.IntegerField()
    ```

  - `serializers.ModelSerializer`:

    - This is a shortcut for creating serializers that automatically handle the creation and validation logic based on Django models.
    - It dynamically generates fields based on the model definition.
