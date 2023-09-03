from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from global_settings.models import Address, GlobalSettings
from manager.models import SliderItem,WelcomeSection,Image,PracticeAreas,Experiences,WhatweDidItem,WhatweDid,Team,Testimonial,Faq
from manager.serializers import AboutSerializer, CombinedSerializer, ContactSerializer, FaqSerializer,GlobalSettingsSerializer,GlobalContentSerializer, HomeSerializer, PracticeAreaSerializer, TeamSerializer
# Create your views here.
class CombinedDataView(APIView):
    def get(self, request, format=None):
        global_Settings = GlobalSettings.objects.all()
        slider = SliderItem.objects.all()
        practice_areas = PracticeAreas.objects.all()
        expriences = Experiences.objects.all()
        whatdid = WhatweDid.objects.all()
        whatwediditem = WhatweDidItem.objects.all()
        teams = Team.objects.all()
        testimonials = Testimonial.objects.all()
        welcome= WelcomeSection.objects.all()
        serializer = CombinedSerializer({
            'global_Settings': global_Settings,
            'slider': slider,
            'welcome':welcome,
            'practice_areas': practice_areas,
            'expriences': expriences,
            'whatdid': whatdid,
            'whatdiditem':whatwediditem,
            'teams': teams,
            'testimonials': testimonials,
        })

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GlobalDataView(APIView):
    def get(self, request, format=None):
        global_Settings = GlobalSettings.objects.all()
        serializer = GlobalContentSerializer({
            'global_Settings': global_Settings,
            
        })
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class HomeDataView(APIView):
    def get(self, request, format=None):
        global_Settings = GlobalSettings.objects.all()
        slider = SliderItem.objects.all()
        practice_areas = PracticeAreas.objects.all()
        expriences = Experiences.objects.all()
        whatdid = WhatweDid.objects.all()
        whatwediditem = WhatweDidItem.objects.all()
        teams = Team.objects.all()
        testimonials = Testimonial.objects.all()
        welcome= WelcomeSection.objects.all()

        serializer = HomeSerializer({
            'global_Settings': global_Settings,
            'slider': slider,
            'welcome':welcome,
            'practice_areas': practice_areas,
            'expriences': expriences,
            'whatdid': whatdid,
            'whatdiditem':whatwediditem,
            'teams': teams,
            'testimonials': testimonials,
        })

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AboutDataView(APIView):
    def get(self, request, format=None):
        global_Settings = GlobalSettings.objects.all()
        expriences = Experiences.objects.all()
        teams = Team.objects.all()

        serializer = AboutSerializer({
            'global_Settings': global_Settings,
            'expriences': expriences,
            'teams': teams,
        })

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TeamDataView(APIView):
    def get(self, request, format=None):
        global_Settings = GlobalSettings.objects.all()
        teams = Team.objects.all()
        serializer = TeamSerializer({
            'global_Settings': global_Settings,
            'teams': teams,
        })

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FaqDataView(APIView):
    def get(self, request, format=None):
        global_Settings = GlobalSettings.objects.all()
        faqs = Faq.objects.all()

        serializer = FaqSerializer({
            'global_Settings': global_Settings,
            'faqs': faqs,
        })

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PracticeDataView(APIView):
    def get(self, request, format=None):
        global_Settings = GlobalSettings.objects.all()
        practice_areas = PracticeAreas.objects.all()
        serializer = PracticeAreaSerializer({
            'global_Settings': global_Settings,
            'practice_areas': practice_areas,
        })

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ContactDataView(APIView):
    def get(self, request, format=None):
        global_Settings = GlobalSettings.objects.all()
        address = Address.objects.all()

        serializer = ContactSerializer({
            'global_Settings': global_Settings,
            'address': address,
        })

        return Response(serializer.data, status=status.HTTP_200_OK)
