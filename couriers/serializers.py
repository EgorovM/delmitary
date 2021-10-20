from rest_framework import serializers
from rest_framework.validators import ValidationError

from couriers import models as courier_models


class ShiftSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        # проверяем, имеет ли пересечение с ранее созданными интервалами
        shifts = courier_models.Shift.objects.filter(
            courier=attrs["courier"],
            week_day=attrs["week_day"],
            week_parity=attrs["week_parity"],
        ).order_by("start")

        for shift in shifts:
            if attrs["end"] > shift.start and attrs["start"] < shift.end:
                raise ValidationError(
                    "Имеется пересечение с существующим графиком в этот же день "
                    f"id: {shift.id}, начало: {shift.start}, конец: {shift.end}"
                )

        return attrs

    class Meta:
        model = courier_models.Shift
        fields = "__all__"


class CourierSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)

    class Meta:
        model = courier_models.Courier
        fields = (
            "id",
            "user",
            "first_name",
            "last_name",
            "room_number",
            "vehicle",
            "telephone",
        )


class CourierSerializerWithShifts(CourierSerializer):
    shifts = serializers.SerializerMethodField()

    class Meta:
        model = courier_models.Courier
        fields = CourierSerializer.Meta.fields + ("shifts",)

    def get_shifts(self, obj):
        return ShiftSerializer(obj.shifts.all(), many=True).data
