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

		
	
class ReferenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reference
		fields = '__all__'

class PayloadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payload
		fields = '__all__'
class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = '__all__'

class ReportNestedSerializer(serializers.ModelSerializer):
	reference = ReferenceSerializer()
	payload = PayloadSerializer()

	class Meta:
		model = Report
		fields = '__all__'
		
	# def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
		
	# def create(self, validated_data):
		
	# 	reference = Reference.objects.create(**validated_data.pop('reference'))
	# 	payload = Payload.objects.create(**validated_data.pop('payload'))
	# 	report = Report.objects.create(reference=reference, payload=payload, **validated_data)
	# 	return report

	# def destroy(self,request,*args,**kwargs):
	# 	reports = Report.objects.all()
	# 	for report in reports:
	# 		report.delete()
	# 		return JsonResponse({"status":"ok"}, status=status.HTTP_200_OK)
	# 	return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)