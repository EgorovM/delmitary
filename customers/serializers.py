from rest_framework import serializers

from customers import models as customer_models


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer_models.Customer
        fields = "__all__"
