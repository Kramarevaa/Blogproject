from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=150, blank=True, default='')
    about = models.TextField(default='', blank=True)
    profile_image = models.ImageField(upload_to='profile_image/%Y/%m/%d', default='default/default_profile_image.png', verbose_name='Profile Image', blank=True)
    profile_image_thumbnail = models.ImageField(upload_to='profile_image_thumbnail/%Y/%m/%d', blank=True, verbose_name='Profile Image Thumbnail')

    def __str__(self):
        return self.user_profile.get_full_name()