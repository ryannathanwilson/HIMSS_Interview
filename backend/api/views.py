from django.shortcuts import render
from .serializers import ReportSerializer, ReportNestedSerializer, ReferenceSerializer, PayloadSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import UpdateModelMixin
from .models import Report, Reference, Payload
import json
from datetime import datetime

class ReportView(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = Report.objects.all()
        reference = Reference.objects.all()
        payload = Payload.objects.all()
        if reference:
            for ref in reference:
                ref.delete()
        if payload:
            for pay in payload:
                pay.delete()
        
        return Response(status=status.HTTP_200_OK)
    
class ReportOpenView(viewsets.ModelViewSet):
    queryset = Report.objects.filter(ticketState="OPEN")
    serializer_class = ReportNestedSerializer


class ReferenceView(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
	
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

class PayloadView(viewsets.ModelViewSet):
    queryset = Payload.objects.all()
    serializer_class = PayloadSerializer