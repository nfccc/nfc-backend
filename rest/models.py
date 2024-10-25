# models.py
from timeit import default_timer
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField
import cloudinary.uploader
import logging

logger = logging.getLogger(__name__)

class Password(models.Model): ## TO BE REMOVED
    password = models.CharField(max_length=255)


class Girls(models.Model):
    name = models.CharField(max_length=100)  # Ensure name starts with a capital letter
    subname = models.CharField(max_length=100, default="Default Subname")  # Subname field
    bio = models.TextField()  # Bio field
    avatar = models.ImageField(upload_to='Ai-Girls', null=True, blank=True)  # Avatar image
    header_image = models.ImageField(upload_to='Ai-Girls', null=True, blank=True)  # Header image
    subscription_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Subscription price
    tips = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Tips
    online_status = models.BooleanField(default=False)  # Online status
    last_active = models.DateTimeField(null=True, blank=True)  # Last active
    country = models.CharField(max_length=100, null=True, blank=True)  # Country
    likes_count = models.PositiveIntegerField(default=0)  # Likes count
    
    def save(self, *args, **kwargs):
        # Ensure name starts with a capital letter
        self.name = self.name.capitalize()
        super(Girls, self).save(*args, **kwargs)



class Photo(models.Model):
    girl = models.ForeignKey(Girls, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='girl_photos')
    caption = models.CharField(max_length=255, null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    share = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo of {self.girl}"
    
# class Boo(models.Model):
#     pass


# class Bae(models.Model):
#     pass


class Photos(models.Model):
    likes = models.PositiveIntegerField(default=0)


class Video(models.Model):
    girl = models.ForeignKey(Girls, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=100, )
    video_file = models.FileField(upload_to='gallery_videos', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.video_file:
            try:
                # Check if the file is a video
                if self.video_file.name.endswith(('.mp4', '.avi', '.mov')):
                    # Upload video to Cloudinary specifying the resource type
                    response = cloudinary.uploader.upload_large(
                        self.video_file,
                        resource_type='video'
                    )
                    # Set the video_file field to the secure URL from Cloudinary
                    self.video_file = response['secure_url']
                else:
                    raise ValueError('Invalid video file format')
            except Exception as e:
                # Log the error for debugging
                logger.error(f"Error uploading video: {e}")
                raise
        super().save(*args, **kwargs)









    
    



    # Add more fields as needed, such as title, description, etc.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username

class Creator(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='creator_profile',   null=True, blank=True) # type: ignore
    name = models.CharField(max_length=100)  # Ensure name starts with a capital letter
    subname = models.CharField(max_length=100, default="Default Subname")  # Subname field
    bio = models.TextField()  # Bio field
    avatar = models.ImageField(upload_to='Ai-Girls', null=True, blank=True)  # Avatar image
    header_image = models.ImageField(upload_to='Ai-Girls', null=True, blank=True)  # Header image
    subscription_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Subscription price
    tips = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Tips
    online_status = models.BooleanField(default=False)  # Online status
    last_active = models.DateTimeField(null=True, blank=True)  # Last active
    country = models.CharField(max_length=100, null=True, blank=True)  # Country
    likes_count = models.PositiveIntegerField(default=0)  # Likes count
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')  # Gender

    def __str__(self):
        return self.name

    
    




class Auction(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=50)
    image = models.ImageField(upload_to='auction_images/')

    def __str__(self):
        return self.name
    


class Adverts(models.Model):
    image = models.ImageField(upload_to='advert_images/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    





    
    
    
    
    


  
  
  
