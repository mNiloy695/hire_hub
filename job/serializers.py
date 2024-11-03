from .  import models
from rest_framework import serializers

class JobModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.JobModel
        fields='__all__'

class ApplyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ApplyModel
        fields=['id','user','job','status','resume','apply_date']

class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Company
        fields=['id','logo','name']

