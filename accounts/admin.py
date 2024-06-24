from django.contrib import admin
from .models import Profile
from blog.models import Comment
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'data_of_birth', 'photo']

admin.site.register(Profile,ProfileAdmin)
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user']