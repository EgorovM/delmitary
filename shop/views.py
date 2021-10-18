from rest_framework import viewsets

from helpers.drf import GenericSerializerClass
from shop.filter import ShopFilter
from shop.models import City, Dormitory, Good, Shop
from shop.serializers import (
    CitySerializer,
    CompactShopSerializer,
    DormitorySerializer,
    GoodSerializer,
    ShopSerializer,
)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class DormitoryViewSet(viewsets.ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer


class ShopViewSet(viewsets.ModelViewSet, GenericSerializerClass):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    list_serializer_class = CompactShopSerializer
    filterset_class = ShopFilter


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
