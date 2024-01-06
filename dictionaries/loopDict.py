person = {
    "name": "Mahin Jaman",
    "address": "Dhaka, Bangladesh",
    "age": 19,
    "class": 10,
    "group": "science"
};

for item in person:
    # print(item)  output key name
    print(item, person[item]);



# only keys loop

keys = person.keys();
for key in keys:
    # print(key) output only key name
    print(key, person[key]);



# only values loop

values = person.values();

for value in values:
    print(value);


 # loop in both key and value

both = person.items();

for [key, value] in both:
    print(key, value)