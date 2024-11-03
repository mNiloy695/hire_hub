from django.shortcuts import render
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from . serializers import JobModelSerializer,ApplyModelSerializer,CompanyModelSerializer
from . import models
from  rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.http import Http404
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.filters import SearchFilter,BaseFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
# Create your views here.
# class EmployeeCheck(BasePermission):
#     def has_permission(self, request, view):
#         if request.user.type =='Employee' or  request.user.is_staff:
#                 return  True
#         else:
#              return False
        
# def SpecificEmployeeFilter(BaseFilterBackend):
#      def get_queryset(self,request,queryset,view):
#           employee_id=request.query_params.get('employee_id')
#           if employee_id:
#                return queryset.filter(user=employee_id)
#           return queryset
         
     

class JobListView(APIView):
     def post(self, request):
        # Check if user has the right type or is staff
        if not request.user.is_authenticated:
             return Response({"error": "You don't have permission to access this resource."},
                            status=status.HTTP_403_FORBIDDEN)
             
        if request.user.is_authenticated and request.user.type != 'Employee' and not request.user.is_staff:
            return Response({"error": "You don't have permission to access this resource."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = JobModelSerializer(data=request.data)
        if serializer.is_valid():
            location=serializer.validated_data['location'].lower()
            serializer.validated_data['location']=location
            serializer.save()
            return Response({"message": "Job posted successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     def get(self,request): 
           jobs=models.JobModel.objects.all()
           employee_id=request.query_params.get('employee_id')
           company=request.query_params.get('company')
           location=request.query_params.get('location')
           time=request.query_params.get('time')
           
           if employee_id:
                jobs=models.JobModel.objects.filter(user=employee_id)
           elif company:
                jobs=models.JobModel.objects.filter(company_name=company)
           elif location:
                 location=location.lower()
                 jobs=models.JobModel.objects.filter(location=location)
           elif time:
                jobs=models.JobModel.objects.filter(time=time)          
           serializer=JobModelSerializer(jobs,many=True)
           
           return Response(serializer.data,status=status.HTTP_200_OK)
         


class JobDetailView(APIView):
     def get_object(self,pk):
          try:
               return models.JobModel.objects.get(pk=pk)
          except(models.JobModel.DoesNotExist):
               raise Http404
     def get(self,request,pk,format=None):
          job=self.get_object(pk)
          serializer=JobModelSerializer(job)
          return Response(serializer.data,status=status.HTTP_200_OK)
     def put(self,request,pk,format=None):
          job=self.get_object(pk)
          serializer=JobModelSerializer(job,data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response('job model successfully updated')
          else:
               return Response(serializer.errors)
     def delete(self,request,pk,format=None):
          job=self.get_object(pk)
          job.delete()
          return Response('The Job model successfully deleted')
     def patch(self,request,pk,format=None):
          job=self.get_object(pk)
          serializer=JobModelSerializer(job,data=request.data,partial=True)
          if serializer.is_valid():
               serializer.save()
               return Response("data partially updated")
          return Response(serializer.errors)
     
class ApplyListView(APIView):
     def post(self,request):
          if not request.user.is_authenticated:
               return Response({"detail":"You don't have permission vai"})
          if request.user.type!='Job Seeker':
                return Response({"detail":"Youuu don't have permission"})
          serializer=ApplyModelSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               subject='Apply for Job'
               body=render_to_string('apply_mail.html',{"name":f"{request.user.first_name}' '+{request.user.last_name}"})
               email=EmailMultiAlternatives(subject,'',to=[request.user.email])
               email.attach_alternative(body,'text/html')
               email.send()
               return Response({"detail":"Applied successfully"})
          return Response(serializer.errors)
     def get(self,request):
          print("Authenticated User ",request.user)
          if request.user.is_authenticated:
               applies=models.ApplyModel.objects.all()
               user_id=request.query_params.get('user_id')
               job_user_id=request.query_params.get('job_user_id')
               print("yesss")
               if user_id:
                    applies=models.ApplyModel.objects.filter(user=user_id)
               if job_user_id:
                    print("yesss")
                    
                    applies=models.ApplyModel.objects.filter(job__user=job_user_id)
                    print(applies)
                    print("yesss")
               # print(applies[3].job.user)
               serializer=ApplyModelSerializer(applies,many=True)
               return Response(serializer.data)
          else:
               return Response("You don't havee the permisson")
         




class ApplyDetailView(APIView):
     permission_classes=[IsAuthenticated]
     def get_object(self,pk):
      try:
          return models.ApplyModel.objects.get(pk=pk)
      except(models.ApplyModel.DoesNotExist):
          raise Http404

     def get(self,request,pk):
          apply=self.get_object(pk)
          serializer=ApplyModelSerializer(apply)
          return Response(serializer.data)
     def put(self,request,pk):
          apply=self.get_object(pk)
          serializer=ApplyModelSerializer(apply,data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          else:
               return Response(serializer.errors)
     def patch(self,request,pk):
          apply=self.get_object(pk)
          serializer=ApplyModelSerializer(apply,data=request.data,partial=True)
          if serializer.is_valid():
               serializer.save()
               status=serializer.validated_data['status']
               if status=='Cancelled':
                    subject='Application update'
                    body=render_to_string('applied_updation.html',{"status":status})
                    email=EmailMultiAlternatives(subject,'',to=[request.user.email])
                    email.attach_alternative(body,'text/html')
                    email.send()
                    return Response(serializer.data)
          return Response(serializer.errors)
     def delete(self,request,pk):
          apply=self.get_object(pk)
          apply.delete()
          return Response('apply model successfully deleted')
class CompanyView(ModelViewSet):
     serializer_class=CompanyModelSerializer
     queryset=models.Company.objects.all()