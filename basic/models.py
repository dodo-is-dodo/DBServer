from django.db import models, migrations
# from django.contrib.auth.models import User
from django.contrib.postgres import fields
# from picklefield.fields import PickledObjectField

# class MyUser(models.Model):
#     # user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     created = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(max_length=20, blank=False)
#     uid = models.CharField(max_length=20, blank=False)
#     pwd = models.CharField(max_length=20, blank=False)
#     # longtitude = models.DecimalField(max_digits=8, decimal_places=3)
#     # latitude = models.DecimalField(max_digits=8, decimal_places=3)
#     purchase_history = fields.JSONField()
#     basket = fields.JSONField()

class Store(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    lon = models.DecimalField(max_digits=8, decimal_places=3)
    inventory = fields.JSONField()

    class Meta:
        ordering = ('sid',)


# class Product(models.Model):
#     foreignKey
#     name = models.CharField(max_length=20, blank=False)
#     price = models.DecimalField()
#     stock = models.DecimalField()
