from rest_framework import serializers

class DogecoinAddressGeneratorSerializer(serializers.Serializer):
    userId = serializers.CharField(required=True)
