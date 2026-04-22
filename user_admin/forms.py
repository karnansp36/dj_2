from django import forms
from .models import User_signup

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User_signup
        fields ="__all__"
        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control",}),
        }
        