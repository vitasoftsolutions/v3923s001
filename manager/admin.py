from django.contrib import admin

from manager.models import ClientLogo, Experiences, Faq, Gallery, Image, Industry, PracticeAreas, SliderItem, Team, Testimonial, WelcomeSection, WhatweDid, WhatweDidItem, WorkTechnology
from solo.admin import SingletonModelAdmin
# Register your models here.
@admin.register(Image)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(SliderItem)
class SldiderItemAdmin(SingletonModelAdmin):
    list_display = ['title','text']
@admin.register(WelcomeSection)
class TermsAdmin(SingletonModelAdmin):
    list_display = ['title']

@admin.register(PracticeAreas)
class PracticeAreaAdmin(admin.ModelAdmin):
    list_display = ['title','text']

@admin.register(WhatweDidItem)
class WhatweDidItemAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(WhatweDid)
class WhatweDidAdmin(SingletonModelAdmin):
    list_display = ['title']
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','description']
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question']
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(WorkTechnology)
class WorkTechnologyAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(ClientLogo)
class ClientLogoAdmin(admin.ModelAdmin):
    list_display = ['company_name']
@admin.register(Gallery)
class GalleryAdmin(SingletonModelAdmin):
    list_display = ['name']
