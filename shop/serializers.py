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
    mean_price = serializers.SerializerMethodField()

    class Meta:
        model = shop_models.Shop
        fields = ("id", "name", "address", "nearest_dormitory", "mean_price")

    def get_mean_price(self, obj):
        actual_prices = [good.price for good in obj.goods.all() if good.price != -1]

        return sum(actual_prices) // len(actual_prices)


class ShopSerializer(CompactShopSerializer):
    walk_time = serializers.SerializerMethodField()
    bike_time = serializers.SerializerMethodField()

    class Meta:
        model = shop_models.Shop
        fields = CompactShopSerializer.Meta.fields + (
            "walk_time",
            "bike_time",
        )

    def get_walk_time(self, obj):
        return obj.walk_time.minute
    
    def get_bike_time(self, obj):
        return obj.bike_time.minute

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
