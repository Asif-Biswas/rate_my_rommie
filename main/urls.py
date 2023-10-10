from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('add-roommate/', views.add_roommate, name='add_roommate'),
    path('add-address/', views.add_address, name='add_address'),
    path('roommate/<int:roommate_id>/', views.roommate, name='roommate'),
]