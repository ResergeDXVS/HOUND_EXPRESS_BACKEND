from django.db import models

PACKAGE_STATUS_CHOICES = (
    ("pending","PENDING"),
    ("intransit","INTRANSIT"),
    ("delivered","DELIVERED"),
)

class Package(models.Model):
    guide_number = models.CharField(max_length=10, unique=True)
    origin = models.CharField(max_length=400)
    destination = models.CharField(max_length=400)
    recipient = models.CharField(max_length=400)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,default="PENDING",choices=PACKAGE_STATUS_CHOICES)

    def __str__(self):
        return self.guide_number