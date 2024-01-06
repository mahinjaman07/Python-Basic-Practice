# access list item
myList = ["a", "b", "c", 1, 2, 3];
# use indexing
a = myList[0];
print(a);

# use negative indexing

b = myList[-1];
print(b);

# use variabe

item1, item2, item3, item4,item5, item6 = myList;
print(item4);

# while loop

num = 0;
while num < len(myList):
    # print(num);
    item = myList[num];
    print(num , item)
    num += 1;


# for loop

for item in myList:
    print(item)


# use range

newList = myList[0: 4];
print(newList);


# use *

x, y, *z, w = myList;

print(x, y);
print(z);
print(w);
