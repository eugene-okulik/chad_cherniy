PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = [x.rstrip('р') if "р" in x else x for x in PRICE_LIST.strip().split()]
price_dict = {new_list[i]: int(new_list[i + 1]) for i in range(0, len(new_list), 2)}
print(price_dict)
