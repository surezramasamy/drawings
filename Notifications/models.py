from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.urls import reverse

class notification(models.Model):
    date = models.DateTimeField(default=now, editable=False)
    Information =models.CharField(max_length=256)
    photo=models.FileField(blank=True,upload_to='Notifications/')
    Action_required = models.CharField(max_length=256)
    Raised_by=models.CharField(max_length=256)
    status_choices =(("open", "open"),("closed","closed"))
    Status=models.CharField(max_length=256,choices = status_choices,default ="open",null=True,blank=True )
    Remarks = models.CharField(max_length=256,blank=True)
    def get_absolute_url(self):
        return reverse("home")
