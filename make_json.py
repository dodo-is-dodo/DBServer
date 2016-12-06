import json

# data = {"uid" : 3, "sid" : 4,
#         "product" : [{"pid" : 5, "volume" : 5}, {"pid" : 6, "volume" : 7}]}
# data = {"uid" : 3, "store" : [{"sid" : 10}, {"sid" : 11}],
        # "product" : [{"pid" : 'cocacola', "volume" : 5}, {"pid" : 'mac', "volume" : 7}]}

# data = {"uid" : 3, "store" : [{"sid" : 1}, {"sid" : 2}],
#         "products" : [{"pid" : '코카콜라', "volume" : 5}, {"pid" : '미에로화이바', "volume" : 7}]}

data = {"item" : [{"pid" : "누드 빼빼로", "volume" : 5},
                  {"pid" : "코카콜라", "volume" : 2}]}

with open('ex.json', 'w') as outfile:
    json.dump(data, outfile)
