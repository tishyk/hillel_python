# import string
# string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.digits
# '0123456789'
# range(10)
# range(0, 10)
# string.octdigits
# '01234567'
# "mno" in string.ascii_letters
# True
# string.ascii_letters.index("mno")
# 12
# template = 'mp\d'
# text = 'abc.mp4 defghijklmpnopqrstuvwxyzABCDEF mp3 GHIJKLMNOPQRSMP4TUVWXYZ'
# import re
# re.findall(template, text)
# ['mp4', 'mp3']
# text = 'abc.mp4 defghijklmpnopqrstuvwxyzABCDEF filename.mp3 GHIJKLMNOPQRSMP4TUVWXYZ'
# re.findall("\w+", text)
# ['abc', 'mp4', 'defghijklmpnopqrstuvwxyzABCDEF', 'filename', 'mp3', 'GHIJKLMNOPQRSMP4TUVWXYZ']
# re.findall("\w+\.mp\d", text)
# ['abc.mp4', 'filename.mp3']
# re.findall("\w+.mp\d", text)
# ['abc.mp4', 'filename.mp3']
# text = '''abc.mp4 defghijklmpnopqrstuvwxyzABCDEF filename.mp3 GHIJKLMNOPQRSMP4TUVWXYZ'''
# text = '''abc.mp4 defghijklmpnopqrstuvwxyzABCDEF
# ... filename.mp3 GHIJKLMNOPQRSMP4TUVWXYZ'''
# re.findall("\w+\.mp\d", text)
# ['abc.mp4', 'filename.mp3']
# re.findall("\w+\.mp\d", text, re.S, re.IGNORECASE)
# ['abc.mp4', 'filename.mp3']

# i = 10
# f = float(1)  # 1.0
# c = 1 + 1j
# b = b"abcdefg"
# st = "a "
# sts = "abcdefgj"
#
# var = 10, 15, 0
# x,y,z,*anything_else  = 10, 15, 0, 5, 5, 5, 8
# x, *args, end  = "abcdefg"
#
# t = st, sts, c, b, f  # "aabcdefg"
# # t = t[:] + (t[-1],)
#
# t.index(b)  # int
# t.count("a")  #
# print("a " == 'a')
#
# if True or Hello:
#     pass
# if False and hello:
#     pass
#
# for element in t:
#     if isinstance(element, (str, bytes)) and "j" in str(element):
#         print(element)

# >>> t
# >>> ('a', (1+1j), b'abcdefg', 1.0, 1.0)
#
# >>> t.index(f)
# >>> 3
#
# >>> t.count(f)
# >>> 2
#
# >>> for element in t:
# ... 	print(element)
# ...
# >>> a
# (1+1j)
# b'abcdefg'
# 1.0
# 1.0
#
# >>> len(t)
# >>> 5

if __name__ == "__main__":
       list(), [], "".split(),
       #t = tuple()

       i = 10
       f = float(1)  # 1.0
       c = 1 + 1j
       b = b"abcdefg"
       st = "a "
       sts = "abcdefgj"

       lst = [i,
              c,
              b,
              st,
              sts]

       lst2 = [10, 15,]

       lst3 = [[10, 15],
              [10, 27]]


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

# >>> lst.append("a")
# >>> lst
# >>> [10, (1+1j), b'abcdefg', 'a ', 'abcdefgj', 'a']
#
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

# >>> len(lst)
# >>> 5
#
# >>> lst.extend(lst2)
# >>> lst
# >>> [10, (1+1j), b'abcdefg', 'a ', 'abcdefgj', 10, 15]

# >>> lst[0]
# >>> 10
#
# >>> lst[0] = 1547
# >>> lst
# >>> [1547, (1+1j), b'abcdefg', 'a ', 'abcdefgj', 10, 15]

# >>> lst.remove('a ')
# >>> sorted(t)
# >>> []
#
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

# >>> lst5 = sorted(words, key=len)

# >>> [][-1]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
#
# lst = [10, (1+1j), b'abcdefg', 'a ', 'abcdefgj']
# lst2 = lst.copy()
# lst3  = lst[:]
# import copy
# lst5 = copy.deepcopy(lst)
# # lst.clear()
# print(lst[::-1])
# print(lst.reverse())
# lst.insert(2, 544)
#
# from collections import deque
#
# dq = deque(lst)
#
# for elem in range(2):
#        print(dq.pop())
#        #dq.remove(elem)
#
# lst  = lst[:2] + lst2 + lst[2:]



