from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    price = serializers.IntegerField(read_only=True)
    quantity = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    category = serializers.CharField()