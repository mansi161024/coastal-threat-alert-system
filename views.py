from rest_framework import viewsets
from backend.models import SafeZone, Alert
from backend.serializer import SafeZoneSerializer, AlertSerializer

class SafeZoneViewSet(viewsets.ModelViewSet):
    queryset = SafeZone.objects.all()
    serializer_class = SafeZoneSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Alerts app working fine!")    