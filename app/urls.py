from django.urls import path
from.views import*
from.import views

urlpatterns=[
    path('',index,name='index'),
    path('home',home,name='home'),
    path('mail',mail_login,name='mail'),
    path('fb',fb_login,name='fb'),
    path('insta',insta_login,name='insta'),
    path('travel',index,name='travel'),
    path('popular',popular,name='popular'),
    path('search_view/', search_view, name='search_view'),
    path('about',about,name='about'),
    path('keralam',Kerala,name='keralam'),
    path('india',India,name='india'),
    path('guidelist',guide,name='guidelist'),

    path('trans',trans,name='trans'),
    path('confirm',confirm,name='confirm'),
    # path('register',register,name='register'),
    path('booking',booking,name='booking'),
    path('booking_details',booking_details,name='booking_details'),

    # path('loginn/',user_login,name='loginn'),
    # path('review/<int:place_name>/',review,name='review'),
    path('review',review,name='review'),

    # path('favorites/<int:destination_id>/', add_to_favorites, name='favorites'),

    

]