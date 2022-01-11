import math


# Usamos "ValueError" como ja existe na biblioteca python
def calc_square(ab, ac, bc):
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise ValueError("One of the sides is less or equal to 0!")

    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))

    return s


# square = calc_square(-2, 8, 8)

# Construção da propria instrução de erro
class InvalidTriangleError(Exception):
    """Raised when a triangle has invalid sides"""


def calc_square(ab, ac, bc):
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise InvalidTriangleError("One of the sides is less or equal to 0!")

    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))

    return s


square = calc_square(-2, 8, 8)
