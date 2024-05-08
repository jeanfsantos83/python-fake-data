# pip install faker #
from faker import Faker

# Initialize the lib #
fake = Faker()

# Create variables with fake data #
name = fake.name()
first_name_fem = fake.first_name_female()
user = fake.user_name()
password = fake.password()
month = fake.month()

print(f'Name: {name}')
print(f'Name Female: {first_name_fem}')
print(f'User: {user}')
print(f'Password: {password}')
print(f'Month: {month}')
