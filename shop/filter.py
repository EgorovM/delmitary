from django_filters import rest_framework as filters

from shop.models import Shop


class ShopFilter(filters.FilterSet):
    class Meta:
        model = Shop
        fields = "__all__"
