from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from product.models import Product
from projectapi.serializers import ProductSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
# Create your views here.
def index(request):
    # adım1
    # products = Product.objects.all()
    # print(products)
    # products_list = list(products.values())
    # print(products_list)
    # return JsonResponse({'products': products_list})
    # adım 2
    # products = Product.objects.all()
    # serializer = ProductSerializer(products, many=True)
    # return JsonResponse(serializer.data, safe=False)
    # adım3
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
