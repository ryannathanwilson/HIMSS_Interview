from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Report, Reference, Payload

# todo: delete UserSerializer if not used
class UserSerializer(serializers.ModelSerializer): 
	email = serializers.EmailField( required=True )
	username = serializers.CharField() 
	password = serializers.CharField(min_length=8, write_only=True) 

	class Meta: 
		model = get_user_model() 
		fields = ('email', 'username', 'password', 'id') 
		extra_kwargs = {'password': {'write_only': True}} 
 
	def create(self, validated_data): 
		password = validated_data.pop('password', None) 
		instance = self.Meta.model(**validated_data) 
		instance.set_password(password) 
		instance.save() 
		return instance

class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = '__all__'
		
	
class ReferenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reference
		fields = '__all__'

class PayloadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payload
		fields = '__all__'