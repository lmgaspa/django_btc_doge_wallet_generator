from rest_framework import serializers

class SolanaAddressGeneratorSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
