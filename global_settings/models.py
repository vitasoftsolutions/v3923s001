from django.db import models
from solo.models import SingletonModel
from django.urls import reverse
# Create your models here.
class Social(models.Model):
    name= models.CharField(max_length=20)
    link = models.URLField()
    icon_class = models.CharField(max_length=50)
class Address(models.Model):
    title = models.CharField(max_length=200)
    address = models.TextField(max_length=500)
    phone_no= models.CharField(max_length=200)
    email=models.EmailField()
    head_branch = models.BooleanField()
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Address"
class GlobalSettings(SingletonModel):
    company_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="upload")
    logo_dark = models.ImageField(upload_to="upload",null=True,blank=True)
    address = models.ManyToManyField(Address)
    welcome_text = models.TextField(max_length=500)
    company_number = models.CharField(max_length=200)
    copyright_text = models.TextField(max_length=500)
    ceo_sign= models.ImageField(upload_to="upload",null=True,blank=True)
    social = models.ManyToManyField(Social)
    def __str__(self):
        return f"{self.company_name}"
    def get_image_path(self):
        return reverse('global-settings-image', kwargs={'pk': self.pk})
    class Meta:
        verbose_name = "Global Setting"