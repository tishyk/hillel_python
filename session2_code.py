
name = input("Enter name: ")

# +, -, /,
if name == "sergii":
    print("Hello ", name)


# First name
"""
line 1
for
my comment
"""

print(isinstance(name, (str, int)) )#--> True False

if type(name) == str:
    print(str)


# name = ''
# firstName = 'Sergii'
# secondName = 'TS'
#
# firstName, secondName, args = 'Sergii', 'TS', "a", 'b' , 'c'
#
#
#
# forMyFirstvariableinit = 'Kate'
# name1 = 'Jane'
# NAme1 = 'Jane'
#
# type(name) # --> str
#
# name2 = name1
# name3 = name1
#
# id_number = 319101010
#
# if "Sergii":
#     print(True)
#     print(True)

a = 1
b = 1
print(id(a))
print(id(b))

n = 10 # input("Номер элемента ряда Фибоначчи: ")
n = int(n)

i = 0
while i < n - 2:
    fib_sum = a + b
    a = b
    b = fib_sum
    i = i + 1

print(b)







