text = "NameError: name 'ohhoh' is not defined 10"
key = ""
key2 = "John"

key in text  # --> True
key2 not in text  # --> True

bd = bytes(10)

print(bd)
print(bd.decode('utf-8'))
# data = input(":")
# bd = bytes(data, 'utf-8')

text_tmpl = "Занятие 4. ."
my_data = "String operations, formats. If else statement, for loop"
my_int_data = 5

# %
print("Занятие %i. %s" % (my_int_data, my_data))
text_tmpl + my_data

# "".format()
# print(
#     # "Занятие {}. {}".format(my_int_data, my_data),
#     # "Занятие {1}. {0}".format(my_int_data, my_data),
#     "Занятие {1:-^3}. {0}".format(my_int_data,
#                                   my_data),
#     f'Занятие {my_int_data}. {my_data}.',
#     r"\n\t",
#     b"abccdefgh",
#     sep="\n")

# input --> str, admin, ""

if not key:
    key = "name"
else:
    key = ""

key = "name" if not key else print() #---> None


if input("Your first name:").lower():
    print("You enter first name")
    print("done")
else:
    print("No data requested")

if input("Your second name:").lower():
    print("You enter second name")

elif input("Your age:").lower():
    print("You enter age")

if not key:
    key = "default value"
    print(key)

symbol = 'e'

for symbol in text:
    print(symbol)
    if symbol == 'e':
        break
    else:
        continue
else:
    print("Init done")

# if symbol == text[-1]:
#     print("Init done")



for i in range(6):
    print(i)
    for symbol in text:
        print(symbol)
        if symbol == 'e':
            break
    if i > 3:
        break
#
# >>> lst
# >>> [10, (1+1j), b'abcdefg', 'a ', 'abcdefgj']
# lst2
# [10, 15]
# >>> lst3
# >>> [[10, 15], [10, 27]]
#
# >>> id(lst)
# >>> 20456632
#
# >>> lst.append("
# ...
# ... )
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: append() takes exactly one argument (0 given)
# >>> lst.append("a")
# >>> lst
# >>> [10, (1+1j), b'abcdefg', 'a ', 'abcdefgj', 'a']
#
# >>> lst.append(l)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: append() takes exactly one argument (0 given)
# >>> lst.append(lst2)
# >>> lst
# >>> [10, (1+1j), b'abcdefg', 'a ', 'abcdefgj', 'a', [10, 15]]
#
# >>> lst.pop()
# >>> [10, 15]
#
#
# >>> >>>
# >>> x = lst.pop()
# >>> x
# >>> 'a'
#
# >>> lst
# >>> [10, (1+1j), b'abcdefg', 'a ', 'abcdefgj']
#
# >>> len(l)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: len() takes exactly one argument (0 given)
# >>> len(lst)
# >>> 5
#
# >>> lst.extend(lst2)
# >>> lst
# >>> [10, (1+1j), b'abcdefg', 'a ', 'abcdefgj', 10, 15]
#
#
# >>> >>>
# >>> lst[0]
#   File "<stdin>", line 1
#     lst[]
#         ^
# SyntaxError: invalid syntax
# >>> lst[0]
# >>> 10
#
# >>> lst[0] = 1547
# >>> lst
# >>> [1547, (1+1j), b'abcdefg', 'a ', 'abcdefgj', 10, 15]
#
# >>> lst.remove('a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: list.remove(x): x not in list
# >>> lst.remove('a ')
# >>> sorted(t)
# >>> []
#
#
# >>> >>> sorted(lst)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<' not supported between instances of 'complex' and 'int'
# >>> del lst[1]
#   File "<stdin>", line 1
#     del lst[]
#             ^
# SyntaxError: invalid syntax
# >>> del lst[1]
# >>> lst
# >>> [1547, b'abcdefg', 'abcdefgj', 10, 15]
#
# >>> sorted(l
# ... )
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: sorted expected 1 arguments, got 0
# >>> sorted(lst)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<' not supported between instances of 'bytes' and 'int'
# >>> del lst[1]
# >>> sorted(lst)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<' not supported between instances of 'str' and 'int'
# >>> "" < 1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<' not supported between instances of 'str' and 'int'
# >>> lst.sort()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<' not supported between instances of 'str' and 'int'
# >>> lst2
# >>> [10, 15]
#
# >>> lst.append(12)
# >>> lst2.append(12)
# >>> lst2
# >>> [10, 15, 12]
#
# >>> sorted(lst2)
# >>> [10, 12, 15]
#
# >>> s  = sorted(lst2)
# >>> s
# >>> [10, 12, 15]
#
# >>> lst2
# >>> [10, 15, 12]
#
# >>> lst2.sort()
# >>> lst2
# >>> [10, 12, 15]
#
# >>> text = """print("Hello world1")
# print("Hello world2")
# print("Hello world3")
# print("Hello world4")
# print("Hello world5")... ... ... ... """
# >>> text
# >>> 'print("Hello world1")\nprint("Hello world2")\nprint("Hello world3")\nprint("Hello world4")\nprint("Hello world5")'
#
#
# >>> >>>
# >>> lst4 = text.splitlines()
# >>> lst4
# >>> ['print("Hello world1")', 'print("Hello world2")', 'print("Hello world3")', 'print("Hello world4")', 'print("Hello world5")']
#
# >>> sorted(lst4)
# >>> ['print("Hello world1")', 'print("Hello world2")', 'print("Hello world3")', 'print("Hello world4")', 'print("Hello world5")']
#
# >>> words = text.split()
# >>> words
# >>> ['print("Hello', 'world1")', 'print("Hello', 'world2")', 'print("Hello', 'world3")', 'print("Hello', 'world4")', 'print("Hello', 'world5")']
#
# >>> sorted(w)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: sorted expected 1 arguments, got 0
# >>> sorted(words, key=len)
# >>> ['world1")', 'world2")', 'world3")', 'world4")', 'world5")', 'print("Hello', 'print("Hello', 'print("Hello', 'print("Hello', 'print("Hello']
#
#
# >>> >>>
# >>> lst5 = sorted(words, key=len)
# >>> lst5[-]
#   File "<stdin>", line 1
#     lst5[]
#          ^
# SyntaxError: invalid syntax
# >>> lst5[-1]
# >>> 'print("Hello'
#
# >>> [][-]1
#   File "<stdin>", line 1
#     [][]1
#        ^
# SyntaxError: invalid syntax
# >>> [[]
# >>> []
#
# >>> [][-1]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range

lst = [10, (1+1j), b'abcdefg', 'a ', 'abcdefgj']
lst2 = lst.copy()
lst3  = lst[:]
import copy
lst5 = copy.deepcopy(lst)
lst.clear()
print(lst.reverse())
print(lst[::-1])
