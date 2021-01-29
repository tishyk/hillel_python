#! usr/bin/python3
#! coding: utf-8

import os
import time

import sys
sys.path.append("../hillel1")

from defaults.ver2.urls import *

__all__ = ['x', 'y']
x = True # any integer but not 0,
y = False   # 0, "", tuple(), [], {}

text = """Python files names (правила наименования файлов, импорт имен)

    Mutable vs Immutable Objects(black boxes,)

    Python Built in Functions and object methods (dir, help, sorted, min, id, len)

    Python Booleans (True/False, 0/1, ""/"a", None/"a")

    Python Logical Operators ( or, and, or and or, and or)

    Python Arithmetic Operators. String Concatenation (+, -, *, **, /, //, %, pow, math.pow)

    Python Assignment Operators (=, +=, -=, *=, /=)

    Python Comparison Operators (==, !=, >, <, >=, <=)

    Python Bitwise Operators | https://younglinux.info/python/task/binary | https://wiki.python.org/moin/BitwiseOperators

    Python Identity Operators (is, is not)

    Python Membership Operators (in, not in)



    Python Numbers and data size

    Python Strings

    Strings as array

    String Slicing ([0], [0:5], [-1], [1:5:2])

    String Negative Indexing

    String Length

    String Methods (upper())

    Check String (in, not in)
    """

print(__file__)

if __name__ == "__main__":
    print(__name__)

    import session12_code
    print(__file__)

    bytearray
    import math


    type(10)
    x = 10
    f = 10.112544
    type(x)
    # help(x)
    # help("")

    dir(x)
    "".isupper()
    pass



    z = None # False

    # >>> x
    # >>> True
    #
    # >>> x and y
    # >>> False
    #
    # >>> True and True and True and False
    # >>> False
    #
    #
    # >>> >>>
    # >>> and True
    #   File "<stdin>", line 1
    #     and True
    #       ^
    # SyntaxError: invalid syntax
    # >>> x or y
    # >>> True
    #
    # >>> x or y or None
    # >>> True
    #
    # >>> x or ohhho
    # >>> True
    #
    #
    # >>> >>>
    # >>> ohhoh or x
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # NameError: name 'ohhoh' is not defined
    # >>> x or y and z
    # >>> True
    #
    #
    # >>> >>>
    # >>> y and z or x
    # >>> True
    #
    # >>> z = True
    # >>> y and z or x
    # >>> True
    #
    #
    # >>> >>>
    # >>> not x
    # >>> False
    #
    # >>> not y
    # >>> True
    #
    # >>> x and not y
    # >>> True
    #
    #
    # >>> >>>
    # >>> x and not y and not z
    # >>> False
    # z
    # True
    # >>> z = None
    # >>> x and not y and not z
    # >>> True
    #
    #
    #
    # >>> >>> >>>
    # >>> x and not y and not z and 0
    # >>> 0
    #
    #
    # >>> >>>
    # >>> x and not y and not z and 0
    # >>> 0
    #
    # >>> result = x and not y and not z and 0
    # >>> type(result)
    # >>> <class 'int'>
    #
    #
    # >>> >>>
    # >>> reslut_b = True and False or True
    # >>> type(r)eslut_b
    #   File "<stdin>", line 1
    #     type()eslut_b
    #                 ^
    # SyntaxError: invalid syntax
    # >>> type(reslut_b)
    # >>> <class 'bool'>
    #
    # >>> r
    # >>> bool(result)
    # >>> False
    #
    # >>> int(False)
    # >>> 0
    #
    # >>> int(True)
    # >>> 1
    #
    # >>> str(False)
    # >>> 'False'
    #
    #
    # >>> >>>
    # >>> bool("")
    #   File "<stdin>", line 1
    #     bool(")
    #           ^
    # SyntaxError: EOL while scanning string literal
    # >>> bool("")

    #x = x + x
    # +, -, *, **, /, //, %, pow, math.pow

    print(pow(2, 3))
    print(math.pow(2, 3))
    print(math.pi)
    print(round(math.pi, 3))
    print(round(100.5548887, 2))

    # >>> x = 10
    # >>> y = 3
    # >>> x / y
    # >>> 3.3333333333333335
    #
    #
    # >>> >>>
    # >>> x // y
    # >>> 3
    #
    # >>> 1/2
    # >>> 0.5
    #
    # >>> 1//2
    # >>> 0
    #
    # >>> x % y
    # >>> 1
    #
    # >>> 2 % 2
    # >>> 0

    # ==, !=, >, <, >=, <=

    x == y # box values

    x = 15555555555444444
    y = 15555555555444444
    s_x = "abc"
    s_y = "abc"

    # >>> x == y
    # >>> True
    #
    # >>> x is y
    # >>> True
    #
    # >>> id(x)
    # >>> 27041944
    #
    # >>> id(y)
    # >>> 27041944
    #
    # >>> "abc" >
    # >>> 'abc'
    #
    # >>> "a
    #   File "<stdin>", line 1
    #     "
    #     ^
    # SyntaxError: EOL while scanning string literal
    # >>> ord("a")
    # >>> 97
    #
    # >>> ord("b")
    # >>> 98
    #
    # >>> "a" < "b"
    # >>> True
    #
    #
    #
    # >>> >>> >>>
    # >>> "abc" > "abd"
    # >>> False
    #
    #
    # >>> >>>
    # >>> "abc" < "abd"
    # >>> True
    #
    #
    # >>> >>>
    # >>> ord("a")
    # >>> 97
    #
    # >>> chr(65)
    # >>> 'A'

    line_27 = u"хелоу"
    line = r"хелоу\n"
    print(line)



    # "".index()
    "".find('1')
    lines = text.replace("\n\n", "\n")
    list_lines = lines.splitlines()
    print(list_lines)

    count = 0
    short_line = ""


    for line in list_lines:
        line_len = len(line)
        if line_len > 0:
            if not count:
                count = line_len

            if line_len < count:
                count = line_len


    line = "Python files names"
    print(line[10])

    # >>> line[10]
    # >>> 'e'
    #
    #
    # >>> >>>
    # >>> line[4:5]
    # >>> 'o'
    #
    # >>> line[4:6]
    # >>> 'on'
    #
    # >>> line.index('o')
    # >>> 4
    #
    #
    # >>> >>>
    # >>> line.index('n')
    # >>> 5
    #
    # >>> line[line.index('o'):line.index('n') + 1]
    # >>> 'on'
    # >>> line[-1]
    # >>> 's'
    #
    #
    # >>> >>>
    # >>> line[::-1]
    # >>> 'seman selif nohtyP'
    #
    # >>> line[6:-2:-1]
    # >>> ''


