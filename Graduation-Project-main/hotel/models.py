from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)  # Email field for user login
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)  # Date of birth field
    is_admin = models.BooleanField(default=False)  # True if the user is an admin
    gender = models.CharField(max_length=10)  
    is_verified = models.BooleanField(default=False)  # True if the user has verified their email

    USERNAME_FIELD = 'email'  # Use email as the username field
    REQUIRED_FIELDS = ['username', 'phone_number']
    
    def __str__(self):
        return self.email

class Hotel(models.Model):
    contact_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='hotel_images/')  # Image field for hotel images

class Room(models.Model):
    choices = (
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=20, choices=choices, default='Single')  # e.g., Single, Double, Suite
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    amenities = models.TextField()  # e.g., Wi-Fi, TV, AC, etc.
    room_image = models.ImageField(upload_to='room_images/', null=True, blank=True)  # Image field for room images

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the booking is made
    