def say_hello(name=None):
    if name is None:
        return "hello, world!"
    else:
        return "hello, " + name + "!"
