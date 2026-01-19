from address import Address
from mailing import Mailing

from_addr = Address("636044", "Томск", "Герасименко", "6", "10")
to_addr = Address("634046", "Новосибирск", "Толмочева", "10", "20")

mailing = Mailing(to_addr, from_addr, 350, "AB123456789RU")

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)