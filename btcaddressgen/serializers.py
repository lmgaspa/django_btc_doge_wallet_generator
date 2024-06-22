from rest_framework import serializers

class BtcAddressGenSerializer(serializers.Serializer):
    userId = serializers.CharField(required=True)
