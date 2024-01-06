class parent:
    car = "BMW";
    House = "10 flore";
    Money = "100 crore"



class son(parent): #amra parent ke inherit korar maddhome amra son1 er moddhe parent er shob kichur access peye gechi
    bike = "KTM";
    phone = "Iphone 14"



son1 = son();

print(son1.car) # parent theke
print(son1.bike)

