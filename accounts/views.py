from django.shortcuts import render,redirect
from .serializers import RegistrationSerializer,LoginSerializer,RegistrationDetailSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from . models import CustomUserModel
from rest_framework.permissions import BasePermission
from django.contrib.auth import login,logout
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework import serializers
from django.http import Http404
from rest_framework import status

class RegistrationView(APIView):

    # def get(self,request,format=None):
    #     users=CustomUserModel.objects.all()
    #     serializer=RegistrationSerializer(users,many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token=default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link=f'https://hire-hub-bsf2.vercel.app/account/active/{uid}/{token}/'
            subject="registration confirm mail"
            email_body=render_to_string('confirm_mail.html',{"confirm_link":confirm_link})
            email=EmailMultiAlternatives(subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response("check your mail")
        else:
            return Response(serializer.errors)
    def get(self,request):
        users=CustomUserModel.objects.all()
        username=request.query_params.get('username')
        email=request.query_params.get('email')
        if username:
            try:
              user=CustomUserModel.objects.get(username=username)
            except CustomUserModel.DoesNotExist:
                user=None
            if(user):
                users=user
                serializer=RegistrationSerializer(users)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer=RegistrationSerializer(users,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
            



class RegistrationDetailView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self,pk):
        try:
           return CustomUserModel.objects.get(pk=pk)
        except(CustomUserModel.DoesNotExist):
            raise Http404
  
    def get(self,request,pk,format=None):
        user=self.get_object(pk)
        serializer=RegistrationDetailSerializer(user)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        user=self.get_object(pk)
        serializer=RegistrationDetailSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail":"your data updated"})
        return Response(serializer.errors)
    def delete(self,request,pk,format=None):
        user=self.get_object(pk)
        user.delete()
        return Response('User succesfully deleted')
    def patch(self,request,pk,format=None):
        
        user=self.get_object(pk)
        serializer=RegistrationDetailSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('successfully updated')
        return Response(serializer.errors)
        

def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=CustomUserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError,CustomUserModel.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
            user.is_active=True
            if user.type=='Employee':
                user.is_staff=True
            user.save()
            return redirect('https://hire-hub-fronted-d4oq.vercel.app/login.html')
        
    return redirect('registration')
        


class LoginView(APIView):
    def post(self,request,format=None):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user=authenticate(username=username,password=password)
            if user:
                token,_=Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({"token":token.key,"user_id":user.id,"is_staff":user.is_staff,"type":user.type})
            else:
                return Response({'error':"invalid user"})
        return Response(serializer.errors)
class LogoutView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        logout(request)
        return Response({'detail':'succesfully log out'})

       
