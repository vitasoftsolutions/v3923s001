from django.db import models
from global_settings.models import Social
from solo.models import SingletonModel
# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="upload")
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Images"
class SliderItem(models.Model):
    welcome_text= models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null=True,blank=True)
    video= models.URLField(null=True,blank=True)
    text = models.TextField(max_length=500)
    button_text = models.CharField(max_length=200)
    button_link = models.URLField()
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Hero Items"
class WelcomeSection(SingletonModel):
    title = models.CharField(max_length=200)
    desscription = models.TextField(max_length=500)
    image_horizontal = models.ImageField(upload_to="upload",null=True,blank=True)
    image_vertical = models.ImageField(upload_to="upload",null=True,blank=True)
    video = models.URLField(blank=True,null=True)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Who we are"
class PracticeAreas(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null=True,blank=True)
    icon = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Service"
class Experiences(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Experiences"
class WhatweDidItem(models.Model):
    title = models.CharField(max_length=200)
    number = models.IntegerField(blank=True,null=True)
    image = models.ImageField(upload_to="upload",null=True,blank=True)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Work Counter Item"

class WhatweDid(SingletonModel):
    title = models.CharField(max_length=200)
    item = models.ManyToManyField(WhatweDidItem)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Work Counter"
class Team(models.Model):
    name=models.CharField(max_length=200)
    designation= models.CharField(max_length=200)
    description =models.TextField(max_length=500)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,null=True,blank=True)
    social = models.ManyToManyField(Social)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Team"
class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    description =models.TextField(max_length=500)
    proffession=models.CharField(max_length=200)
    image = models.ImageField(upload_to="upload",null=True,blank=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Testimonial"
class Faq(models.Model):
    question=models.CharField(max_length=200)
    answer =models.TextField(max_length=500)
    OPTION_a = 'General'
    OPTION_b = 'Advanced'
    CHOICES2 = (
        (OPTION_a, 'General'),
        (OPTION_b, 'Advanced'),
        
    )
    category = models.CharField(
        max_length=20,
        choices=CHOICES2,
        default=OPTION_a  # You can set the default to your preference
    )
    def __str__(self):
        return f"{self.question}"
    class Meta:
        verbose_name = "Faq"

class WorkTechnology(models.Model):
    OPTION_c = 'Frontend'
    OPTION_d = 'Backend'
    OPTION_e = 'Mobile Application'
    OPTION_f = 'Database'
    CHOICES5 = (
        (OPTION_c, 'Frontend'),
        (OPTION_d, 'Backend'),
        (OPTION_e, 'Mobile Application'),
        (OPTION_f, 'Database'),
        
    )
    category = models.CharField(
        max_length=20,
        choices=CHOICES5,
        default=OPTION_c  # You can set the default to your preference
    )
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="upload",null=True,blank=True)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Work Technology"
class Industry(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="upload",null=True,blank=True)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Serve Industry"
class ClientLogo(models.Model):
    company_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="upload",null=True,blank=True)
    def __str__(self):
        return f"{self.company_name}"
    class Meta:
        verbose_name = "Client Company"
class Gallery(SingletonModel):
    name= models.CharField(max_length=20)
    images = models.ManyToManyField(Image)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Gallery"
