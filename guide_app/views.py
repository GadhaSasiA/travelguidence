from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import Complaints,guide_reg,Direct_message,Reply,Booking
from .forms import ComplaintForm,DmForm,ReplyForm,EditProfileForm,BookingForm
from user_app.models import User_reg



def complaints(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "com_details.html")
    else:
        form = ComplaintForm()
    
    return render(request, "complaints.html", {'form': form})


def com_details(request):
    return render(request, 'com_details.html')

def comp_info(request):
    # Assuming you have a Complaint model with fields your_name, your_Email, and complaint
    complaints = Complaints.objects.all()  # Retrieve all complaints from the database

    context = {
        'comp': complaints  
    }

    return render(request, 'com_info.html', context)

def comp_information_view(request, complaints_id):
    complaint_obj = get_object_or_404(Complaints, id=complaints_id)

    context = {
        'complaint': complaint_obj,
    }

    return render(request, 'com_details.html', context)


  # Import your Booking model

def booking_details(request):
    user_bookings = Booking.objects.filter(users_name=request.user)
    
    return render(request, 'booking_details.html', {'user_bookings': user_bookings})

def user_booking_view(request):
    if request.method == 'GET':
        username = request.session.get('uid')
        if username:
            user_bookings = Booking.objects.filter(username=username)
            context = {
                'user_bookings': user_bookings
            }
            return render(request, 'user_booking.html', context)
        else:
            return HttpResponse("User is not logged in. Please log in.")
    else:
        return HttpResponse("Unsupported request method.")



def booking(request):
    return render(request, 'booking.html')

def bookinginfo(request):
    dict_b ={
        "info":Booking.objects.all()
    }
    return render(request, 'bookinginfo.html',dict_b)


# def booking(request):
#     if request.method=="POST":
#         form=BookingForm(request.POST)
#         if form.is_valid():
#            form.save()
#         return render(request,"booking_details.html")
#     else:
#         form=BookingForm()
#     dict_form={
#         'form':form 
#     }
#     return render(request,"booking.html",dict_form)

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"booking_details.html")

    else:
        # Retrieve usernames for choices
        usernames = User_reg.objects.all().values_list('id', 'username')
        form = BookingForm()
        form.fields['username'].choices = usernames

    context = {
        'form': form
    }
    return render(request, 'booking.html', context)






def booking_information_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    context = {
        'booking': booking,
    }

    return render(request, 'booking_details.html', context)

def user_booking_details(request):
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user)
        return render(request, 'booking_details.html', {'user_bookings': user_bookings})
    else:
        return render(request, 'not_logged_in.html')


# def guidelist(request):
#     dict_g={
#         'guidelist':guide_reg.objects.all()
#     }
#     return render(request,'guidelist.html',dict_g)


def send_message(request):
    if request.method == 'POST':
        form = DmForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            user_id = request.session.get('uid')
            user = User_reg.objects.get(id=user_id)
            message.sender = user
            message.save()
            return render(request,'dmsend.html')
    else:
        form = DmForm()
    return render(request, 'dm.html', {'form': form})

def message_sent(request,user_id):
    return render(request, 'dmsend.html')

def reply_message(request):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            guide_id = request.session.get('gid')
            guide = guide_reg.objects.get(id=guide_id)
            message.sender = guide
            # Assign recipient based on your application logic, for example:
            # message.recipient = User_reg.objects.get(id=request.POST['recipient'])
            message.save()
            return render(request, 'message_show.html')
    else:
        form = ReplyForm()
    return render(request, 'message_reply.html', {'form': form})

def display_reply(request):
    if 'uid' in request.session:  # Assuming guide ID is stored in session as 'gid'
        user_id = request.session['uid']
        reply_messages = Reply.objects.filter(recipient__id=user_id)
        return render(request, 'display_reply.html', {'reply_messages': reply_messages})
    else:
        return render(request, 'not_logged_in.html')
    
def message_show(request):
    return render(request, 'message_show.html')

def display_messages(request):
    if 'gid' in request.session:  # Assuming guide ID is stored in session as 'gid'
        guide_id = request.session['gid']
        user_messages = Direct_message.objects.filter(recipient__id=guide_id)
        return render(request,'display_msg.html', {'user_messages': user_messages})
    else:
        return render(request, 'not_logged_in.html')
    

def guide_profile(request):
    # Step 1: Check session data
    guide_id = request.session.get('gid')
    print("User ID from session:", guide_id)  # Print user ID for debugging

    if guide_id is not None:
        # Step 2: Verify user object retrieval
        guide = get_object_or_404(guide_reg, id=guide_id)
        print("User object retrieved:", guide)  # Print user object for debugging

        # Step 3: Confirm template existence and Step 4: Check template rendering
        return render(request, 'guide_profile.html', {'guide_profile': guide})
    else:
        # Handle the case where user_id is not found in the session
        # For example, redirect the user to a login page
        return redirect('login')
    

def edit_gprofile(request):
    # Retrieve GuideProfile object from session
    guide_profile_id = request.session.get('gid')
    
    # Check if the guide_profile_id exists and if it corresponds to a valid GuideProfile instance
    if guide_profile_id is not None:
        try:
            guide_profile = guide_reg.objects.get(pk=guide_profile_id)
        except guide_reg.DoesNotExist:
            guide_profile = None
    else:
        guide_profile = None

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=guide_profile)
        if form.is_valid():
            form.save()
            return redirect('guide_profile')
    else:
        form = EditProfileForm(instance=guide_profile)

    return render(request, 'edit_gprofile.html', {'form': form})