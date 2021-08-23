from django.contrib import admin
from .models import Report, Reference, Payload

# Register your models here.

class ReportAdmin (admin.ModelAdmin):
	list_display = ('id', 'source', 'state', 'created')
	
class ReferenceAdmin (admin.ModelAdmin):
	pass
	
class PayloadAdmin (admin.ModelAdmin):
	pass	

# Register your models here.
admin.site.register(Report, ReportAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Payload, PayloadAdmin)