from django_filters import rest_framework as filters

from shop import models as shop_models


class ShopFilter(filters.FilterSet):
    class Meta:
        model = shop_models.Shop
        fields = ["name", "address", "nearest_dormitory"]


class GoodFilter(filters.FilterSet):
    class Meta:
        model = shop_models.Good
        fields = ["shop"]


class OrderFilter(filters.FilterSet):
    total_price = filters.FilterSet

    class Meta:
        model = shop_models.Order
        fields = {
            "shop": ["exact"],
            "courier": ["exact"],
            "customer": ["exact"],
            "has_completed": ["exact"],
            "total_price": ["gte", "lte"],
            "completed_time": ["gte", "lte"],
        }
