from rest_framework import serializers
from .models import ShortURL

# Serializer do tworzenia skróconych URLi
class ShortenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['original_url']


# Serializer do wyświetlania informacji o skrócie
class ExpandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['original_url', 'code', 'created_at']