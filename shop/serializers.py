from rest_framework import serializers

from shop.models import City, Dormitory, Good, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name",)


class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormitory
        fields = ("name", "address")


class CompactShopSerializer(serializers.ModelSerializer):
    prices_from = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ("name", "address", "nearest_dormitory", "prices_from")

    def get_prices_from(self, obj):
        return min(good.price for good in obj.goods.all())


class ShopSerializer(CompactShopSerializer):
    class Meta:
        model = Shop
        fields = CompactShopSerializer.Meta.fields + (
            "walk_time",
            "bike_time",
        )


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ("shop", "name", "description", "icon", "price")
