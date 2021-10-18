from django.shortcuts import render
from rest_framework import generics
from Inspection.models import Details       
from Inspection.Serializers import DetailsSerializer



class UserDetails (generics.ListCreateAPIView) :
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

class Useredit (generics.RetrieveUpdateDestroyAPIView) :
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer





