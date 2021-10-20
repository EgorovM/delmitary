import datetime

from django_filters import rest_framework as filters

from couriers import models as courier_models
from helpers.study import get_current_week_parity


class CourierFilter(filters.FilterSet):
    """
    Фильтр для курьеров

    * is_working - работает ли в текущее время
    """

    is_working = filters.BooleanFilter(method="filter_is_working")

    class Meta:
        model = courier_models.Courier
        fields = {
            "user__username": ["exact"],
            "room_number": ["exact"],
            "dormitory": ["exact"],
            "vehicle": ["exact"],
        }

    def filter_is_working(self, request, queryset, value):
        if not value:
            return queryset

        current_time = datetime.datetime.now().time()
        current_week_parity = get_current_week_parity()

        possible_couriers = courier_models.Courier.objects.prefetch_related(
            "shifts"
        ).filter(
            shifts__is_enabled=True,
            shifts__start__lte=current_time,
            shifts__end__gte=current_time,
            shifts__week_parity=current_week_parity,
        )

        return possible_couriers
