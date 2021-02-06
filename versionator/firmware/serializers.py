from rest_framework import serializers
from .models import Firmmware


class FirmmwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firmmware
        fields = ('id', 'project_name', 'version', 'compatible_card_name', 'file')
