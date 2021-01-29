range(10)  # --> 0,1,...9
range(5, 10)  # --> 5,6...9
range(5, 10, 2)  # --> 5,7,9

# from distutils.version import LooseVersion, StrictVersion
# LooseVersion("99") < LooseVersion("100")
# True
# LooseVersion(99) < LooseVersion(100)
# 2.7
range  # list
# xrange() # range(5, 10, 2)

for i in range(10):  # range(10)
    print(i)
    pass

iter_object = iter(range(1, 4))  # check for iterable
i = next(iter_object)  # iter_object.__next__()


def my_gen(start, end, step=1):
    print(f"my_gen({start}, {end}, {step})")
    yield start
    start = start + step
    yield start
    start = start + step
    yield start
    return "Done"


for j in my_gen(3, 5):
    print(j)

it = iter(my_gen(3, 5))

j = next(it)
j = next(it)
j = next(it)

try:
    next(it)
except StopIteration as exec:
    print(exec.value)

text = """Python files names (правила наименования файлов, импорт имен)
Mutable vs Immutable Objects(black boxes,)
Python Built in Functions and object methods (dir, help, sorted, min, id, len)
Python Booleans (True/False, 0/1, ""/"a", None/"a")
Rython Logical Operators ( or, and, or and or, and or)"""

# count = 5
# for line in text.splitlines():
#     print(count, line)
#     count += 1
#
#
# def enumlines(text, start=1, step=1, end=-1):
#     for line in text.splitlines():
#         yield start, line
#         start += step
#         if end > 0 and end < start:
#             break
#
# for i, line in enumlines(text, 10, 2, 14):
#     print(i, line)


# for i, line in enumerate(text.splitlines()):
#     print(i, line)

# for i,j, line in zip(range(5, 100), range(1, 10), text.splitlines()):
#     print(i, line)

result = []


#
# for line in text.splitlines():
#     if line.startswith('P'):
#         result.append(True)
#     else:
#         result.append(False)
#
# print(result)

def check_line(line):
    return line.startswith('P')


line = text.splitlines()[0]
var = check_line(line)
result.append(var)
line = text.splitlines()[1]
var = check_line(line)
result.append(var)
line = text.splitlines()[2]
var = check_line(line)
result.append(var)
line = text.splitlines()[3]
var = check_line(line)
result.append(var)

for line in text.splitlines():
    res = check_line(line)
    result.append(res)

map  # --> result []

result = map(check_line, text.splitlines())
print(result)
print(list(result))

result = map(lambda line: line.startswith('P'), text.splitlines())
print(result)
print(list(result))

all([]) # --> True
all(result) # --> False

any([]) # --> False
any(result) # --> True


result = filter(lambda line: line.startswith('P'), text.splitlines())
print(result)
print(list(result))

result = filter(lambda i: i[0] > i[1] and i[1] > 50, zip(range(10, 100), range(5, 95)))
print(result)
print(list(result))

