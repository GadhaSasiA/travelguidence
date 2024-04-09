from django import forms
from.models import Review,User_reg
from app.models import Post
 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'Your_name','place_name', 'about_place', 'rating']

        widgets = {
            'about_place': forms.Textarea(attrs={'rows': 3}),  
        }
  
class blogForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ['title', 'content']


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = User_reg
        fields = ['username', 'gender', 'place', 'email', 'profile_image']