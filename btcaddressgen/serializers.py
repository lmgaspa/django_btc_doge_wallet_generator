# myapp/serializers.py
from rest_framework import serializers

class ExampleSerializer(serializers.Serializer):
    text = serializers.CharField()
