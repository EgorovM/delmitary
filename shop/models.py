from django.db import models


class City(models.Model):
    name = models.CharField(max_length=120)


class Dormitory(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)


class Shop(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    nearest_dormitory = models.ForeignKey("Dormitory", on_delete=models.CASCADE)
    walk_time = models.TimeField()
    bike_time = models.TimeField()


class Good(models.Model):
    shop = models.ForeignKey("Shop", on_delete=models.CASCADE, related_name="goods")
    name = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.ImageField(upload_to="goods/", default="goods/default.png")
    price = models.IntegerField()
