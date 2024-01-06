class baba:
    car = "BMW";
    house = "10 flore";
    money = "100 crore"

class kaka1:
    shop = "Fashion Showroom";
    flat = "5 flat";
    bike = "KTM"


class kaka2:
    laptop = "MAQ";
    phone = "I-Phone 14 pro"


class child(baba, kaka1, kaka2):
    pass;


Mahin = child();

print(Mahin.money) # baba theke
print(Mahin.bike) # kaka1 er theke
print(Mahin.phone) # kaka2 er theke

