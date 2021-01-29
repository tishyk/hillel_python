import random
import time
import sys
import os

count = 100

while count > 4:
    if count > 15:
        count -= 1
        continue
    print(True, count)  # print it 10 times
    if count == 3:
        print("Exit from loop")
        break
    count -= 1

else:
    print("Else block")

lst = []
random.randint(0, 10)  # ---> 0 . 10 , 4

# while len(lst) < 10:
#     lst.append(random.randint(0, 10))
#     print(lst)
# time.sleep(random.randint(0, 3))

# download from www, buffer
# delete, create, rename, move, move with metadata
# search files,
# file metadata
# search in files: pdf, doc, xls, image, mp3, mp4, db

path = "C:/Projects/basics/hillel1/lesson11114.py"
file = open(path, "a+", encoding='utf-8', newline="")

# read, write, append   # keys: r, w, a, r+, w+, a+, rb, wb, ab, rb+, wb+, ab+,
# load, save, create
# search some text in file, binary search
# file.readable()
wrt_list = ["some file data1\n",
            "some file data2\n",
            "some file data3\n"]

# file.writelines(wrt_list)

# file.write("some file data1\n")
# file.write("some file data2\n")
# file.write("some file data3\n")
# file.flush()
print(sys.getsizeof(file))
file.seek(0)
line = file.readline()
line.splitlines(keepends=False)
print(line.endswith('\n'))

print("Line", line)

# print(file.read(8))  # return string
# print(file.read()[:10])  # return string[:]
# file.seek(0)
# print(file.readline())  # return string
# file.seek(100)
# print(file.readlines())  # return list object
print(file.name)
print(file.mode)
print(file.fileno())  # ?

# file.close()
# os.remove(path)
#os.rmdir("Dir name")

if os.path.exists("hello.py"):
    mode = "a"
else:
    mode = "w"

mode = "a" if os.path.exists("hello.py") else "w"

for line in wrt_list:
    with open(path, "a+", encoding='utf-8', newline="") as file:
        file.writelines(line)
        print(file.closed)
    print(file.closed)
