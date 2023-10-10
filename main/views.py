from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def add_roommate(request):
    return render(request, 'main/add_roommate.html')


def add_address(request):
    return render(request, 'main/add_address.html')