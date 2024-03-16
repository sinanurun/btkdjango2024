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

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.keywords = validated_data.get('keywords', instance.keywords)
        instance.price = validated_data.get('price', instance.price)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.detail = validated_data.get('detail', instance.detail)
        instance.save()
        return instance