class Character:
    # Constants
    MAX_SPEED = 100

    def __init__(self, race, damage=10):
        self.damage = damage
        # private
        self.__race = race
        # semi-privados - não se vêm mas podem ser modificados
        self._health = 100

        self._current_speed = 20

    def hit(self, damage):
        self._health -= damage

    # @property dá permissão para ser lido os atributos privados e semi-privados
    @property
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self._current_speed

    # Propriedade com a possibilidade de ser introduzido informação
    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed


c = Character("Elf")

print(c.health)
print(c.race)

print(c.current_speed)
c.current_speed = 50
print(c.current_speed)
c.current_speed = 1000
print(c.current_speed)
c.current_speed = -10
print(c.current_speed)
