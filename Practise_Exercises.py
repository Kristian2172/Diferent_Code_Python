def greeting():
    print("Hello World")


def print_name(name):
    print(name)


print_name("John")


def get_sum(a, b):
    return a + b


result = get_sum(10, 2)
print(result)


def is_adult(age):
    return age >= 18


is_adult = is_adult(20)
print(is_adult)


def is_palindrome(text):
    return text == text[::-1]


is_palindrome("aabaa")
is_palindrome("aabba")


def calc_taxes(p1, p2, p3):
    return sum((p1, p2, p3)) * 0.06


calc_taxes(10, 20, 30)


# Para receber inumeros argumentos temos de meter *args
def calc_taxes(*args):
    for x in args:
        print(f"Got payment = {x}")
    return sum(args) * 0.06


calc_taxes(10, 20, 30, 40)


# Para receber inumeros argumentos que contêm key values pairs devemos de meter **kwargs
def save_players(**kwargs):
    for k, v in kwargs.items():
        print(f"Player {k} has rating {v}")


save_players(Carlsen=2800, Giri=2780)
