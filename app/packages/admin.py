from django.contrib import admin

from .models import Package, HistoricalPackage

admin.site.register(Package)
admin.site.register(HistoricalPackage)