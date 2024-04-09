from django import forms
# from .models import
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from.models import mail,fb,InstaUser,Train,Messages,Vehiclebooking,Popular
from guide_app.models import guide_reg
from user_app.models import User_reg




# class guideSignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=255, required=True)    
#     profile_image = forms.ImageField(required=False)
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2','profile_image']


class guideSignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = guide_reg
        fields = ['username', 'gender', 'place', 'email','profile_image', 'password1', 'password2']

class userSignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User_reg
        fields = ['username', 'gender', 'place', 'email','profile_image','password1', 'password2'] 


# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password1 = forms.CharField(widget=forms.PasswordInput)

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput) 


class mail(forms.ModelForm):
    class Meta:
        model=mail
        fields='__all__'
        widgets={
        }
        labels={
            'to':"enter your mail id",
            'from_id':"enter mail id",
            'subject':"subject",
            'note':"details",
        }

class fb(forms.ModelForm):
    password=forms.CharField(label='password',widget=forms.PasswordInput)

    class Meta:
        model=fb
        fields='__all__'
        widgets={
        }
        labels={
            'fb_userid':"Username",
            }
        

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['username','from_place', 'to_place', 'date_and_time', 'select_class']
        widgets = {
            'date_and_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
  


class InstaForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = InstaUser
        fields = '__all__'
        labels = {
            'in_userid': "Username",
        }

class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'message']


      
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)





# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2', 'user_type']

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password']
    




class BusbookingForm(forms.ModelForm):
    class Meta:
        model = Vehiclebooking
        fields = ['username', 'phonenum', 'Email', 'numof_persons', 'address', 'choose_vehicles', 'pickup_date', 'picup_at', 'drop_date', 'drop_at']
        widgets = {
            'pickup_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'drop_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Popular
        fields = ['is_favorite']
        widgets = {'is_favorite': forms.CheckboxInput()}