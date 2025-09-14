from decimal import Decimal
import math


def stergess_func(minimum: Decimal, maximum, Decimal, n: int) -> Decimal:
    return (maximum - minimum) / (1 + Decimal('3.322') * math.log(float(n), 10))

