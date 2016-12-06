from basic.models import Store
import csv
from random import randint


p = ["코카콜라", "미에로 화이바", "핫식스", "새우깡", "누드 빼빼로"]

with open("data", "r") as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in rows:
        # print(row)
        # print(i, row[0], row[1], row[2], p[0], int(randint(800, 1300) / 100) * 100)
        Store.objects.create(sid=i, name=row[0],
                             lat=float(row[1]),
                             lon=float(row[2]),
                             inventory={
                                 p[0] : int(randint(800, 1300) / 100) * 100,
                                 p[1] : int(randint(500, 1000) / 100) * 100,
                                 p[2] : int(randint(900, 1500) / 100) * 100,
                                 p[3] : int(randint(1200, 2000) / 100) * 100,
                                 p[4] : int(randint(1300, 2200) / 100) * 100})
        i+=1

# dodo = MyUser.objects.create(
#     name="dodo", uid="dodo", pwd="1234",
#     purchase_history=[{'time':str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
#                        "product" : [
#                            {"pid" : "cocacola", "price" : 2000, "volume" : 3}, {"pid" : "condom", "price" : 1000, "volume" : 5}]}],
#     basket=[{'time':datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                        "product" : [
#                            {"pid" : "cocacola", "volume" : 3}, {"pid" : "condom", "volume" : 5}]}])

# a= Store.objects.create(sid=10, name="fuckYou", longtitude=126.98, latitude=37.476, inventory={'condom': 3000, 'cocacola':2000, 'mac':30000000})
# a= Store.objects.create(sid=11, name="fuckYou", longtitude=126.98, latitude=37.476, inventory={'condom': 2000, 'cocacola':1000, 'mac':300000})

# a= Store.objects.create(sid=5, name="MiniStop",
#                         inventory={"코카콜라" : 1000,
#                                    "미에로화이바" : 600,
#                                    "핫식스" : 2000,
#                                    "새우깡" : 1300,
#                                    "빼빼로" : 3000})
