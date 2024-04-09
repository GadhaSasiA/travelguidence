from django.db import models
from app.models import Popular,india,kerala,Guide
# from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from user_app.models import User_reg







class guide_reg(models.Model):
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
    

class Booking(models.Model):
    username = models.ForeignKey(User_reg, on_delete=models.CASCADE)
    users_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    phone_number=models.CharField(max_length=10)
    date=models.DateTimeField()
    select_Popular_destinations=models.ForeignKey(Popular, on_delete=models.CASCADE,null=True, blank=True)
    Select_india_destinations=models.ForeignKey(india, on_delete=models.CASCADE,null=True, blank=True)
    Select_kerala_destinations=models.ForeignKey(kerala, on_delete=models.CASCADE,null=True, blank=True)
    guide_name=models.ForeignKey(Guide,on_delete=models.CASCADE,null=True, blank=True)
    guidename=models.ForeignKey(guide_reg,on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return self.users_name
    
class Complaints(models.Model):
    your_name=models.CharField(max_length=100)
    your_Email=models.EmailField()
    complaint=models.TextField(max_length=400)
    def __str__(self):
        return self.your_name

class Direct_message(models.Model):
    sender = models.ForeignKey(User_reg, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(guide_reg,on_delete=models.CASCADE, related_name='received_messages',null=True, blank=True)
    guidename2= models.ForeignKey(Guide,on_delete=models.CASCADE, related_name='received_messages',null=True, blank=True)
    message_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.recipient} at {self.timestamp}"
    

class Reply(models.Model):
    sender = models.ForeignKey(guide_reg, on_delete=models.CASCADE, related_name='sent_messages',)
    recipient = models.ForeignKey(User_reg,on_delete=models.CASCADE, related_name='received_messages',)
    message_reply = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.recipient} at {self.timestamp}"