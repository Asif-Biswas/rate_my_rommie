from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('add-roommate/', views.add_roommate, name='add_roommate'),
    path('add-address/', views.add_address, name='add_address'),
    path('roommate/<int:roommate_id>/', views.roommate, name='roommate'),
    path('address/<int:address_id>/', views.address, name='address'),
    path('address-roommates/<int:address_id>/', views.address_roommates, name='address_roommates'),
    path('search-roommate/', views.search_roommate, name='search_roommate'),
    path('search-address/', views.search_address, name='search_address'),
    path('rate-existing-roommate/<int:roommate_id>/', views.rate_existing_roommate, name='rate_existing_roommate'),
    path('rate-existing-address/<int:address_id>/', views.rate_existing_address, name='rate_existing_address'),
    path('all-roommates/', views.all_roommates, name='all_roommates'),
    path('all-addresses/', views.all_addresses, name='all_addresses'),
]