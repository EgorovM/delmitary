from django.db import models


class City(models.Model):
    """ Город """

    name = models.CharField(max_length=120)


class Dormitory(models.Model):
    """ Общежитие """

    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)


class Shop(models.Model):
    """
    Магазин
    * nearest_dormitory - ближайщий закрепленный магазин
    * walk_time - время пешком в минутах
    * bike_time - время пешком с помощью велосипеда
    """

    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    nearest_dormitory = models.ForeignKey("Dormitory", on_delete=models.CASCADE)
    walk_time = models.TimeField()
    bike_time = models.TimeField()


class Good(models.Model):
    """
    Товар в магазине
    * shop - магазин в котором товар продается
    """

    shop = models.ForeignKey("Shop", on_delete=models.CASCADE, related_name="goods")
    name = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.ImageField(upload_to="goods/", default="goods/default.png")
    price = models.IntegerField()


class Order(models.Model):
    """
    Сформированный заказ
    """

    shop = models.ForeignKey("Shop", on_delete=models.CASCADE)
    goods = models.ManyToManyField("Good")

    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    courier = models.ForeignKey("couriers.Courier", on_delete=models.CASCADE, null=True)

    has_completed = models.BooleanField(default=False)
    completed_time = models.DateTimeField(blank=True, null=True)

    # технические поля
    total_price = models.FloatField(default=0)
