# Binary Types:	bytes, bytearray

numbers = [150, 12, 44, 32];
x = bytes(numbers);

print(type(x));

numbers2 = [150, 12, 44, 32, 45, 33, 251];
y = bytearray(numbers2);
print(type(y))