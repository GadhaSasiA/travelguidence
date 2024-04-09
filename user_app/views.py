from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from.models import Review,User_reg
from.forms import ReviewForm,EditUserProfileForm
# from django.contrib.auth.decorators import login_required
from guide_app.models import guide_reg



def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "revop.html")  
    else:
        form = ReviewForm()

    dict_form = {'form': form}
    return render(request, "review.html", dict_form)

def review_information_view(request, review_id):
    review = get_object_or_404(review, id=review_id)

    context = {
        'review': review,
    }

    return render(request, 'revop.html', context)

def revshow(request):
    dict_r ={
        "review":Review.objects.all()
    }
    return render(request, 'revshow.html',dict_r)

# def reg_details(request):
#     user_id = request.session.get('uid')
#     if user_id is not None:
#         user = get_object_or_404(User_reg, id=user_id)
#         return render(request, 'reg_details.html', {'user': user})
#     else:
#         # Handle the case where user_id is not found in the session
#         # For example, redirect the user to a login page
#         return redirect('login')

def reg_details(request):
    # Step 1: Check session data
    user_id = request.session.get('uid')
    print("User ID from session:", user_id)  # Print user ID for debugging

    if user_id is not None:
        # Step 2: Verify user object retrieval
        user = get_object_or_404(User_reg, id=user_id)
        print("User object retrieved:", user)  # Print user object for debugging

        # Step 3: Confirm template existence and Step 4: Check template rendering
        return render(request, 'reg_details.html', {'user_profile': user})
    else:
        # Handle the case where user_id is not found in the session
        # For example, redirect the user to a login page
        return redirect('login')

def edit_uprofile(request):
    # Retrieve GuideProfile object from session
    user_profile_id = request.session.get('uid')
    
    # Check if the guide_profile_id exists and if it corresponds to a valid GuideProfile instance
    if user_profile_id is not None:
        try:
            user_profile = User_reg.objects.get(pk=user_profile_id)
        except User_reg.DoesNotExist:
            user_profile = None
    else:
        user_profile = None

    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('reg_details')
    else:
        form = EditUserProfileForm(instance=user_profile)
    return render(request, 'edit_uprofile.html', {'form': form})






 

