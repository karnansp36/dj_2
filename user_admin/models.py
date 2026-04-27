from django.db import models

# Create your models here.

class User_signup(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
class Twitter_Post(models.Model):
    user_id =models.ForeignKey(User_signup, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)