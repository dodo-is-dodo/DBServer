from rest_framework import serializers
from basic.models import Store
# from rest_framework_hstore.serializers import HStoreSerializer
# from rest_framework_hstore.serializers import HStoreSerializer

# class StoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         fields = ('sid', 'name', 'latitude', 'longtitude','inventory')

class ItemSerializer(serializers.Serializer):
    pid = serializers.CharField()
    volume = serializers.IntegerField()

class SearchSerializer(serializers.Serializer):
    item = ItemSerializer(many=True)


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    pid = serializers.IntegerField()
    price = serializers.IntegerField()

class StoreSerializer(serializers.Serializer):
    name = serializers.CharField()
    total = serializers.IntegerField()
    lat = serializers.FloatField()
    lon = serializers.FloatField()
    product = ProductSerializer(many=True)


class ResultSerializer(serializers.Serializer):
    store = StoreSerializer(many=True)


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyUser
#         fields = ('created', 'name', 'uid', 'purchase_history', "basket")



# class StoresSerializer(serializers.Serializer):
#     sid = serializers.IntegerField()


# class Query_param(serializers.Serializer):
#     uid = serializers.IntegerField()
#     store = StoresSerializer(many=True)
#     products = ProductSerializer(many=True)


# class StorePriceSerializer(serializers.Serializer):
#     pid = serializers.CharField()
#     price = serializers.IntegerField()


# class StoreListSerializer(serializers.Serializer):
#     sid = serializers.IntegerField()
#     detail = StorePriceSerializer(many=True)


# class ReturnSerializer(serializers.Serializer):
#     stores = StoreListSerializer(many=True)

