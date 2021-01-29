import os
import glob
import pprint

set()
se = set("agnadnbnbadn;bjk;qernj")
# {'g', 'j', 'q', 'n', 'd', 'k', 'e', 'r', ';', 'b', 'a'}


se2 = {15, 1, 2, 3, 8,
       (10, 10), 14, 12, 10,
       open('tmp.txt', 'w')}

# se2.add(12)
se2.remove(12)
# se2.remove(18)
se2.discard(18)
# se3 = se2.copy()
# se3.clear()
# se2.update(se)  # list.extend(list2)
# se2.pop()  # list.pop()
print(se.isdisjoint(se2))
se.union()
# hash([1,1]) # not working for mutable objects

# >>> se.intersection(se2)
# >>> {'e', 'a', 'j', 'n', 'q', ';', 'k', 'r', 'g', 'b', 'd'}
res = set()

for element in se:  # se.difference(se2)
    if element not in se2:
        res.add(element)
print(res)
res.clear()

for element in se2:  # se2.difference(se)
    if element not in se:
        res.add(element)
print(res)

lst = [1, 2, 4, 5, 7, 8, 10, 15]

d = {8: [1, 2, 3, 4, 5, 6, 7, 8, 9], 'a': se}

d['abc'] = 'value'
var = d.get('ab', '')   # --> ""
var = d.get('a', '')   # -->  se

var2 = d.pop('a')

# d.clear() # clear

# >>> d.get('a')
# >>> {';', 'd', 'j', 'a', 'k', 'q', 'n', 'b', 'g', 'e', 'r'}
#
# >>> d['a']
# >>> {';', 'd', 'j', 'a', 'k', 'q', 'n', 'b', 'g', 'e', 'r'}
# d['ab']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'ab'

for key, value in d.items():
    print(key, '-'*5, value)

# value = None
#
# if d.get(8):
#     value = d[8]
# else:
#     d[8] = value

d.setdefault(10, None)
d.clear()
d.setdefault(10, "None")

path_dict = {}
files = glob.glob('s*.py')
f = os.listdir('.')
for item in f:
    print(item)
    print("Is dir:",os.path.isdir(item))
    print("Is file:", os.path.isfile(item))
    print(os.path.exists(item))
    # os.walk()

contents = []

pprint.pprint(files)
#
# for path in files:
#     with open(path) as f:
#         path_dict[path] = f.read(100)


for path in files:
    with open(path) as f:
        contents.append(f.read(100))

for path in zip(files, contents):
    path_dict.setdefault(path[0], path[1])

path_d2 = dict(zip(files, contents)) # path_d2.items()

path_d2.update({1:1, 2:2})
path_d2.items()

path_dict['path_d2'] = path_d2















