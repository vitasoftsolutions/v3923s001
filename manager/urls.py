from django.urls import path

from . import views
urlpatterns = [
    
    path('global-data', views.GlobalDataView.as_view(), name='global-data'),
    path('hero', views.SliderItemDataView.as_view(), name='hero'),
    path('who-we-are', views.WelcomeSectionDataView.as_view(), name='who-we-are'),
    path('images', views.ImageDataView.as_view(), name='images'),
    path('services', views.PracticeAreasDataView.as_view(), name='services'),
    path('work-counter', views.WhatweDidDataView.as_view(), name='work-counter'),
    
    path('faqs', views.FaqDataView.as_view(), name='faqs'),
    path('teams', views.TeamDataView.as_view(), name='teams'),
    path('testimonials', views.TestimonialDataView.as_view(), name='testimonials'),
    path('work-technology', views.WorkTechnologyDataView.as_view(), name='work-technology'),
    path('serve-industry', views.IndustryDataView.as_view(), name='serve-industry'),
    path('client-logo', views.ClientLogoDataView.as_view(), name='client-logo'),
    path('gallery', views.GalleryDataView.as_view(), name='gallery'),
    
]
