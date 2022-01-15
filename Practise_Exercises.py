class Character:

    def __init__(self, race, damage=10, armor=20):
        # Criação dos atributos
        self.race = race
        self.damage = damage
        self.armor = armor


unit = Character("Elf", 20, 40)

print(unit.damage)
print(unit.armor)
