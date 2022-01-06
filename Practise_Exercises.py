def square(*args):
    return [x * x for x in args]


# Quando vai se executar o codigo o que vai ser executado vai ser da classe list

result = square(1, 2, 3, 4, 5)
print(result)
print(type(result))


def triple(*args):
    return [x * 3 for x in args]


result = triple(1, 2, 3, 4, 5)
print(result)


# Quando vai se executar o codigo o que vai ser executado vai ser da classe int

def square(number):
    return number * number


numbers = [1, 2, 3, 4, 5]

mapped_seq = map(square, numbers)
for x in mapped_seq:
    print(x)


# A função "filter" permite filtrar o codigo onde é necessario

def is_adult(age):
    return age >= 18


ages = [14, 18, 21, 16, 30]

print(list(filter(is_adult, ages)))


# Exemplos de uso de "lambda"

is_adult = lambda age: age >= 18

print(list(filter(is_adult, ages)))

multiplier = lambda z, y: z * y
print(multiplier(2, 3))

