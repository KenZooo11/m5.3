import random

class BusinessCard:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.email}"

business_cards = []

for _ in range(5):
    first_name = random.choice(["John", "Emma", "Michael", "Emily", "Daniel"])
    last_name = random.choice(["Smith", "Johnson", "Williams", "Brown", "Jones"])
    company = random.choice(["ABC Corp", "XYZ Company", "Tech Solutions", "Global Industries", "Innovative Ventures"])
    position = random.choice(["Manager", "Director", "CEO", "CFO", "CTO"])
    email = f"{first_name.lower()}.{last_name.lower()}@{company.replace(' ', '').lower()}.com"
    business_cards.append(BusinessCard(first_name, last_name, company, position, email))

print("Przed sortowaniem:")
for card in business_cards:
    print(card)

print("\nPo sortowaniu według imienia:")
sorted_by_first_name = sorted(business_cards, key=lambda x: x.first_name)
for card in sorted_by_first_name:
    print(card)

print("\nPo sortowaniu według nazwiska:")
sorted_by_last_name = sorted(business_cards, key=lambda x: x.last_name)
for card in sorted_by_last_name:
    print(card)

print("\nPo sortowaniu według adresu e-mail:")
sorted_by_email = sorted(business_cards, key=lambda x: x.email)
for card in sorted_by_email:
    print(card)

from faker import Faker

fake = Faker()

def generate_random_business_card():
    first_name = fake.first_name()
    last_name = fake.last_name()
    company = fake.company()
    position = fake.job()
    email = fake.email()
    return BusinessCard(first_name, last_name, company, position, email)

random_card = generate_random_business_card()
print(f"\nImię: {random_card.first_name}")
print(f"Nazwisko: {random_card.last_name}")
print(f"Firma: {random_card.company}")
print(f"Stanowisko: {random_card.position}")
print(f"Email: {random_card.email}")