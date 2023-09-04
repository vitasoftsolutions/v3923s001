from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from global_settings.models import Address, GlobalSettings
from manager.models import ClientLogo, Gallery, Industry, SliderItem,WelcomeSection,Image,PracticeAreas,Experiences,WhatweDidItem,WhatweDid,Team,Testimonial,Faq, WorkTechnology
from manager.serializers import  ClientLogoSerializer, FaqSerializer, GallerySerializer,GlobalSettingsSerializer, ImageSerializer, IndustrySerializer, PracticeAreasSerializer, SliderItemSerializer, TeamSerializer, TestimonialSerializer, WelcomeSectionSerializer, WhatweDidSerializer, WorkTechnologySerializer
# Create your views here.

    
class GlobalDataView(APIView):
    def get(self, request, format=None):
        queryset = GlobalSettings.objects.all()
        serializer = GlobalSettingsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

############################
class SliderItemDataView(APIView):
    def get(self, request, format=None):
        queryset = SliderItem.objects.all()
        serializer = SliderItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class WelcomeSectionDataView(APIView):
    def get(self, request, format=None):
        queryset = WelcomeSection.objects.all()
        serializer = WelcomeSectionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ImageDataView(APIView):
    def get(self, request, format=None):
        queryset = Image.objects.all()
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class PracticeAreasDataView(APIView):
    def get(self, request, format=None):
        queryset = PracticeAreas.objects.all()
        serializer = PracticeAreasSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class WhatweDidDataView(APIView):
    def get(self, request, format=None):
        queryset = WhatweDid.objects.all()
        serializer = WhatweDidSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FaqDataView(APIView):
    def get(self, request, format=None):
        queryset = Faq.objects.all()
        serializer = FaqSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TeamDataView(APIView):
    def get(self, request, format=None):
        queryset = Team.objects.all()
        serializer = TeamSerializer(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TestimonialDataView(APIView):
    def get(self, request, format=None):
        queryset = Testimonial.objects.all()
        serializer = TestimonialSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class WorkTechnologyDataView(APIView):
    def get(self, request, format=None):
        queryset= WorkTechnology.objects.all()
        serializer = WorkTechnologySerializer(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class IndustryDataView(APIView):
    def get(self, request, format=None):
        queryset = Industry.objects.all()
        serializer = IndustrySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GalleryDataView(APIView):
    def get(self, request, format=None):
        queryset = Gallery.objects.all()
        serializer = GallerySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ClientLogoDataView(APIView):
    def get(self, request, format=None):
        queryset = ClientLogo.objects.all()
        serializer = ClientLogoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)