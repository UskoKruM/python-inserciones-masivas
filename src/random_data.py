from faker import Faker

fake = Faker()

data = []

for _ in range(100):
    data.append((fake.uuid4(), fake.name(), fake.company(), fake.job(),
                 fake.email(), fake.phone_number(), fake.mac_address()))
