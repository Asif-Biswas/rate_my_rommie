from django.shortcuts import render
import json
from .models import Roommate, Address, RoommateRating, AddressRating
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'main/home.html')


@login_required(login_url='account:login')
def add_roommate(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        photo = request.FILES.get('photo')
        about = request.POST['about']
        social_media_link = request.POST['social_media_link']
        attributes = request.POST['attributes']
        attributes = json.loads(attributes)

        roommate = Roommate.objects.create(name=name, address=address, email=email, photo=photo, about=about,
                            social_media_link=social_media_link)
        roommate.save()

        for attribute in attributes:
            roommate_rating = RoommateRating.objects.create(
                user=request.user,
                roommate=roommate,
                attribute=attribute['name'],
                rating=attribute['rating'],
            )
            roommate_rating.save()

        messages.success(request, 'Roommate added successfully')
        return render(request, 'main/add_roommate.html')
    return render(request, 'main/add_roommate.html')



@login_required(login_url='account:login')
def add_address(request):
    if request.method == 'POST':
        address = request.POST['address']
        photo = request.FILES.get('photo')
        about = request.POST['about']
        attributes = request.POST['attributes']
        attributes = json.loads(attributes)

        address = Address.objects.create(address=address, photo=photo, about=about)
        address.save()

        for attribute in attributes:
            address_rating = AddressRating.objects.create(
                user=request.user,
                address=address,
                attribute=attribute['name'],
                rating=attribute['rating']
            )
            address_rating.save()

        messages.success(request, 'Address added successfully')
        return render(request, 'main/add_address.html')
    return render(request, 'main/add_address.html')