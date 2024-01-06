class baba:
    car = "BMW";
    house = "10 flore";
    money = "100 crore"

class kaka1(baba):  # kaka1 er moddhe baba ke inherit korar maddhome babar shob data er access kaka1 peye geche
    shop = "Fashion Showroom";
    flat = "5 flat";
    bike = "KTM"


class kaka2(kaka1): # kaka1 er moddhe baba ke age inherit koray babar shob data er access kaka1 peye geche abar kaka2 er moddhe kaka1 ke inherit korar maddhome kaka2 er moddhe kaka1 e thaka data and baba er moddhe thaka all dataa kaka2 er moddhe access peye geche
    laptop = "MAQ";
    phone = "I-Phone 14 pro"


class child(kaka2): # kaka2 er moddhe kaka1 and kaka1 er moddhe baba ke inherit korar maddhome kakaw er moddhe kaka1 and baba er full data access peye geche ar amra child er moddhe kaka2 ke inherit korar maddhome kaka2 ar opore thaka kaka1 and babaer full data access peye gechi

    pass;


mahin = child();

print(mahin.money) #baba
print(mahin.flat) #kaka1
print(mahin.laptop) # kaka2