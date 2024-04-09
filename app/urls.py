from django.urls import path
from.views import*
from.import views
from django.contrib.auth import views as auth_views



urlpatterns=[
    path('',index,name='index'),
    # path('base/',base,name='base'),

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
    path('privacy',privacy,name='privacy'),

   path('login',login_user,name='login'),
   path('logout',logout_view,name='logout'),

    # path('login/', auth_views.LoginView.as_view(), name='login'),


  path('register', guide_signup ,name='register'),
  path('register_user', user_signup ,name='register_user'),

  path('place/<int:pk>/review/', views.place_review, name='place_review'),
  path('kerala/<int:pk>/about/', views.kerala_about, name='kerala_about'),
  path('india/<int:pk>/about/', views.india_about, name='india_about'),
  path('add_to_favorites/<int:item_id>/', views.add_to_favorites, name='add_to_favorites'),



  path('add_fav/<int:pk>/', views.add_to_favorites, name='add_fav'),
  path('remove_fav/<int:pk>/', views.remove_from_favorites, name='remove_fav'),
  path('favitems', views.favorite_items, name='favitems'),
  # path('fav',fav, name='fav'),
    # path('user_busbooking/', user_busbooking_view, name='user_busbooking'),




 

  path('add_guide',add_guide,name='add_guide'),


    # path('register', guide_profile_form, name='register'),
    # path('register_user',user_form, name='register_user'),
#   path('custom_user_form/', views.custom_user_form, name='custom_user_form'),
#     path('guide_profile_form/', views.guide_profile_form, name='guide_profile_form'),
#     path('user_form/', views.user_form, name='user_form'),
    


    # path('signup/', signup_view, name='signup_view'),
    # path('profile/', user_profile, name='user_profile'),
    # path('logout/', user_logout, name='user_logout'),
    
    path('create_profile',guide_signup, name='create_profile'),



    path('faq', views.faq_list, name='faq'),

    path('mark_as_favorite/<int:page_id>/', mark_as_favorite, name='mark_as_favorite'),
    # path('page_detail',page_detail,name='page_detail'),


    path('contact_us',contact_us,name='contact_us'),
    path('message', message, name='message'),
    path('local_transp',local_transp,name='local_transp'),
    path('bus',bus,name='bus'),
    path('bus_booking',busbooking,name='bus_booking'),  
    path('bus_books', booking_success, name='bus_books'),

    


    path('flight',flight,name='flight'),
    path('train',create_train,name='train'),
    path('train_booking',train_booking,name='train_booking'),
    path('train_details', train_booking_view, name='train_details'),
    path('bus_details', bus_booking_view, name='bus_details'),

    path('favitems/', views.favorite_items, name='favitems'),
    path('add_fav/<int:destination_id>/', views.add_to_favorites, name='add_fav'),
    path('remove_fav/<int:destination_id>/', views.remove_from_favorites, name='remove_fav'),



    path('review',review,name='review'),
    path('revop',revop,name='revop'),
    path('faq',faq,name='faq'),
    # path('complaint/', complaint_view, name='complaint_view'),





    # path('loginn/',login_view,name='loginn'),
    # path('review/<int:place_name>/',review,name='review'),

    # path('favorites/<int:destination_id>/', add_to_favorites, name='favorites'),
    # path('reg_details',reg_details, name='reg_details'),
  #  path('registration_details/', user_registration_details, name='registration_details'),

    

]