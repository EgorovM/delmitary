from rest_framework import viewsets

from couriers import models as courier_models
from couriers import serializers as courier_serializers
from couriers.filters import CourierFilter
from helpers.drf import GenericSerializerClass


class CourierViewSet(viewsets.ModelViewSet, GenericSerializerClass):
    queryset = courier_models.Courier.objects.all()
    serializer_class = courier_serializers.CourierSerializer
    retrieve_serializer_class = courier_serializers.CourierSerializerWithShifts
    filter_class = CourierFilter


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = courier_models.Shift.objects.all()
    serializer_class = courier_serializers.ShiftSerializer
