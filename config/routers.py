from rest_framework import routers

from couriers import views as couriers_views
from customers import views as customer_views
from shop import views as shop_views

router = routers.SimpleRouter()

router.register(r"city", shop_views.CityViewSet, basename="city")
router.register(r"dormitory", shop_views.DormitoryViewSet, basename="dormitory")
router.register(r"shop", shop_views.ShopViewSet, basename="shop")
router.register(r"good", shop_views.GoodViewSet, basename="good")
router.register(r"order", shop_views.OrderViewSet, basename="order")

router.register(r"courier", couriers_views.CourierViewSet, basename="courier")
router.register(r"courier-shift", couriers_views.ShiftViewSet, basename="courier-shift")

router.register(r"customer", customer_views.CustomerViewSet, basename="customer")
