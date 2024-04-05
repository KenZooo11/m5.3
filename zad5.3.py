import random
from faker import Faker

class BaseContact:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
    
    def contact(self):
        print(f"Wybieram numer prywatny +48 {self.phone_number} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)

class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, email, phone_number, position, company, business_phone):
        super().__init__(first_name, last_name, email, phone_number)
        self.position = position
        self.company = company
        self.business_phone = business_phone
        
    def contact(self):
        print(f"Wybieram numer służbowy +48 {self.business_phone} i dzwonię do {self.first_name} {self.last_name}")
   
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)

business_cards = []

fake = Faker()

def create_contacts():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone_number = str(random.randint(100000000, 999999999)).zfill(9)
    contact_type = random.choice([BaseContact, BusinessContact])
    
    if contact_type == BusinessContact:
        position = fake.job()
        company = fake.company()
        business_phone = str(random.randint(100000000, 999999999)).zfill(9)
        return contact_type(first_name, last_name, email, phone_number, position, company, business_phone)
    else:
        return contact_type(first_name, last_name, email, phone_number)

for _ in range(1):
    contact = create_contacts()
    business_cards.append(contact)

business_cards[0].contact()

for card in business_cards:
    print(f"\nDługość imienia i nazwiska dla {card.first_name} {card.last_name}: {card.label_length}")

random_card = create_contacts()
print(f"\nImię: {random_card.first_name}")
print(f"Nazwisko: {random_card.last_name}")
if isinstance(random_card, BusinessContact):
    print(f"Firma: {random_card.company}")
    print(f"Stanowisko: {random_card.position}")
print(f"Email: {random_card.email}")
