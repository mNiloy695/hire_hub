from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.
class JobModelAdmin(admin.ModelAdmin):
    list_display=['id','title','company_name','location',"job_type"]
    
    # def employee_name(self,obj):
    #     return obj.user.first_name +" "+obj.user.last_name
    

admin.site.register(models.JobModel,JobModelAdmin)

class CompanyModelAdmin(admin.ModelAdmin):
      prepopulated_fields = {'slug': ('name',)}
      list_display=['name','slug']

admin.site.register(models.Company,CompanyModelAdmin)
class ApllyModelAdmin(admin.ModelAdmin):
    list_display=['job_title','status']

    def job_title(self,obj):
        return obj.job.title
    def save_model(self, request, obj, form, change):
       if change and (obj.status=='Rejected' or obj.status=='Accepted'):
           subject='Application update'
           body=render_to_string('applied_updation.html',{"status":obj.status})
           email=EmailMultiAlternatives(subject,'',to=[obj.user.email])
           email.attach_alternative(body,'text/html')
           email.send()
           print("inside the save model")
           return super().save_model(request, obj, form, change)
           
admin.site.register(models.ApplyModel,ApllyModelAdmin)
