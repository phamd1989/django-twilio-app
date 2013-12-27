from django.db import models

class Status(models.Model):
    msid = models.CharField(max_length=40, unique=True)
    phone_number = models.CharField(max_length=20)
    accsid = models.CharField(max_length=40)
    from_number = models.CharField(max_length=20)
    to_number = models.CharField(max_length=20)
    message = models.CharField(max_length=300)
    
class Subscrption(models.Model):
    phone_number = models.CharField(primary_key=True, max_length=20)
    is_subscribed = models.BooleanField(default=False)
