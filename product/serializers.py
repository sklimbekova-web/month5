from rest_framework import serializers
from .models import Category, Product, Review



class ReviewSerializer(serializers.ModelSerializer):
  stars = serializers.IntegerField(min_value=1, max_value=5)

  class Meta:
    model = Review
    fields = '__all__'  



class ProductReviewsSerializer(serializers.ModelSerializer):
  reviews = ReviewSerializer(many=True, read_only=True)
  rating = serializers.FloatField(read_only=True)

  class Meta:
    model = Product
    fields = [
        'id',
        'title',
        'description',
        'price',
        'category',
        'rating',
        'reviews',
    ]


class CategoryWithCountSerializer(serializers.ModelSerializer):
  products_count = serializers.IntegerField(read_only=True)

  class Meta:
    model = Category
    fields = ['id', 'name', 'products_count']


class CategorySerializer(serializers.ModelSerializer):
  name = serializers.CharField(min_length=2, max_length=100)

  class Meta:
    model = Category
    fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
  price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
  title = serializers.CharField(min_length=2, max_length=255)

  class Meta:
    model = Product
    fields = '__all__'