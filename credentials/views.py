from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from credentials.serializers import InformationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView

from .models import (
    Information
)
from .serializers import (
    InformationSerializer,
)


class InformationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
