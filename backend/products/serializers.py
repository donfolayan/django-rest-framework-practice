from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
            'discounted_price',
        ]

    def get_discounted_price(self, obj):
        if  not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
        