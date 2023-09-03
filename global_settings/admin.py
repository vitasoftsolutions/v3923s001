from django.contrib import admin
from global_settings.models import GlobalSettings,Address, Social
from solo.admin import SingletonModelAdmin
# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(GlobalSettings)
class GlobalSettingsAdmin(SingletonModelAdmin):
    list_display = ['company_name']
@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['name']