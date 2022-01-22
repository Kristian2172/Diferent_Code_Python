class StaticTest:
    x = 1


t1 = StaticTest()

print(f"via instance: {t1.x}")
print(f"Via class: {StaticTest.x}")

# Esta atribuição acontece ao nivel da instancia
t1.x = 2

# Estes dois 'x' que estam abaixo sao dois diferentes atributos
print(f"Via instance: {t1.x}")
print(f"Via class: {StaticTest.x}")

# Esta atribuição ja acontece ao nivel da classe
StaticTest.x = 3

print(f"Via instance: {t1.x}")
print(f"Via class: {StaticTest.x}")


class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f"{self.month}-{self.day}-{self.year}"

    @classmethod
    def millenium_c(cls, month, day):
        return cls(month, day, 2000)

    @staticmethod
    def millenium_s(month, day):
        return Date(month, day, 2000)


d1 = Date.millenium_c(6, 9)
d2 = Date.millenium_s(6, 9)

print(d1.display())
print(d2.display())


class DateTime(Date):
    def display(self):
        return f"{self.month}-{self.day}-{self.year} - 00:00:00PM"


dt1 = DateTime(10, 10, 1990)
dt2 = DateTime.millenium_c(10, 10)

print(isinstance(dt1, DateTime))
print(isinstance(dt2, DateTime))

print(dt1.display())
print(dt2.display())
