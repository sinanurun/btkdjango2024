from rest_framework import serializers

from product.models import Product


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     price = serializers.IntegerField(read_only=True)
#     quantity = serializers.IntegerField(read_only=True)
#     description = serializers.CharField()
#     category = serializers.CharField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'