from django.contrib.auth.models import User
from django.db import models


class Shift(models.Model):
    """
    Рабочая смена курьеров, определяется:
    * week_parity - четная/нечетная учебная неделя
    * week_day - число от 0 до 6 - от понедельника до воскресенья
    * start - начало рабочей смены
    * end - конец рабочей смены
    * is_enabled - работает ли в указанную смену
    """

    WEEK_PARITY = (("even", "Четный"), ("odd", "Нечетный"))

    courier = models.ForeignKey(
        "Courier", on_delete=models.CASCADE, related_name="shifts"
    )

    week_parity = models.CharField(
        max_length=4,
        choices=WEEK_PARITY,
    )
    week_day = models.IntegerField()
    start = models.TimeField()
    end = models.TimeField()

    is_enabled = models.BooleanField(default=True)


class Courier(models.Model):
    """
    Сущеность курьера
    * dormitory - общежитие
    * room_number - номер комнаты
    * vehicle - способ передвижения
    * telephone - телефонный номер
    """

    VEHICLE = (
        ("CAR", "Машина"),
        ("BIKE", "Велосипед"),
        ("WALK", "Пешком"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dormitory = models.ForeignKey("shop.Dormitory", on_delete=models.CASCADE)

    room_number = models.IntegerField()
    vehicle = models.CharField(max_length=4, choices=VEHICLE)
    telephone = models.CharField(max_length=20)
