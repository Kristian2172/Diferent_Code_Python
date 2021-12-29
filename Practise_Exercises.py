# Par ou impar

for i in range(1, 6):
    if i % 2 == 0:
        print(str(i) + " é par")
    else:
        print(str(i) + " é impar")

# Exercicio usando tuple
persons = [("John", 22), ("Bob", 32), ("Dave", 20)]

for (name, age) in persons:
    print(f"{name} is {age} years old")

# Outro exercicio usando tuple
players = dict(Calsen=2842, Caruana=2822, Mamedyarov=2801)

for item in players:
    print(item)

for item in players.items():
    print(item)

for k, v in players.items():
    print(f"{k} has rating {v}")

# find all pairs sum of which equals 0
list1 = [2, 4, -5, 6, 8, -2]
list2 = [2, -6, 8, 3, 5, -2]

pairs = []
for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x, y))

print(pairs)
