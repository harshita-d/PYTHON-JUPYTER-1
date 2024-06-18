from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password, make_password


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        if username is None or password is None:
            return None

        try:
            user = User.objects.get(email=username)
            print("password==", user.check_password(password))
            print(f"Stored hashed password: {user.password}")
            print(f"Plain password: {password}")

            if user.check_password(password):
                return user
            else:
                print("Password check failed")
            return user
        except User.DoesNotExist:
            return None
