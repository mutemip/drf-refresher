from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250)
    city = models.CharField(max_length=40)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class ProfileStatus(models.Model):
    profile = models.ForeignKey('Profile', related_name='statuses', on_delete=models.CASCADE)
    status_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self):
        return str(self.user_profile)
