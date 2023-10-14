from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    phone = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    class Meta:
        db_table = 'user_profile'
        managed = True
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username
