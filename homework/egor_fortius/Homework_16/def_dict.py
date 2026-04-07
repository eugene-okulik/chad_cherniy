import collections


with open('shops.txt') as shops_file:
    shops = list(map(lambda x: x.replace('\n', ''), shops_file.readlines()))

city_shops = collections.defaultdict(list)
for line in shops:
    shop, city = line.split(':')
    city_shops[city].append(shop)

print(city_shops)
