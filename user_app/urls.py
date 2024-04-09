from django.urls import path
from.views import*
from .import views
urlpatterns=[
    path('review<int:revshow_id>/',review_information_view,name='review_information'),
    path('revshow',revshow,name='revshow'),

    path('reg_details/', reg_details, name='reg_details'),  
    path('edit_uprofile/', edit_uprofile, name='edit_uprofile'),

    # path('user_profile/', views.user_profile, name='user_profile'),



]