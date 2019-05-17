from django.shortcuts import render
from .models import Category, Product, PriceTracker, Shop
from .serializers import CategorySerializer, ProductSerializer, PriceTrackerSerializer, ShopSerializer
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

# Create your views here.


class CategoryView(APIView):
    def get(self, request):
        '''
        returns all product categories
        '''

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProductsView(APIView):
    def get(self, request):
        '''
        returns all products 
        '''

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class PriceTrackerView(APIView):
    def get(self, request):
        '''
        returns pricetracker
        '''
        price_tracker = PriceTracker.objects.all()
        serializer = PriceTrackerSerializer(price_tracker, many=True)
        return Response(serializer.data)


class ShopView(APIView):
    def get(self, request):
        '''
        returns all shops
        '''
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)
