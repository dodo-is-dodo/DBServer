from django.shortcuts import render
# from basic.serializers import UserSerializer, StoreSerializer, Query_param, ReturnSerializer
from basic.serializers import SearchSerializer, ResultSerializer
from basic.models import Store
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# class StoreList(generics.ListAPIView):
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer

# class UserList(generics.ListAPIView):
#     queryset = MyUser.objects.all()
#     print("nyan?")
#     serializer_class = UserSerializer

# class UserSearch(APIView):
#     def get(self, request, pk, format=None):
#         queryset = MyUser.objects.get(uid=pk)
#         serializer = UserSerializer(queryset)
#         print(queryset)
#         print(serializer)
#         print(type(serializer))
#         return Response(serializer.data)
def transform(name):
    p = ["코카콜라", "미에로 화이바", "핫식스", "새우깡", "누드 빼빼로"]
    for i in range(len(p)):
        if name == p[i]:
            return i
    return 5

class SearchAPI(APIView):
    def get(self, request, format=None):
        serializer = SearchSerializer(data=request.data)
        print("suck")
        if serializer.is_valid():
            # print(serializer.data)
            items = serializer.data["item"]
            # print(items)
            store_list = []
            stores = Store.objects.all()
            # print("stores",stores)
            for store in stores:
                # print(store)
                total = 0
                product_list = []
                for item in items:
                    # print(item)
                    name = item["pid"]
                    print(name)
                    pid = transform(name)
                    price = store.inventory[name]
                    volume = item["volume"]
                    total += price * volume
                    product_list.append(Product(name, pid, price))
                name = store.name
                lat = store.lat
                lon = store.lon
                store_list.append(StoreObj(name, total, lat, lon, product_list))
            result = Result(store_list)
            ret = ResultSerializer(result)
            return Response(ret.data, status=status.HTTP_200_OK)
            # p1 = Product("듀렉스", 1, 5000)
            # p2 = Product("유니더스", 2, 2000)
            # p3 = Product("오카모토", 3, 3500)
            # product_list = [p1, p2, p3]
            # s1 = Store("CU", 130.5, 42.66, product_list)
            # s2 = Store("GS25", 130.5, 42.66, product_list[:2])
            # result = Result(store_list)
            # ret = ResultSerializer(result)
            # return Response(ret.data, status=status.HTTP_200_OK)
        print("fuck")
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = SearchSerializer(data=request.data)
        print("suck")
        if serializer.is_valid():
            # print(serializer.data)
            items = serializer.data["item"]
            # print(items)
            store_list = []
            stores = Store.objects.all()
            # print("stores",stores)
            for store in stores:
                # print(store)
                total = 0
                product_list = []
                for item in items:
                    # print(item)
                    name = item["pid"]
                    print(name)
                    pid = transform(name)
                    price = store.inventory[name]
                    volume = item["volume"]
                    total += price * volume
                    product_list.append(Product(name, pid, price))
                name = store.name
                lat = store.lat
                lon = store.lon
                store_list.append(StoreObj(name, total, lat, lon, product_list))
            result = Result(store_list)
            ret = ResultSerializer(result)
            return Response(ret.data, status=status.HTTP_200_OK)
            # p1 = Product("듀렉스", 1, 5000)
            # p2 = Product("유니더스", 2, 2000)
            # p3 = Product("오카모토", 3, 3500)
            # product_list = [p1, p2, p3]
            # s1 = Store("CU", 130.5, 42.66, product_list)
            # s2 = Store("GS25", 130.5, 42.66, product_list[:2])
            # result = Result(store_list)
            # ret = ResultSerializer(result)
            # return Response(ret.data, status=status.HTTP_200_OK)
        print("fuck")
        return Response(None, status=status.HTTP_400_BAD_REQUEST)


    # def get(self, request, format=None):
    #     serializer = Query_param(data=request.data)
    #     if serializer.is_valid():
    #         # print(serializer.data)
    #         products = serializer.data["products"]
    #         s_list = []
    #         for store in serializer.data["store"]:
    #             sid = store["sid"]
    #             p_list = []
    #             # print(sid)
    #             try:
    #                 store = Store.objects.get(sid=sid)
    #             except:
    #                 return Response(None, status=status.HTTP_404_NOT_FOUND)
    #             # print(store)
    #             for p in products:
    #                 # print(p)
    #                 # print(p['pid'])
    #                 try:
    #                     price = int(store.inventory[p['pid']])
    #                 except:
    #                     return Response(None, status=status.HTTP_404_NOT_FOUND)
    #                 # print(price)
    #                 p_list.append(
    #                     StorePrice(p["pid"], price))
    #             s_list.append(Stores(sid, p_list))
    #         ret = Ret(s_list)
    #         retSerializer = ReturnSerializer(ret)
    #         print(retSerializer.data)
    #         return Response(retSerializer.data)
    #     print("fail")
    #     return Response(None, status=status.HTTP_400_BAD_REQUEST)
    # def post(self, request, format=None):
    #     serializer = Query_param(data=request.data)
    #     if serializer.is_valid():
    #         # print(serializer.data)
    #         products = serializer.data["products"]
    #         s_list = []
    #         for store in serializer.data["store"]:
    #             sid = store["sid"]
    #             p_list = []
    #             # print(sid)
    #             try:
    #                 store = Store.objects.get(sid=sid)
    #             except:
    #                 return Response(None, status=status.HTTP_404_NOT_FOUND)
    #             # print(store)
    #             for p in products:
    #                 # print(p)
    #                 # print(p['pid'])
    #                 try:
    #                     price = int(store.inventory[p['pid']])
    #                 except:
    #                     return Response(None, status=status.HTTP_404_NOT_FOUND)
    #                 # print(price)
    #                 p_list.append(
    #                     StorePrice(p["pid"], price))
    #             s_list.append(Stores(sid, p_list))
    #         ret = Ret(s_list)
    #         retSerializer = ReturnSerializer(ret)
    #         print(retSerializer.data)
    #         return Response(retSerializer.data)
    #     print("fail")
    #     return Response(None, status=status.HTTP_400_BAD_REQUEST)





        # p1 = StorePrice("cocacola", 1200)
        # p2 = StorePrice("condom", 2000)
        # p3 = StorePrice("girl", 200000)
        # s1 = Stores(1, [p1, p2])
        # s2 = Stores(2, [p1, p2, p3])
        # ret = Ret([s1, s2])
        # serializer = ReturnSerializer(ret)
        # return Response(serializer.data)
    # def get(self, request, format=None):
    #     j = Fuck(5, 10)
    #     j1 = Fuck(5, 10)
    #     j2 = Fuck(5, 10)
    #     obj = KKK(3, 4, [j, j1, j2])
    #     serializer = Query_param(obj)
    #     return Response(serializer.data)
    # def post(self, request, format=None):
    #     print(type(request.data))
    #     serializer = Query_param(data=request.data)
    #     if serializer.is_valid():
    #         print(serializer.data)
    #         # serializer.save()
    #         print(serializer.data["product"][0])
    #         print("fuck")
    #         return Response(serializer.data)
    #     print("suck")
    #     return Response(None)

class Item:
    def __init__(self, pid, volume):
        self.pid = pid
        self.volume = volume

class Search:
    def __init__(self, item):
        self.item = item

class Product:
    def __init__(self, name, pid, price):
        self.name = name
        self.pid = pid
        self.price = price


class StoreObj:
    def __init__(self, name, total, lat, lon, product):
        self.name = name
        self.total = total
        self.lat = lat
        self.lon = lon
        self.product = product

class Result:
    def __init__(self, store):
        self.store = store
# class KKK:
#     def __init__(self, uid, sid, product):
#         self.uid = uid
#         self.sid = sid
#         self.products = product

# class Fuck:
#     def __init__(self, pid, volume):
#         self.pid = pid
#         self.volume = volume

# class Ret:
#     def __init__(self, stores):
#         self.stores = stores

# class Stores:
#     def __init__(self, sid, detail):
#         self.sid = sid
#         self.detail = detail

# class StorePrice:
#     def __init__(self, pid, price):
#         self.pid = pid
#         self.price = price

