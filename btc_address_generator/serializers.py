from rest_framework import serializers

class BitcoinAddressGeneratorSerializer(serializers.Serializer):
    userId = serializers.CharField(required=True)
