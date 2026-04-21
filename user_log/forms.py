from django import forms
from .models import UserPost

class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        exclude = ["create_at"] # or
        fields = "__all__" # or ['title', 'content', 'img'] 
        widgets = {
            "title": forms.TextInput(attrs={"class": " title" , "placeholder": "Enter title here"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "img": forms.ClearableFileInput(attrs={"class": "form-control"}),}