from django.db import models
from job_board import settings
# Create your models here.
JOB_TYPE={
    ('Government','Government'),
    ("Semi-Government",'Semi-Government'),
    ("Privet",'Privet'),
}
TIME={
    ('Full-Time','Full-Time'), 
    ('Half-time','Half-time'), 
    
}
class Company(models.Model):
    logo=models.CharField(max_length=200,blank=True,null=True)
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True,blank=True,null=True)
    def __str__(self):
        return  self.name
class JobModel(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='job',blank=True,null=True)
    title=models.CharField(max_length=40)
    company_name=models.ForeignKey(Company,blank=True,null=True,on_delete=models.CASCADE,related_name="company")
    discriptions=models.CharField(max_length=100000)
    requirements=models.CharField(max_length=100000)
    location=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    job_type=models.CharField(choices=JOB_TYPE,default="Privet",max_length=100)
    time=models.CharField(max_length=20,choices=TIME,default='Full-Time',blank=True,null=True)
    def __str__(self):
        return self.title

STATUS={
    ("Pending","Pending"),
    ("Accepted","Accepted"),
    ("Rejected","Rejected"),
    ("Cancelled","Cancelled"),
}
class ApplyModel(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='apply',on_delete=models.CASCADE,blank=True,null=True,unique=True)
    job=models.ForeignKey(JobModel,on_delete=models.CASCADE,related_name="job",blank=False,null=False)
    apply_date=models.DateField(auto_now_add=True)
    status=models.CharField(choices=STATUS,max_length=100,default='Pending')
    resume = models.CharField(blank=True,null=True,max_length=100)
    class Meta:
        ordering = ['-apply_date']  # Order by apply_date descending