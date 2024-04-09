from django.db import models
# from django.contrib.auth.models import User
# from app.models import User

# from app.models import Popular
# from app.models import Popular,kerala,india,Guide
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User




class User_reg(models.Model):
    profile_image = models.ImageField(upload_to='profile_imagess', default='default_profile_image.jpg')
    username = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.pk: 
            self.password1 = make_password(self.password1)
            self.password2 = make_password(self.password2)
        super().save(*args, **kwargs)


    
class Review(models.Model):
    Your_name=models.CharField(max_length=200)
    place_name=models.CharField(max_length=200)
    about_place=models.TextField(max_length=400)
    rating = models.IntegerField(default=0)  
    
    def _str_(self):
        return self.place_name
    



class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_favorite = models.BooleanField(default=False) 
    def __str__(self):
        return self.title
    
