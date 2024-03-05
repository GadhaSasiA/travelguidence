from django.db import models
from django.contrib.auth.models import User
from app.models import Popular
from app.models import Popular,kerala,india,Guide


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)

    def _str_(self):
        return self.user.username
    
# class Review(models.Model):
#     place_photo=models.ImageField(upload_to='placeimage')
#     Your_name=models.CharField(max_length=200)
#     place_name=models.CharField(max_length=200)
#     about_place=models.TextField(max_length=400)
#     opinion=models.TextField(max_length=500)

#     def _str_(self):
#         return self.place_name
    

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Popular, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.destination.place_name}"
    
# Create your models here.

class Booking(models.Model):
    users_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    phone_number=models.CharField(max_length=10)
    date=models.DateTimeField()
    select_Popular_destinations=models.ForeignKey(Popular, on_delete=models.CASCADE,blank=True,)
    Select_india_destinations=models.ForeignKey(india, on_delete=models.CASCADE,blank=True)
    Select_kerala_destinations=models.ForeignKey(kerala, on_delete=models.CASCADE,blank=True)
    guide=models.ForeignKey(Guide,on_delete=models.CASCADE)

    def __str__(self):
        return self.users_name