from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    

class Roommate(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    social_media_link = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.address}'
    
    def get_total_rating(self):
        ratings = RoommateRating.objects.filter(roommate=self)
        return len(ratings)
    
    def get_average_rating(self):
        ratings = RoommateRating.objects.filter(roommate=self)
        if ratings:
            total = 0
            for rating in ratings:
                total += rating.rating
            return float("{:.1f}".format(total / len(ratings)))
        else:
            return 0
        
    def get_star(self):
        average_rating = self.get_average_rating()
        stars = []
        for i in range(1, 6):
            if i <= average_rating:
                stars.append('fas fa-star')
            elif i - average_rating < 1:
                stars.append('fas fa-star-half-alt')
            else:
                stars.append('far fa-star')

        return stars
    
    def get_top_two_ratings(self):
        ratings = RoommateRating.objects.filter(roommate=self).order_by('-rating')
        if len(ratings) < 2:
            return ratings
        top_two = []
        top_two.append(ratings[0])
        top_two.append(ratings[len(ratings)-1])
        return top_two
    
    def get_total_user_rated(self):
        ratings = RoommateRating.objects.filter(roommate=self)
        users = []
        for rating in ratings:
            if rating.user not in users:
                users.append(rating.user)
        return len(users)
    
    def all_ratings(self):
        ratings = RoommateRating.objects.filter(roommate=self)
        return ratings



class RoommateRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roommate = models.ForeignKey(Roommate, on_delete=models.CASCADE)
    attribute = models.CharField(max_length=100)
    rating = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.roommate.name} - {self.attribute} - {self.rating}'
    
    def get_percentage(self):
        ratings = RoommateRating.objects.filter(roommate=self.roommate, attribute=self.attribute)
        total = 0
        for rating in ratings:
            total += rating.rating
        return int((total / (len(ratings)*5)) * 100)
    
    def get_star(self):
        stars = []
        for i in range(1, 6):
            if i <= self.rating:
                stars.append('fas fa-star')
            elif i - self.rating < 1:
                stars.append('fas fa-star-half-alt')
            else:
                stars.append('far fa-star')

        return stars
    


class Address(models.Model):
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.address}'
    
    def get_total_rating(self):
        ratings = AddressRating.objects.filter(address=self)
        return len(ratings)
    
    def get_average_rating(self):
        ratings = AddressRating.objects.filter(address=self)
        if ratings:
            total = 0
            for rating in ratings:
                total += rating.rating
            return float("{:.1f}".format(total / len(ratings)))
        else:
            return 0
        
    def get_star(self):
        average_rating = self.get_average_rating()
        stars = []
        for i in range(1, 6):
            if i <= average_rating:
                stars.append('fas fa-star')
            elif i - average_rating < 1:
                stars.append('fas fa-star-half-alt')
            else:
                stars.append('far fa-star')

        return stars
    
    def get_top_two_ratings(self):
        ratings = AddressRating.objects.filter(address=self).order_by('-rating')
        if len(ratings) < 2:
            return ratings
        top_two = []
        top_two.append(ratings[0])
        top_two.append(ratings[len(ratings)-1])
        return top_two
    
    def get_total_user_rated(self):
        ratings = AddressRating.objects.filter(address=self)
        users = []
        for rating in ratings:
            if rating.user not in users:
                users.append(rating.user)
        return len(users)
    
    def all_ratings(self):
        ratings = AddressRating.objects.filter(address=self)
        return ratings


class AddressRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    attribute = models.CharField(max_length=100)
    rating = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.address.address} - {self.attribute} - {self.rating}'
    
    def get_percentage(self):
        ratings = AddressRating.objects.filter(address=self.address, attribute=self.attribute)
        total = 0
        for rating in ratings:
            total += rating.rating
        return int((total / (len(ratings)*5)) * 100)
    
    def get_star(self):
        stars = []
        for i in range(1, 6):
            if i <= self.rating:
                stars.append('fas fa-star')
            elif i - self.rating < 1:
                stars.append('fas fa-star-half-alt')
            else:
                stars.append('far fa-star')

        return stars