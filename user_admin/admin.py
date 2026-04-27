from django.contrib import admin
from .models import User_signup
# Register your models here.

class UserSignupAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")
    list_filter = ["created_at"]

admin.site.register(User_signup, UserSignupAdmin)