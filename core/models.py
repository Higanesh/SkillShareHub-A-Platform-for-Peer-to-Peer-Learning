from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    u_email = models.EmailField(max_length=20, default="default@gmail.com")
    gender = models.CharField(max_length=10)
    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username+" "+self.first_name+" "+self.last_name

class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str(self):
        return self.room_name
    
class Message(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    Message = models.TextField()

    def __str(self):
        return str(self.room)
