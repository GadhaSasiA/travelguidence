
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Destination, Favorite

@login_required
def add_to_favorites(request, destination_id):
    destination = Destination.objects.get(pk=destination_id)
    
    if not Favorite.objects.filter(user=request.user, destination=destination).exists():
        Favorite.objects.create(user=request.user, destination=destination)

    return redirect('destination_detail', destination_id=destination_id)

