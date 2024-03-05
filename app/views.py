from django.shortcuts import render,HttpResponse,redirect
from.forms import mail,fb,InstaForm,SearchForm,SignUpForm,LoginForm
from.models import Popular,kerala,india,Guide
from user_app.models import Booking
from user_app.forms import BookingForm
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_app.models import Favorite
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

def index(request):
    return render(request,'index.html')




# def index(request):
#     return render(request,'index.html')

def home(request):
    return render(request,'home.html')


def travel(request):
    return render(request,'index.html')


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
    dict_g={
        'guide':Guide.objects.all()
    }
    return render(request,'guidelist.html',dict_g)


def popular(request):
    dict_p={
        'pop':Popular.objects.all()
    }
    return render(request,'popular.html',dict_p)

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

def booking_details(request):
    return render(request,'booking_details.html')

def booking(request):
    return render(request,'booking.html')

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
           form.save()
        return render(request,"booking_details.html")
    form=BookingForm()
    dict_form={
        'form':form 
    }
    return render(request,"booking.html",dict_form)

def review(request):
    # review=Popular.objects.get(place_id)
    return render(request,'review.html')


# def user_login(request):
#     if request.method=="POST":
#         form=Loginform(request.POST)
#         if form.is_valid():
#             cd=form.cleaned_data
#             user=authenticate(request,username=cd['username'],password=cd['password'])
#             if user is not None:
#                login(request,user)
#                return render(request,'confirm.html',{'form':form})
#             else:
#                 return HttpResponse("Invalid login")
#         else:
#             return render(request,"loginn.html", {'form': form, 'error_message': 'Invalid form data'})
    
#     else:
#         form=Loginform()
#         return render(request,'loginn.html',{'form':form})
    

def trans(request):
    return render(request,'trans.html')


# def register(request):
#     if request.method=="POST":
#         form=RegisterForm(request.POST)

#         if form.is_valid():
#            new_user=form.save(commit=False)
#            new_user.set_password(form.cleaned_data['password'])
#            new_user.save()
#         return HttpResponse("you are successfully Register")

#     else:
#         form =RegisterForm()
#         return render(request, 'register.html', {'form': form})


# @login_required
# def add_to_favorites(request, destination_id):
#     destination = popular.objects.get(pk=destination_id)
    
#     # Check if the user has already added this destination to favorites
#     if not Favorite.objects.filter(user=request.user, destination=destination).exists():
#         Favorite.objects.create(user=request.user, destination=destination)

#     # Redirect back to the original destination detail page
#     return redirect('destination_detail', destination_id=destination_id)


def signup(request):
    msg=None
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.info(request,"user created successfully")
            return redirect('login')
        else:
            messages.info(request,"Form not valid")
    else:
        form=SignUpForm()
    return render (request,'signup.html',{'form':form})


def login_user(request):
    form=LoginForm(request.POST or None)
    msg=None
    if request.method=='POST':
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('admin')
            elif user is not None and user.is_guide:
                login(request,user)
                return redirect('guide')
            elif user is not None and user.is_user:
                login(request,user)
                return redirect('user')
            else:
                msg='invalid credenials'
        else:
            msg='error validating form'
    return render(request,'login.html',{'form':form,'msg':msg})

@login_required
def admin_dashboard(request):
    return render(request,'admin.html')

@login_required
def teacher_dashboard(request):
    return render(request,'teacher.html')

@login_required
def student_dashboard(request):
    return render(request,'student.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')