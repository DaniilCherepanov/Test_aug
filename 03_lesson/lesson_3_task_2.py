from smartphone import Smartphone

catalog = []

# Добавляем 5 телефонов
catalog.append(Smartphone("Apple", "iPhone 14", "+79112223344"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79213334455"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79314445566"))
catalog.append(Smartphone("Google", "Pixel 7", "+79415556677"))
catalog.append(Smartphone("OnePlus", "10 Pro", "+79516667788"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")