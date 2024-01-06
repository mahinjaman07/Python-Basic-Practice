person = {
    "name": "Mahin Jaman",
    "address": "Dhaka, Bangladesh",
    "age": 19
};

# use pop()
person.pop("name");
print(person);

# use popitem() / eta amader dict er last item remove kore dibe

person.popitem();

print(person)


# clear()
person.clear();
print(person)

# del / eta amader pora dict kei delete kroe dive jar karone amra kono output pabo na

del person;

# print(person) kono dict , list, tuple , set ke del korar por tar kono access nite parbo na jode nite chai tahole amader akta error dibe