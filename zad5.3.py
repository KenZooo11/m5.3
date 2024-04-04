import random
from faker import Faker

class BusinessCard:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.email}"
    
    @property
    def full_name_length(self):
        return len(self.first_name) + len(self.last_name)

class BaseContact(BusinessCard):
    def __init__(self, first_name, last_name, email, base_phone):
        super().__init__(first_name, last_name, None, None, email)
        self.base_phone = base_phone
        
    def contact(self):
        print(f"Wybieram numer prywatny +48 {self.base_phone} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return super().full_name_length

class BusinessContact(BusinessCard):
    def __init__(self, first_name, last_name, email, position, company, business_phone):
        super().__init__(first_name, last_name, company, position, email)
        self.business_phone = business_phone
        
    def contact(self):
        print(f"Wybieram numer służbowy +48 {self.business_phone} i dzwonię do {self.first_name} {self.last_name}")
   
    @property
    def label_length(self):
        return super().full_name_length

business_cards = []

fake = Faker()

def create_contacts():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    contact_type = random.choice([BaseContact, BusinessContact])
    base_phone = str(random.randint(100000000, 999999999)).zfill(9)
    if contact_type == BusinessContact:
        position = fake.job()
        company = fake.company()
        business_phone = str(random.randint(100000000, 999999999)).zfill(9)
        return contact_type(first_name, last_name, email, position, company, business_phone)
    else:
        return contact_type(first_name, last_name, email, base_phone)

for _ in range(1):
    contact = create_contacts()
    business_cards.append(contact)

business_cards[0].contact()

for card in business_cards:
    print(f"\nDługość imienia i nazwiska dla {card.first_name} {card.last_name}: {card.label_length}")

random_card = create_contacts()
print(f"\nImię: {random_card.first_name}")
print(f"Nazwisko: {random_card.last_name}")
print(f"Firma: {random_card.company}")
print(f"Stanowisko: {random_card.position}")
print(f"Email: {random_card.email}")
