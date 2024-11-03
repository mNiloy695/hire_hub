from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUserModel


class RegistrationSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=CustomUserModel
        fields=['id','username','first_name','last_name','type','email','password','confirm_password','company']
    def save(self):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email=self.validated_data['email']
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']
        type=self.validated_data['type']
        company=self.validated_data['company']
        if password != confirm_password:
            raise serializers.ValidationError({"error":"your confirm password does'nt match"})
        if CustomUserModel.objects.filter(username=username).exists():
            raise serializers.ValidationError({"error":"The username Alrady exist"})
        if CustomUserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"The email already exists"})
        if type=='Employee' and not company:
            raise serializers.ValidationError({"error":'You must be needed to set company'})
        account=CustomUserModel(username=username,first_name=first_name,last_name=last_name,email=email,type=type,company=company)
    
        account.set_password(password)
        account.is_active=False
        account.save()
        return account
class RegistrationDetailSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=CustomUserModel
        fields=['username','first_name','last_name','type','email','password','confirm_password','company']
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()