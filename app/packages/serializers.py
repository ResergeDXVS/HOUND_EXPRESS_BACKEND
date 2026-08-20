from rest_framework import serializers
from packages.models import Package, HistoricalPackage
class PackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            "id",
            "id_guide",
            "origin",
            "destiny",
            "recipient",
            "status",
            "datetime_created",
            "datetime_updated"
        ]
        read_only_fields = ["id", "datetime_created", "datetime_updated"]

class HistoricalSerializers(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPackage
        fields = [
            "guide",
            "new_status",
            "datetime_created"
        ]
        read_only_fields = ["guide","new_status","datetime_created"]