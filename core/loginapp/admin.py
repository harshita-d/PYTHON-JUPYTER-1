from django.contrib import admin

""" from loginapp import models

# Register your models here.
admin.site.register(models.UserLoginProfile) """

from django.apps import apps

models = apps.get_models()

# Register your models here.
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
