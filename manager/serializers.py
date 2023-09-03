from rest_framework import serializers
from global_settings.models import Address, GlobalSettings

from manager.models import SliderItem,WelcomeSection,Image,PracticeAreas,Experiences,WhatweDidItem,WhatweDid,Team,Testimonial,Faq



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
    


#combined serializer
class GlobalContentSerializer(serializers.Serializer):
    global_Settings = GlobalSettingsSerializer(many=True)


class CombinedWedidSerializer(serializers.Serializer):
    whatdid = WhatweDidSerializer(many=True)
    whatdiditem = WhatweDidItemSerializer(many=True)

    
class CombinedSerializer(serializers.Serializer):
    global_Settings = GlobalSettingsSerializer(many=True)
    slider= SliderItemSerializer(many=True)
    practice_areas= PracticeAreasSerializer(many=True)
    expriences = ExperiencesSerializer(many=True)
    whatdid = WhatweDidSerializer(many=True)
    whatdiditem = WhatweDidItemSerializer(many=True)
    teams= TeamSerializer(many=True)
    testimonials= TestimonialSerializer(many=True)


class HomeSerializer(serializers.Serializer):
    global_Settings = GlobalSettingsSerializer(many=True)
    welcome = WelcomeSectionSerializer(many=True)
    slider= SliderItemSerializer(many=True)
    practice_areas= PracticeAreasSerializer(many=True)
    expriences = ExperiencesSerializer(many=True)
    whatdid = WhatweDidSerializer(many=True)
    whatdiditem = WhatweDidItemSerializer(many=True)
    teams= TeamSerializer(many=True)
    testimonials= TestimonialSerializer(many=True)


class AboutSerializer(serializers.Serializer):
    global_Settings = GlobalSettingsSerializer(many=True)
    expriences = ExperiencesSerializer(many=True)
    teams= TeamSerializer(many=True)



class TeamSerializer(serializers.Serializer):
    global_Settings = GlobalSettingsSerializer(many=True)
    teams= TeamSerializer(many=True)



class FaqSerializer(serializers.Serializer):
    global_Settings = GlobalSettingsSerializer(many=True)
    faqs=FaqSerializer(many=True)



class PracticeAreaSerializer(serializers.Serializer):
    global_Settings = GlobalSettingsSerializer(many=True)
    practice_areas= PracticeAreasSerializer(many=True)




class ContactSerializer(serializers.Serializer):
    address = AddressSerializer(many=True)
    global_Settings = GlobalSettingsSerializer(many=True)