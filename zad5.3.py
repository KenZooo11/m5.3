import random
from faker import Faker

class PrywatnyKontakt:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self._label_length = len(first_name) + len(last_name)

    def contact(self):
        print(f"\nWybieram numer prywatny +48 {self.phone_number} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return self._label_length

    def __str__(self):
        return f"Imię: {self.first_name}\nNazwisko: {self.last_name}\nEmail: {self.email}\nNumer telefonu: {self.phone_number}"

class SluzbowyKontakt(PrywatnyKontakt):
    def __init__(self, position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        print(f"\nWybieram numer służbowy +48 {self.business_phone} i dzwonię do {self.first_name} {self.last_name}")

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nFirma: {self.company}\nStanowisko: {self.position}"

def create_contacts(rodzaj_wizytowki, ilosc):
    contacts = []
    fake = Faker()

    for _ in range(ilosc):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = str(random.randint(100000000, 999999999)).zfill(9)

        if rodzaj_wizytowki.lower() == "prywatnykontakt":
            contact = PrywatnyKontakt(first_name, last_name, email, phone_number)
        elif rodzaj_wizytowki.lower() == "sluzbowykontakt":
            position = fake.job()
            company = fake.company()
            business_phone = str(random.randint(100000000, 999999999)).zfill(9)
            contact = SluzbowyKontakt(position, company, business_phone, first_name, last_name, email, phone_number)
        else:
            raise ValueError("Nieprawidłowy rodzaj wizytówki")

        contacts.append(contact)

    return contacts

if __name__ == "__main__":
    rodzaj_wizytowki = input("Podaj rodzaj wizytówki (PrywatnyKontakt/SluzbowyKontakt): ").lower()
    ilosc = int(input("Podaj ilość wizytówek do utworzenia: "))

    contacts = create_contacts(rodzaj_wizytowki, ilosc)

    for contact in contacts:
        contact.contact()
        print("\nInformacje o kontakcie:")
        print(contact)
        print(f"Długość imienia i nazwiska dla {contact.first_name} {contact.last_name}: {contact.label_length}")
