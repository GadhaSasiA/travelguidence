from django.db import models
from app.models import Guide
from user_app.models import User

class Bookinginfo(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_booked = models.DateTimeField()