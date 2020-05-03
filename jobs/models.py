from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    jobtitle = models.CharField(max_length=601, default='none')
    location = models.CharField(max_length=600, default= 'none')
    timepd = models.CharField(max_length=600, default= 'none')
    summary = models.TextField()
