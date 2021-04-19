from rest_framework import serializers

from .models import Category, Product

# to convert objects into bytes/data
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = (
      'id',
      'name',
      'get_absolute_url',
      'description',
      'price',
      'get_image',
      'get_thumbnail',
    )