from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from.forms import InstaForm,fb,mail,SearchForm,TrainForm,LoginForm,MessagesForm,guideSignupForm,userSignupForm,BusbookingForm
from.models import Popular,kerala,india,FAQ,Train,Messages,Vehicle_details,Guide,Favorite,Vehiclebooking
from guide_app.models import guide_reg
from django.contrib.auth import authenticate,login
from user_app.models import Review,Page,User_reg
from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth.hashers import check_password

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html')



def add_guide(request):
    guide_name = request.GET.get('name')
    return render(request, 'add_guide.html', {'guide_name': guide_name})

 



def faq(request):
    return render(request,'faq.html')

def home(request):
    return render(request,'home.html')


def travel(request):
    return render(request,'index.html')

def local_transp(request):
    return render(request,'local_transp.html')

def bus(request):
    return render(request,'bus.html')

def bus(request):
    dict_b={
        'bus':Vehicle_details.objects.all()
    }
    return render(request,'bus.html',dict_b)


def bus_books(request):
    dict_bk={
        'booking':Vehicle_details.objects.all()
    }
    return render(request,'bus.html',dict_bk)

# def busbooking(request):
#     if request.method == 'POST':
#         form = BusbookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse('successfully booked') 
#             return render(request, 'booking_success.html', {'form': form})
#     else:
#         form = BusbookingForm()

#     return render(request, 'bus_booking.html', {'form': form})






def booking_success(request):
    bookdetails = Vehiclebooking.objects.all() 
    return render(request, 'bus_books.html', {'bookdetails': bookdetails})

def mail_login(request):
    if request.method=="POST":
        form=mail(request.POST)
        if form.is_valid():
           form.save()
        return HttpResponse ("successfully send your mail")
    form=mail()
    dict_form={
        'form':form 
    }
    return render(request,"mail.html",dict_form)

def fb_login(request):
    if request.method=="POST":
        form=fb(request.POST)
        if form.is_valid():
           form.save()
        return HttpResponse ("successfully send your facebook account")
    form=fb()
    dict_form={
        'form':form 
    }
    return render(request,"fb.html",dict_form)

def insta_login(request):
    if request.method=="POST":
        form=InstaForm(request.POST)
        if form.is_valid():
           form.save()
        return HttpResponse ("successfully send your facebook account")
    form=InstaForm()
    dict_form={
          'form':form 
    }
    return render(request,"insta.html",dict_form)

def guide(request):
  guide = Guide.objects.all()  # Query all guides
  guidelist = guide_reg.objects.all()  # Query all guides from the list

  return render(request, 'guidelist.html', {'guide': guide, 'guidelist':guidelist})


def popular(request):
    dict_p={
        'pop':Popular.objects.all()
    }
    return render(request,'popular.html',dict_p)



def add_to_favorites(request, pk):
    destination = get_object_or_404(Popular, pk=pk)
    destination=get_object_or_404(india,pk=pk)
    destination.is_favorite = True
    destination.save()
    return render(request,'add_fav.html')


def remove_from_favorites(request, pk):
    destination = get_object_or_404(Popular, pk=pk)
    destination=get_object_or_404(india,pk=pk)
    destination.is_favorite = False
    destination.save()
    return render(request,'remove_fav.html')

def favorite_items(request):
    favorite_destinations = Popular.objects.filter(is_favorite=True)
    return render(request, 'favitems.html', {'favorite_destinations': favorite_destinations})



def India(request):
    dict_ii={
        'ind':india.objects.all()
    }
    return render(request,'india.html',dict_ii)

def Kerala(request):
    dict_kk={
        'kl':kerala.objects.all()
    }
    return render(request,'keralam.html',dict_kk)



def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})


def contact_us(request):
    return render(request,'contact_us.html')

def contact_us(request):
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('messege sended successfully')  
    else:
        form = MessagesForm()
    return render(request, 'contact_us.html', {'form': form})

def message(request):
    dict_m={
        "mess":Messages.objects.all()
    }
    return render(request, 'message.html',dict_m)

