from rest_framework import viewsets

from customers import models as customer_models
from customers import serializers as customer_serializers
from helpers.drf import GenericSerializerClass


class CustomerViewSet(viewsets.ModelViewSet, GenericSerializerClass):
    queryset = customer_models.Customer.objects.all()
    serializer_class = customer_serializers.CustomerSerializer
