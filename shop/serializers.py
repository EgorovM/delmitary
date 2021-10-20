from rest_framework import serializers

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
    prices_from = serializers.SerializerMethodField()

    class Meta:
        model = shop_models.Shop
        fields = ("id", "name", "address", "nearest_dormitory", "prices_from")

    def get_prices_from(self, obj):
        return min(good.price for good in obj.goods.all())


class ShopSerializer(CompactShopSerializer):
    class Meta:
        model = shop_models.Shop
        fields = CompactShopSerializer.Meta.fields + (
            "walk_time",
            "bike_time",
        )


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Good
        fields = ("id", "shop", "name", "description", "icon", "price")


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Order
        fields = ("courier", "has_completed", "completed_time")


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Order
        fields = ("shop", "customer", "goods")


class OrderSerializer(CreateOrderSerializer):
    class Meta:
        model = shop_models.Order
        fields = CreateOrderSerializer.Meta.fields + (
            "id",
            "total_price",
            "has_completed",
            "completed_time",
        )
