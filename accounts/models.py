from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from job.models import Company
class CustomUserModel(AbstractUser):
    account_type={
        ("Viewer","Viewer"),
        ("admin","Admin"),
        ("Employee","Employee"),
        ("Job Seeker","Job Seeker"),
    }
    confirm_password=models.CharField(max_length=100,blank=True,null=True)
    type=models.CharField(choices=account_type,default="Viewer",max_length=40)
    company=models.ForeignKey(Company,blank=True,null=True,on_delete=models.CASCADE,default=None)

  
    


