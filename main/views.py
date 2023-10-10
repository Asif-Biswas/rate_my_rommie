from django.shortcuts import render, redirect
import json
from .models import Roommate, Address, RoommateRating, AddressRating
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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


def roommate(request, roommate_id):
    roommate = Roommate.objects.get(id=roommate_id)
    ratings = RoommateRating.objects.filter(roommate=roommate)
    rating_objects = []
    rated_by = []
    for rating in ratings:
        if rating.user in rated_by:
            continue
        rated_by.append(rating.user)
        all_ratings = RoommateRating.objects.filter(user=rating.user, roommate=roommate)
        average = 0
        if all_ratings:
            total = 0
            for rating in all_ratings:
                total += rating.rating
            average = total / len(all_ratings)
        star = []
        for i in range(1, 6):
            if i <= average:
                star.append('fas fa-star')
            elif i - average < 1:
                star.append('fas fa-star-half-alt')
            else:
                star.append('far fa-star')
        rating_object = {
            'user': rating.user,
            'ratings': all_ratings,
            'average': average,
            'star': star,
        }
        rating_objects.append(rating_object)
    context = {
        'roommate': roommate,
        'ratings': rating_objects,
    }
    return render(request, 'main/roommate.html', context)


def address(request, address_id):
    address = Address.objects.get(id=address_id)
    ratings = AddressRating.objects.filter(address=address)
    rating_objects = []
    rated_by = []
    for rating in ratings:
        if rating.user in rated_by:
            continue
        rated_by.append(rating.user)
        all_ratings = AddressRating.objects.filter(user=rating.user, address=address)
        average = 0
        if all_ratings:
            total = 0
            for rating in all_ratings:
                total += rating.rating
            average = total / len(all_ratings)
        star = []
        for i in range(1, 6):
            if i <= average:
                star.append('fas fa-star')
            elif i - average < 1:
                star.append('fas fa-star-half-alt')
            else:
                star.append('far fa-star')
        rating_object = {
            'user': rating.user,
            'ratings': all_ratings,
            'average': average,
            'star': star,
        }
        rating_objects.append(rating_object)
    context = {
        'address': address,
        'ratings': rating_objects,
    }
    return render(request, 'main/address.html', context)


def search_roommate(request):
    q = request.GET.get('q')
    if q:
        roommates = Roommate.objects.filter(
            Q(name__icontains=q) |
            Q(address__icontains=q) |
            Q(email__icontains=q) |
            Q(about__icontains=q) |
            Q(social_media_link__icontains=q)
        ).distinct()
        context = {
            'roommates': roommates,
        }
        return render(request, 'main/search_roommate.html', context)

    messages.error(request, 'Please enter a search query')
    return redirect('main:home')


def search_address(request):
    q = request.GET.get('q')
    if q:
        addresses = Address.objects.filter(
            Q(address__icontains=q) |
            Q(about__icontains=q)
        ).distinct()
        context = {
            'addresses': addresses,
        }
        return render(request, 'main/search_address.html', context)

    messages.error(request, 'Please enter a search query')
    return redirect('main:home')