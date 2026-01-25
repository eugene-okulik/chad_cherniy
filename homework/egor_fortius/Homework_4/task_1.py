my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [6, 7, 8, 9, 10],
    'dict': {
        'first': 'Terizla',
        'second': 'Mia',
        'third': 'Leyla',
        'fourth': 'Grok',
        'fifth': 'Tigril'
    },
    'set': {'white', 'black', 'red', 'green', 'yellow'}
}

# 1
print(my_dict['tuple'][-1])

# 2
my_dict['list'].append(11)
del my_dict['list'][1]

# 3
my_dict[('i am a tuple',)] = (11, 12, 13, 14, 15)
del my_dict['list']

# 4
my_dict['set'].add('ulun')
my_dict['set'].remove('red')

for key, value in my_dict.items():
    print(f"{key}: {value}")
