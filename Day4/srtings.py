#this file explain the concept of string in python
"""this is indepth explanation of strings"""
""" Program is written by Mr. Bhushan Nawlakhe"""

name='Bhushan '
surname = "Nawlakhe"
name1= "'bsn'"
age=26
b="my name is john ,and i am {} year old"
print(b.format(age))
print(name1*2)
print(name)
print(surname)
print(name,"concatenated with"+surname)
print((name+"concated with"+surname))
element='Elephant'
count=5
print("the item {} is repeated{} times".format(element,count))
elemnt=6
count=12
print("the item %i is repeated %i times"%(elemnt,count))
a="""Lorem ipsum dolor sit
amet,
consectetur adipiscing elite,
sed do euisond and """
x= "rem" not in a
print(x)
print(a)
print(a[-5:-8])
print(a[1])
print(a[2:9])
print(len(a))
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("e","k"))
print(a.split(","))
