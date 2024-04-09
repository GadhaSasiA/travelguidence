from django.urls import path
from.views import*
from.import views

urlpatterns=[
  path('booking',booking,name='booking'),
  path('booking_details',booking_details,name='booking_details'),
  path('booking/<int:booking_id>/', booking_information_view, name='booking_information'),
  path('bookinginfo',views.bookinginfo,name='bookinginfo'),
  path('complaints', complaints, name='complaints'),
  path('com_details', com_details, name='com_details'),
  path('complaints<int:complaints_id>/',comp_information_view,name='com_info'),
  path('com_info',comp_info,name='com_info'),

  path('dm/', send_message, name='dm'),
  path('dmsend/<int:user_id>/', views.message_sent, name='dmsend'),
  path('dmsend/<int:user_id>/', message_sent, name='dmsend'),
  path('display_msg', views.display_messages, name='display_msg'),

    path('message_reply/', views.reply_message, name='message_reply'),
    path('message_show/<int:guide_id>/', views.message_show, name='message_show'),
    path('display_reply', views.display_reply, name='display_reply'),

    path('guide_profile', guide_profile, name='guide_profile'),
    path('edit_gprofile/', edit_gprofile, name='edit_gprofile'),
    path('user/booking/', user_booking_view, name='user_booking'),





]