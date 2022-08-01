from rest_framework import serializers
from .models import CardProduct


class CardProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CardProduct
        fields = ('__all__')
