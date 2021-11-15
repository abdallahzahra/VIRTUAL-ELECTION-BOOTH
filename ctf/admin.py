from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *
# Register your models here.
# admin.site.register(ValidTokens)
# admin.site.register(Vote)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.disable_action('delete_selected')

@admin.register(ValidTokens)
class AuthorAdmin(admin.ModelAdmin):
    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj = None):
        return False
    def has_change_permission(self, request, obj = None):
        return False

@admin.register(Vote)
class AuthorAdmin(admin.ModelAdmin):
    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj = None):
        return False
    def has_change_permission(self, request, obj = None):
        return False
# # comment here
# @admin.register(Vote)
# class ResultAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/vote_summary_change_list.html'


