from django.db import models

PACKAGE_STATUS_CHOICES = (
    ("pending","PENDING"),
    ("intransit","INTRANSIT"),
    ("delivered","DELIVERED"),
)

class Package(models.Model):
    id_guide = models.CharField(max_length=10, unique=True)
    origin = models.CharField(max_length=400)
    destiny = models.CharField(max_length=400)
    recipient = models.CharField(max_length=400)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,default="PENDING",choices=PACKAGE_STATUS_CHOICES)

    def __str__(self):
        return self.id_guide


    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_status = Package.objects.get(pk=self.pk).status
            except Package.DoesNotExist:
                old_status = None

            if old_status != self.status:
                HistoricalPackage.objects.create(
                    guide=self,
                    new_status=self.status
                )
        else:
            super().save(*args, **kwargs)
            HistoricalPackage.objects.create(
                guide=self,
                new_status=self.status
            )
            return 

        super().save(*args, **kwargs)


class HistoricalPackage(models.Model):
    guide = models.ForeignKey(Package, on_delete=models.CASCADE)
    new_status = models.CharField(max_length=20,default="PENDING",choices=PACKAGE_STATUS_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
