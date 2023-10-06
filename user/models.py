from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    pf_no = models.IntegerField(null=True, unique=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_Images')

    def __str__(self):
        return f'{self.staff.username} - profile'
    

class Officer(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    pf_no = models.IntegerField(null=True, unique=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_Images')

    def __str__(self):
        return f'{self.staff.username} - Oficcer Profile'


class Supervisor(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    pf_no = models.IntegerField(null=True, unique=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_Images')

    def __str__(self):
        return f'{self.staff.username} -Supervisor profile'
    

class Assistant(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    pf_no = models.IntegerField(null=True, unique=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_Images')

    def __str__(self):
        return f'{self.staff.username} - Assistant profile'
    
