import math


def get_coefficients(a, b, c):
    delta = int(b) ** 2 - 4 * a * int(c)

    if delta > 0:
        x1 = (int(-b) + math.sqrt(delta)) / (2 * int(a))
        x2 = (-b - math.sqrt(delta)) / (2 * int(a))
        return x1, x2
    elif delta == 0:
        x = int(-b) / (2 * int(a))
        return x
    else:
        return "Nu există soluții reale"

# print(get_coefficients())
