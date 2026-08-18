from rest_framework import serializers
from packages.models import Package

class PackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            "id",
            "guide_number",
            "origin",
            "destination",
            "recipient",
            "status",
            "datetime_created",
            "datetime_updated"
        ]
        read_only_fields = ["id", "datetime_created", "datetime_updated"]

    