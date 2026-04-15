from faker import Faker


fake = Faker(locale='ru_RU')

a_name = fake.name()
a_adress = fake.address()
a_tel = fake.phone_number()

print(f'\n{a_name}, \n{a_adress}, \n{a_tel}')
