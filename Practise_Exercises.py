def log_decorator(func):
    def wrap():
        print(f"Calling func: {func}")
        func()
        print(f"Func {func} finished its work")
    return wrap


def hello():
    print("hello, world!")


wrapped_by_logger = log_decorator(hello)
wrapped_by_logger()


# O resultado da execusão deste codigo vai ser o mesmo, só que aqui é utilizado uma nova instrução
@log_decorator
def hello():
    print("hello, world!")


hello()

