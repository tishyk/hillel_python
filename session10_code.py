import json

loaded_dict = json.load(open('event_default.json'))


def load_emails(**kwargs):
    for em in kwargs.get('attendees', []):
        for key in em:
            print(em[key])


load_emails(**loaded_dict)

init_path = "tmp2.txt"
messages = ["tmp3.txt",
            "message one", "message two", "last message"]

path = "tmp45.txt"


def log(msg, path=[]):
    # messages = ["message one", "message two", "last message"][::-1]

    if "last message" not in msg:
        with open(init_path, 'r') as f:
            for line in f.readlines():
                if msg in line:
                    messages.remove(msg.strip())
                    break
            else:
                with open(init_path, 'a') as f:
                    f.write(str(msg))
                    print(msg)

    else:
        with open(path, 'a') as f:
            f.write(str(msg))
            print(msg)
    if isinstance(path, list):
        path.append(msg)
    return path


# for msg in messages[:]:
#     if "last message" in msg:
#         log(path=path, msg=f"{msg}\n",)
#     else:
#         log(f"{msg}\n", init_path, 10, 15, 15, [], {1:".hello"})

# del msg
# print(messages)
# result = log("abc")


def set_graph(*args):
    if len(args) == 0:
        print(0)
    elif len(args) < 3:
        print(1, 2)
    elif len(args) == 3:
        print(3)
    print(args)


# set_graph()
# set_graph(100)
# set_graph(200, 380)
# set_graph(800, 200, 380)
# set_graph(800, 200, 380, "asjhsd")
#
# def extract(*msgs):
#     #(["message one", "message two", "last message"], ) without extraction
#     with open(msgs[0], 'w'):
#         if len(msgs) > 1:
#             for i in msgs[1:]:
#                 print(i)
#
# extract(*messages)  # --> extract("message one", "message two

#
# def extract(msg, path=[],  **kwargs):
#     # (["message one", "message two", "last message"], ) without extraction
#     with open(kwargs.get('path', init_path), 'w'):
#         if len(kwargs) > 1:
#             for k in kwargs:
#                 print(k, kwargs[k])
#     if kwargs.get("hello"):
#         print("Hi")
#     if kwargs.get("close_after"):
#         exit(1)
#
#
# arguments = {'y': 10, 'z': "path", 'hello': True, 'path': "def_path.txt"}
#
# # extract("Hello", **arguments)  # --> extract("message one", "message two", "last message")
#
# arguments = {'y': 10, 'z': "path", 'x': True, 'path': "def_path.txt"}
#
#
# def func(x, y, z, path):
#     print(x, y, z, path)
#
# func(**arguments)

lm = lambda **kwargs: kwargs.get('attendees', []) # --> None
var = lm()
print(var)

sorted(["ab", "abc", 'z'], key=lambda msg: 100 if msg=='z' else 0)