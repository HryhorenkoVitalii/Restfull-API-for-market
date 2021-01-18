from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers
from api.models import Products, Orders


class ProductsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10000, decimal_places=2, required=False)
    discount = serializers.IntegerField(required=False, validators=[MinValueValidator(0),
                                                                    MaxValueValidator(100)])

    class Meta:
        model = Products
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(required=False)
    status = serializers.CharField(required=False)
    paid = serializers.BooleanField(required=False)

    class Meta:
        model = Orders
        fields = "__all__"


class BillsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10000, decimal_places=2)
    discount = serializers.CharField(max_length=100)
    amount_to_pay = serializers.DecimalField(max_digits=10000, decimal_places=2)
    date_order = serializers.DateTimeField()
    date_bill = serializers.DateTimeField()

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.price = validated_data.get("price", instance.price)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.amount_to_pay = validated_data.get("amount_to_pay", instance.amount_to_pay)
        instance.date_order = validated_data.get("date_order", instance.date_order)
        instance.date_bill = validated_data.get("date_bill", instance.date_bill)
        return instance


class StatisticSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    date_order = serializers.DateTimeField()
    product = ProductsSerializer(many=False, read_only=True)
    amount_to_pay = serializers.DecimalField(max_digits=10000, decimal_places=2)
    status = serializers.CharField(max_length=100)
    paid = serializers.BooleanField()
