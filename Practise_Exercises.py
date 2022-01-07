from functools import wraps

# Se não utilizar-mos estas instruções a função hello vai ser igual há função wrap(decorator), mas utilizando estas
# instruções a função hello vai ser igual há função hello, como deve ser...


def log_decorator(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f"Calling func: {func}")
        func(*args, **kwargs)
        print(f"Func {func} finished its work")
    return wrap


@log_decorator
def hello():
    print("hello, world!")


# Utilizamos help para ver se esta tudo bem com a nossa função
help(hello)
