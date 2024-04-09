from django.contrib import admin
from .models import Complaints,guide_reg,Reply,Direct_message,Booking
# Register your models here.
# admin.site.register(Bookinginfo)
admin.site.register(Complaints)
admin.site.register(guide_reg)
admin.site.register(Booking)
# admin.site.register(GuideProfile)
admin.site.register(Direct_message)
admin.site.register(Reply)