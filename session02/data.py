from faker import Faker

fake = Faker()

def get_new_user():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "year_of_birth": fake.year()
    }