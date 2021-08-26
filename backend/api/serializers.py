from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Report, Reference, Payload

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
		