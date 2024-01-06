myList = ["a", "b", "c", 1, 2, 3];
# use append
myList.append("Apple");
print(myList);

# use extend
myList2 = [101, 201, 301, "M","N","O"];
myList.extend(myList2);

print(myList);

# use +

myList3 = myList + myList2;
print(myList3)


# use insaert

myList.insert(1, "Hello World");
print(myList)