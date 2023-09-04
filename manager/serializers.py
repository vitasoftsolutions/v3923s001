from rest_framework import serializers
from global_settings.models import Address, GlobalSettings

from manager.models import ClientLogo, Gallery, Industry, SliderItem,WelcomeSection,Image,PracticeAreas,Experiences,WhatweDidItem,WhatweDid,Team,Testimonial,Faq, WorkTechnology



#manager app serializers here
class SliderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderItem
        fields = "__all__"
        depth=2

class WelcomeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeSection
        fields = "__all__"
        depth=2

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
        depth=2

class PracticeAreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeAreas
        fields = "__all__"
        depth=2

class ExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiences
        fields = "__all__"
        depth=2

class WhatweDidItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatweDidItem
        fields = "__all__"
        depth=2

class WhatweDidSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatweDid
        fields = "__all__"
        depth=2

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"
        depth=2

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
        depth=2

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"
        depth=2
class WorkTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTechnology
        fields = "__all__"
        depth=2
class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = "__all__"
        depth=2
class ClientLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientLogo
        fields = "__all__"
        depth=2

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"
        depth=2

#############################
#global_settings serializer

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
        depth=2
class GlobalSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalSettings
        fields = "__all__"
        depth=3
    


