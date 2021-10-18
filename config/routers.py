from rest_framework import routers

from shop.views import CityViewSet, DormitoryViewSet, GoodViewSet, ShopViewSet

router = routers.SimpleRouter()
router.register(r"city", CityViewSet, basename="city")
router.register(r"dormitory", DormitoryViewSet, basename="dormitory")
router.register(r"shop", ShopViewSet, basename="shop")
router.register(r"good", GoodViewSet, basename="good")