def search_view(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Popular.objects.filter(place_name__icontains=query)

        return render(request, 'search.html', {'form': form, 'results': results})
    else:
        return render(request, 'search.html', {'form': form})
    

def about(request):
    return render(request,'about.html')

def confirm(request):
    return render(request,'confirm.html')

def flight(request):
    return render(request,'flight.html')

def train(request):
    return render(request,'train.html')



# def create_train(request):
#     if request.method == 'POST':
#         form = TrainForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('success')  
#     else:
#         form = TrainForm()
#     return render(request, 'train.html', {'form': form})

def create_train(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Train booked successfully!")  # Or render another template for success
    else:
        # Retrieve usernames for choices
        usernames = User_reg.objects.all().values_list('id', 'username')
        form = TrainForm()
        form.fields['username'].choices = usernames

    context = {
        'form': form
    }
    return render(request, 'train.html', context)


def train_booking_view(request):
    if request.method == 'GET':
        username = request.session.get('uid')
        if username:
            trains = Train.objects.filter(username=username)
            context = {
                'trains': trains
            }
            return render(request, 'train_details.html', context)
        else:
            return HttpResponse("User is not logged in. Please log in.")
    else:
        return HttpResponse("Unsupported request method.")
    


def busbooking(request):
    if request.method == 'POST':
        form = BusbookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("bus booked successfully!")  # Or render another template for success
    else:
        # Retrieve usernames for choices
        usernames = User_reg.objects.all().values_list('id', 'username')
        form = BusbookingForm()
        form.fields['username'].choices = usernames

    context = {
        'form': form
    }
    return render(request, 'bus_booking.html', context)

def bus_booking_view(request):
    if request.method == 'GET':
        username = request.session.get('uid')
        if username:
            bookings = Vehiclebooking.objects.filter(username=username)
            context = {
                'bookings': bookings
            }
            return render(request, 'bus_details.html', context)
        else:
            return HttpResponse("User is not logged in. Please log in.")
    else:
        return HttpResponse("Unsupported request method.")


def train_booking(request):
    dict_t={
        "train":Train.objects.all()
    }
    return render(request, 'train_booking.html',dict_t)


def review(request):
    return render(request,'review.html')

def revop(request):
    return render(request,'revop.html')

def place_review(request, pk):
    place = get_object_or_404(Popular, pk=pk)
    reviews = Review.objects.filter(place_name=place.place_name) 
    return render(request, 'place_review.html', {'place': place, 'reviews': reviews})

def kerala_about(request, pk):
    place = get_object_or_404(kerala, id=pk)
    reviews = Review.objects.filter(place_name=place.placename) 
    return render(request, 'kerala_about.html', {'place': place, 'reviews': reviews})


def india_about(request, pk):
    place = get_object_or_404(india, id=pk)
    reviews = Review.objects.filter(place_name=place.destination_name) 
    return render(request, 'india_about.html', {'place': place, 'reviews': reviews})


# def review(request, review_id):
#     reviews = Review.objects.filter(review_id=review_id)
#     return render(request, 'review.html', {'reviews': reviews})



# def comp_info(request):
#     complaints = Complaints.objects.all()
#     return render(request, 'com_info.html', {'complaints': complaints})



# def comp_info(request):
#     dict_c ={
#         "comp":Complaints.objects.all()
#     }
#     return render(request, 'com_info.html',dict_c)


def trans(request):
    return render(request,'trans.html')

def privacy(request):
    return render(request,'privacy.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')  # Rename password1 to password for clarity
        
        # Check if the user is an admin
        if username == 'admin@gmail.com' and password == 'admin':
            request.session['logintdetail'] = username
            request.session['admin'] = 'admin'
            return redirect("/")
        
        # Check if the user is a regular user
        elif User_reg.objects.filter(username=username).exists():
            user = User_reg.objects.get(username=username)
            if check_password(password, user.password1):
                request.session['uid'] = user.id
                request.session['username'] = user.username
                request.session['user'] = "user"
                request.session['profile_image'] = user.profile_image.url  # Assuming profile_image is an ImageField
                return redirect("/")
        
        # Check if the user is a guide
        elif guide_reg.objects.filter(username=username).exists():
            guide = guide_reg.objects.get(username=username)
            if check_password(password, guide.password1):
                request.session['gid'] = guide.id
                request.session['name'] = guide.username
                request.session['user'] = 'guide'
                request.session['profile_image'] = guide.profile_image.url  # Assuming profile_image is an ImageField
                return redirect("/")
    
    return render(request, 'login.html')


                                                                                

        
                    
    
def user_signup(request):
    if request.method == 'POST':
        form = userSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            messages.error(request, "Invalid form submission")
    else:
        form = userSignupForm()
    return render(request, "register_user.html", {'form': form})


# def user_signup(request):
#     if request.method == 'POST':
#         form = userSignupForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Save the form data without committing to the database
#             user = form.save(commit=False)
#             # If a profile photo is provided, save it to the user object
#             if 'profile_image' in request.FILES:
#                 user.profile_image = request.FILES['profile_imagess']
#             # Commit the changes to the database
#             user.save()
#             messages.success(request, 'User registered successfully.')
#             return redirect("/")
#         else:
#             messages.error(request, "Invalid form submission")
#     else:
#         form = userSignupForm()
#     return render(request, "register_user.html", {'form': form})

    
def guide_signup(request):
    if request.method == 'POST':
        form = guideSignupForm(request.POST)
        if form.is_valid():
            guide = form.save(commit=False)
            password1 = form.cleaned_data.get('password1')
            if password1 == "gktravels":
               guide.save()
            return redirect("/")
        else:
            messages.error(request, "Invalid form submission")
    else:
        form = guideSignupForm()
    return render(request, "register.html", {'form': form})


def logout_view(request):
    logout(request)
    request.session.pop('gid', None)
    request.session.pop('uid', None)
    # Other logout related tasks
    return redirect('index') 

def mark_as_favorite(request, page_id):
    if request.method == 'POST':
        page =Page.objects.get(pk=page_id)
        page.is_favorite = True
        page.save()
        return redirect('page_detail', page_id=page_id)
    else:
        # Handle GET requests if necessary
        return HttpResponse("GET request received. This view only handles POST requests.")


# def reg_details(request):
#     user_reg = User_reg.objects.get(username=request.user.username)
#     return render(request, 'reg_details.html', {'user_reg': user_reg})
    
# def reg_details(request):
#     # Retrieve all User_reg objects
#     user_reg_list = User_reg.objects.all()
#     return render(request, 'reg_details.html', {'user_reg_list': user_reg_list})
# @login_required

# def reg_details(request):
#     total_staff = guide_reg.objects.count()
#     user_profile= User_reg.objects.get(user=request.user.username)
#     profile_image = user_profile.profile_image.url if user_profile.profile_image else None
#     return render(request,'reg_details.html',{'profile_image': profile_image,'total_staff':total_staff})