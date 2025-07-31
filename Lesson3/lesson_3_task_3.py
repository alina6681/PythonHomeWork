from address import Address
from mailing import Mailing

to_address = Address
from_address = Address
to_address = 236040, "г. Москва", "ул. Невская", 25, 15
from_address = 236404, "г. Калиниград", "ул. Черняховского", 43, 12

sending = Mailing
sending(to_address, from_address, 1200, 1234567890)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)