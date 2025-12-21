from decimal import Decimal
from lib.discrete.classes import DiscreteRandomValue


def kolmogorov(d_value: DiscreteRandomValue, F: callable):
    total_n = 0
    for elem in d_value.elements:
        total_n += elem.times

    n = 0
    F_prac = [Decimal(0)]
    for elem in d_value.elements:
        n += elem.times
        F_prac.append(Decimal(n / total_n))

    F_th = [Decimal(0)]
    for elem in d_value.elements:
        F_th.append(F(elem.value))
    F_th.append(Decimal(1))

    print('Fg*|\t ', end='')
    for v in F_prac:
        print(round(v, 4), end=' | ')
    print('\nFg | ', end='')
    for v in F_th:
        print(round(v, 4), end=' | ')

    max_d = Decimal(0)
    for i in range(len(F_prac)):
        d = (F_prac[i] - F_th[i]).copy_abs()
        max_d = max(d, max_d)
        print(f'| {round(F_prac[i], 4)} - {round(F_th[i], 4)} | = {round(d, 4)}')

        d = (F_prac[i] - F_th[i + 1]).copy_abs()
        max_d = max(d, max_d)
        print(f'| {round(F_prac[i], 4)} - {round(F_th[i + 1], 4)} | = {round(d, 4)}')
    print(f'Maximum: {round(max_d, 4)}')