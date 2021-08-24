from django.db import models
from django.contrib.auth import get_user_model
class Report(models.Model):
	id = models.CharField(primary_key=True, max_length=100) # todo: can I set this myself?
	source = models.CharField(max_length=100)
	reference = models.ForeignKey('Reference', on_delete=models.CASCADE)
	state = models.CharField(max_length=100)
	payload = models.ForeignKey('Payload', on_delete=models.CASCADE)
	created = models.DateTimeField()

	def __str__(self):
		return f"Report ID: {self.id}, state: {self.state}"
	
class Reference(models.Model):
	referenceId = models.CharField(primary_key=True, max_length=100)
	referenceType = models.CharField(max_length=100)
	
	def __str__(self):
		return f"Reference ID: {self.referenceId}, type: {self.referenceType}"
	
class Payload(models.Model):
	source = models.CharField(max_length=100)
	reportType = models.CharField(max_length=100)
	message = models.CharField(max_length=100, null=True)
	reportId = models.CharField(max_length=100)
	referenceResourceId = models.CharField(primary_key=True, max_length=100)
	referenceResourceType = models.CharField(max_length=100)