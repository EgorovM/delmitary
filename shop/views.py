from rest_framework import viewsets

from helpers.drf import GenericSerializerClass
from shop import filters as shop_filters
from shop import serializers as shop_serializers
from shop.models import City, Dormitory, Good, Order, Shop


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = shop_serializers.CitySerializer


class DormitoryViewSet(viewsets.ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = shop_serializers.DormitorySerializer


class ShopViewSet(viewsets.ModelViewSet, GenericSerializerClass):
    queryset = Shop.objects.all()
    serializer_class = shop_serializers.ShopSerializer
    list_serializer_class = shop_serializers.CompactShopSerializer
    filter_class = shop_filters.ShopFilter


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = shop_serializers.GoodSerializer
    filter_class = shop_filters.GoodFilter


class OrderViewSet(viewsets.ModelViewSet, GenericSerializerClass):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = shop_serializers.OrderSerializer
    create_serializer_class = shop_serializers.CreateOrderSerializer
    filter_class = shop_filters.OrderFilter

    def perform_create(self, serializer):
        order_goods = serializer.validated_data["goods"]
        goods = [good['good'] for good in order_goods]
        total_price = sum([good.price for good in goods])
        serializer.save(total_price=total_price)
        super().perform_create(serializer)
