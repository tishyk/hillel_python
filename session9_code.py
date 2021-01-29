print()
name = print
# name("Hello")
print = name
# print(10)

t1 = (1, 2, 5, 4, 8)
t2 = 1, 2, 5, 4, 8

logfile_path = "log.txt"
msg = "Hello world"


# def log(n):
#     """ Show incoming message and write it into logfile.
#     Type your message: """
#     incoming = input(log.__doc__)
#     print(incoming)
#     # if incoming == "q":
#     #     return "q"
#     with open(logfile_path, 'a') as f:
#         f.write(incoming + "\n")
#     return None


# result = log(logfile_path) # call to write log file path
res = "adjklfgbdjkb".replace('f', "")
res2 = [1, 0, 5, 5, 5]
rem_result = res2.remove(5)


# log(msg)
# log(__file__)
# log(__name__)
# log(vars())
#
# print(log.__name__)
# print(log.__doc__)

def local_vs_global(parameter):
    global msg
    msg = "Hello" + msg
    print(msg[::-1])
    msg = msg[::-1]
    res = "adjklfgbdjkb".replace('f', "")
    print("Locals", locals())
    print("Globals", globals())

    def log():
        """ Show incoming message and write it into logfile.
        Type your message: """
        msg = input(log.__doc__)
        # if incoming == "q":
        #     return "q"
        with open(logfile_path, 'a') as f:
            f.write(msg + "\n")
        print("\t", "Locals", locals())
        print("\t","Globals", globals())

        def nested_log():
            """ Show incoming message and write it into logfile.
            Type your message: """
            nonlocal msg
            msg = nested_log.__doc__
            print("\t"*3, "Locals", locals())
            print("\t"*3, "Globals", globals())
        nested_log()

    log()

    return msg[::-1], res, None  # tuple object box[0]


# res = local_vs_global()  # msg[::-1]

def l1():
    varl1 = 10
    def l2():
        nonlocal varl1
        varl1 = 15 + varl1
        return varl1
    res = l2()
    print(varl1)
    return res

r = l1()
print(r)
