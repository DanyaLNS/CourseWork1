from rest_framework import serializers


class ReaderSerializer(serializers.Serializer):
    path = serializers.CharField(max_length=300)
    result = serializers.CharField(max_length=50)