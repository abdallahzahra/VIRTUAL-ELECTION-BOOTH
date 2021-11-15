from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *
# Register your models here.
admin.site.register(ClaUser)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header = 'Add Cla_User'
# admin.site.register(ClaTokens)
