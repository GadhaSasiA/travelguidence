from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin=models.BooleanField('Admin',default=False)
    is_guide=models.BooleanField('Guide',default=False)
    is_user=models.BooleanField('User',default=False)


class mail(models.Model):
    to=models.CharField(max_length=100)
    from_id=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    note=models.TextField(max_length=100)
    def __str__(self):
        return self.to
    
class fb(models.Model):
    fb_userid=models.CharField(max_length=100)
    
    def __str__(self):
        return self.fb_userid
     


class InstaUser(models.Model):
    in_userid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Popular(models.Model):
    image=models.ImageField(upload_to='destinations')
    place_name=models.CharField(max_length=100)
    about=models.TextField(max_length=400)
    features=models.TextField(max_length=100)
    def __str__(self):
        return self.place_name

class kerala(models.Model):
    image_place=models.ImageField(upload_to='densinations1')
    placename=models.CharField(max_length=100)
    about_place=models.TextField(max_length=500)
    place_features=models.TextField(max_length=200)
    def __str__(self):
        return self.placename
    
class india(models.Model):
    img_place=models.ImageField(upload_to='densinations2')
    destination_name=models.CharField(max_length=100)
    place_details=models.TextField(max_length=500)
    features=models.TextField(max_length=200)
    def __str__(self):
        return self.destination_name

    

# class TravelGuide(models.Model):
#     guide_image = models.ImageField(upload_to='guidephoto')
#     guide_name = models.CharField(max_length=255)
#     guide_bio=models.CharField(max_length=300)
#     added_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self): 
#         return self.guide_name

class Guide(models.Model):
    guide_photo=models.ImageField(upload_to='guidephotos')
    guide_name=models.CharField(max_length=255)
    about_guide=models.TextField()
    added_at=models.DateTimeField(auto_now_add=True)
     
    def __str__(self): 
      return self.guide_name



    