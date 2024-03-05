from django import forms
from .models import mail,fb,InstaUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import User



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
        


class InstaForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = InstaUser
        fields = '__all__'
        labels = {
            'in_userid': "Username",
        }
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

# class Loginform(forms.Form):
#     username=forms.CharField()
#     password=forms.CharField(widget=forms.PasswordInput)


    
# from django import forms
# from django.contrib.auth.models import User

# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    email=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )


    class Meta:
        model=User
        fields=('username','email','password1','password2','is_admin','is_guide','is_user')