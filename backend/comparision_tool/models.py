from django.db import models

# Create your models here.
from django.db import models
# from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(models.Model):
    username = models.CharField(max_length=150, null=False)
    def __str__(self):
        return self.username
class SavedQueries(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    query_name =  models.CharField(max_length=250)
    query_description = models.TextField()
    first_country = models.CharField(max_length=100, null=False, default='Colombia')
    second_country = models.CharField(max_length=100, null=True, blank=True)
    first_date = models.DateField(null=False, default=timezone.now())
    second_date = models.DateField(null=True,blank=True)
    query_quantity = models.IntegerField(null=False, default=1)

    def __str__(self):
        return self.query_name

class Comments(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    saved_query_reference = models.ForeignKey(SavedQueries, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
