from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TwitterHashSerializer
from .models import TwitterHash

# Create your views here.

class TwitterView(viewsets.ModelViewSet):
    serializer_class = TwitterHashSerializer
    queryset = TwitterHash.objects.all()
    