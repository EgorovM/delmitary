from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from shop import models as shop_models


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.City
        fields = (
            "id",
            "name",
        )


class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Dormitory
        fields = ("id", "name", "address")


class CompactShopSerializer(serializers.ModelSerializer):
    walk_time = serializers.SerializerMethodField()
    bike_time = serializers.SerializerMethodField()
    mean_price = serializers.SerializerMethodField()

    class Meta:
        model = shop_models.Shop
        fields = ("id", "name", "icon", "address", "nearest_dormitory", "mean_price", "walk_time", "bike_time")

    def get_mean_price(self, obj):
        actual_prices = [good.price for good in obj.goods.all() if good.price != -1]
        if not actual_prices:
            return "Нет товаров"

        return sum(actual_prices) // len(actual_prices)

    def get_walk_time(self, obj):
        return obj.walk_time.minute

    def get_bike_time(self, obj):
        return obj.bike_time.minute


class ShopSerializer(CompactShopSerializer):
    class Meta:
        model = shop_models.Shop
        fields = CompactShopSerializer.Meta.fields


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Good
        fields = ("id", "shop", "name", "description", "icon", "price")



class OrderGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.OrderGood
        fields = ("id", "good", "amount")


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Order
        fields = ("courier", "has_completed", "completed_time")


class CreateOrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    goods = OrderGoodSerializer(many=True)

    class Meta:
        model = shop_models.Order
        fields = ("shop", "customer", "goods", "delivery_price")

    def create(self, validated_data):
        goods = [
            shop_models.OrderGood.objects.create(
                **order_good_params
            ) 
            for order_good_params in validated_data.pop('goods')
        ]
        order = shop_models.Order.objects.create(**validated_data)
        order.goods.set(goods)
        return order


class OrderSerializer(CreateOrderSerializer):
    class Meta:
        model = shop_models.Order
        fields = CreateOrderSerializer.Meta.fields + (
            "id",
            "total_price",
            "has_completed",
            "completed_time",
        )
