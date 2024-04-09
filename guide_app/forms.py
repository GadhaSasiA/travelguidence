from django import forms
from.models import Complaints,Direct_message,Reply,guide_reg,Booking
from user_app.models import User_reg
 
class BookingForm(forms.ModelForm):
    username = forms.ModelChoiceField(queryset=User_reg.objects.all(), label="Username")

    class Meta:
        model=Booking
        fields='__all__'
        widgets={
            'booking_date':forms.DateInput(attrs={'type':'date'})
        }
        labels={
            'username':"Username",
            'users_name': "User Name",
            'email_id': "User's Email ID",
            'phone_number': "User's Phone",
            'date': "Booking Date",
            'select_Popular_destinations': "Select Popular Destinations",
            'Select_india_destinations': "Select India Destinations",
            'Select_kerala_destinations': "Select Kerala Destinations",
            'guide_name': "Guide Name",
            'guidename': "Guide Name",

        }     
        
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ['your_name','your_Email' ,'complaint']
        widgets={
             'your_name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
             'Your_Email': forms.EmailInput(attrs={'placeholder': 'Enter your email id'}),
             'complaint': forms.Textarea(attrs={'placeholder': 'Enter your complaint'}),
        }
        labels = {
           
        }


class DmForm(forms.ModelForm):
    class Meta:
        model = Direct_message
        fields = ['sender','recipient', 'message_content'] 

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['sender','recipient', 'message_reply']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = guide_reg
        fields = ['username', 'gender', 'place', 'email', 'profile_image']

