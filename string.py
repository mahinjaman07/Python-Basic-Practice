# Assign String to a Variable

# myStr = "Hello World";
#
# print(myStr);
# print(type(myStr));

# Multiline Strings


# txt = f"""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type specimen book.
# """
#
# print(txt);
# print(type(txt));


# Strings are Arrays
# myStr = "Hello World";
# print(myStr[0])
# print(myStr[0:5])


# loop of string

# fruit = "Banana";
#
# for letter in fruit:
#     print(letter);


# check string length

# print(len(fruit));

# Check String


# mySelf = "I am Mahin Jaman. I am from Bangladesh";
#
# check = "Mahin" in mySelf;
# print(check);
#
# check2 = "Tangail" in mySelf;
# print(check2);


# Check if NOT

# mySelf = "I am Mahin Jaman. I am from Bangladesh";
#
# checknot = "Tangail" not in mySelf;
# print(checknot);
#
# checknot2 = "Mahin" not in mySelf;
# print(checknot2);

# Slicing string

# txt = "Hello World";
#
# s = txt[0:5];
# print(s);


# modify string

# convert upper case
# txt = "hello world";
# u = txt.upper();
# print(u)

# convert lower case
# txt2 = "HELLO WORLD";
# L = txt2.lower();
# print(L);

# strip() / remove white space

# txt = "         hello world  ";
#
# x = txt.strip();
# print(x)


# replace

# txt = "Heo World";
#
# replaceTxt = txt.replace("Heo", "Hello");
#
# print(replaceTxt);

# split  / split diye amra amader text te line by line bhangte pari

# myText = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
#
#
# splitTxt = myText.split(" ");
#
# for x in splitTxt:
#     print(x);



# contcat string

a = "Hello ";
b = "World";

c = a + b;
print(c)

# formate string

d = f"Hello {b}";

print(d);


#Escape Characters

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# string formating
name = "Mahin Jaman"

age = 18;


mySelf = f"I am {name}. I am {age} years old";
print(mySelf)