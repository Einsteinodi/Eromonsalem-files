from django.db import models

# Create your models here.


class ServiceModel(models.Model):
    SERVICE_CHOICES = [
    ('Web design','WEB DESIGN'),
    ('Project management', 'PROJECT MANAGEMENT'),
    ('It training','IT TRAINING'),
    ('Remote support','REMOTE SUPPORT'),
    ('Cloud computing','CLOUD COMPUTING'),
    ('Programming and development','PROGRAMMING AND DEVELOPMENT'),]


    Fullname=models.CharField(max_length=264 ,unique=True)
    Email=models.EmailField(max_length=265, unique=True)
    service=models.CharField(max_length=50, choices=SERVICE_CHOICES ,default='Web design')





class contactModel(models.Model):
    fullname=models.CharField(max_length=264,unique=True)
    email=models.EmailField(max_length=265,unique=True)
    message=models.CharField(max_length=500)