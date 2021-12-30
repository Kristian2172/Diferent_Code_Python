greeting = "hello, world"
chars = []

for x in greeting:
    chars.append(x)

print(chars)

# O resultado destes dois codigos é o mesmo mas a estrutura é diferente

chars = [i for i in greeting]
print(chars)

# Outros exemplos onde podemos usar o list comprehension
numbers = [n for n in range(0, 11)]
print(numbers)

numbers = [n * n for n in range(0, 11)]
print(numbers)

# Mostra a multiplicacao dos numeros impares
numbers = [n * n for n in range(0, 11) if n % 2 != 0]
print(numbers)

# Conversão de centimentros para polegadas
len_in_centi = [12, 10, 54, 124, 64]
len_in_inches = [(round(cm / 2.54, 2)) for cm in len_in_centi]
print(len_in_inches)


