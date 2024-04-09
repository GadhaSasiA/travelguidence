from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import
# from django.contrib.auth.models import AbstractUser
from django.db import models
from user_app.models import User_reg


    
    



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
    about=models.TextField(max_length=1000)
    features=models.TextField(max_length=500)
    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.place_name

class kerala(models.Model):
    image_place=models.ImageField(upload_to='densinations1')
    placename=models.CharField(max_length=100)
    about_place=models.TextField(max_length=500)
    place_features=models.TextField(max_length=200)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.placename
    
class india(models.Model):
    img_place=models.ImageField(upload_to='densinations2')
    destination_name=models.CharField(max_length=100)
    place_details=models.TextField(max_length=500)
    features=models.TextField(max_length=200)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.destination_name



class Guide(models.Model):
    guide_photo=models.ImageField(upload_to='guidephotos')
    guide_name=models.CharField(max_length=255)
    guide_email=models.EmailField()
    about_guide=models.TextField()
    added_at=models.DateTimeField(auto_now_add=True)
     
    def __str__(self): 
      return self.guide_name
    

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    def __str__(self): 
      return self.question


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

class TrainClass(models.Model):
    add_class = models.CharField(max_length=100)

    def __str__(self):
        return self.add_class

class Train(models.Model):
    username = models.ForeignKey(User_reg, on_delete=models.CASCADE)
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)
    date_and_time = models.DateTimeField()
    select_class = models.ForeignKey(TrainClass, on_delete=models.CASCADE)

    def __str__(self):
        return f"Train from {self.from_place} to {self.to_place} ({self.select_class})"

class Messages(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField(max_length=300)
    def __str__(self):
       return self.name
    
# class Reply(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField()
#     reply_message=models.TextField(max_length=300)
#     def __str__(self):
#        return self.name

class Vehicles(models.Model):
    vehicle=models.CharField(max_length=200)
    def __str__(self):
        return self.vehicle

    
class Vehicle_details(models.Model):
    bus_img=models.ImageField(upload_to='busphotos')
    bus_name=models.CharField(max_length=300)
    ac_or_non_ac=models.CharField(max_length=50)
    seating_capacity=models.IntegerField()
    bus_rent=models.IntegerField()
    def __str__(self):
       return self.bus_name
    

     
class Vehiclebooking(models.Model):
    username = models.ForeignKey(User_reg, on_delete=models.CASCADE)
    yourname=models.CharField(max_length=100)
    phonenum=models.IntegerField()
    Email=models.EmailField()
    numof_persons=models.IntegerField()
    address=models.TextField()
    choose_vehicles=models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    pickup_date=models.DateTimeField()
    picup_at=models.CharField(max_length=200)
    drop_date=models.DateTimeField()
    drop_at=models.CharField(max_length=200)
    def __str__(self):
      return self.yourname

class Favorite(models.Model):
    username = models.ForeignKey(User_reg, on_delete=models.CASCADE)
    destination1= models.ForeignKey(Popular, on_delete=models.CASCADE,null=True, blank=True) 
    destination2= models.ForeignKey(india, on_delete=models.CASCADE,null=True, blank=True)  
    destination3= models.ForeignKey(kerala, on_delete=models.CASCADE,null=True, blank=True)         
    def __str__(self):
        return self.username