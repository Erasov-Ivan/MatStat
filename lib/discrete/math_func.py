from lib.discrete.classes import *


def get_results_average(d_value: DiscreteRandomValue) -> Decimal:
    """Выборочное среднее"""
    return Decimal(sum(map(lambda elem: elem.probability * elem.value, d_value.elements)))


def get_dispersion(d_value: DiscreteRandomValue) -> Decimal:
    """Дисперсия"""
    ra = get_results_average(d_value=d_value)
    dispersion = sum(map(lambda elem: ((elem.value - ra) ** 2) * elem.times, d_value.elements)) / sum(map(lambda elem: elem.times, d_value.elements))
    return Decimal(dispersion)


def get_right_dispersion(d_value: DiscreteRandomValue) -> Decimal:
    """Исправленная дисперсия"""
    if len(d_value.elements) <= 1:
        raise Exception('Not enough elements')
    ra = get_results_average(d_value=d_value)
    dispersion = sum(map(lambda elem: ((elem.value - ra) ** 2) * elem.times, d_value.elements)) / (sum(map(lambda elem: elem.times, d_value.elements)) - 1)
    return Decimal(dispersion)


def get_empirical_distribution_func_table(d_value: DiscreteRandomValue) -> list[Interval]:
    """Эмпирическая функция распределения (таблица)"""
    result: list[Interval] = []
    for i in range(len(d_value.elements)):
        probability = Decimal(0)
        for j in range(i):
            probability += d_value.elements[j].probability
        result.append(
            Interval(
                start=d_value.elements[i-1].value if i > 0 else None,
                stop=d_value.elements[i].value,
                size=probability
            )
        )
    result.append(
        Interval(
            start=d_value.elements[-1].value,
            stop=None,
            size=Decimal(1)
        )
    )
    return result


def get_histogram_interval_size(d_value: DiscreteRandomValue) -> Decimal:
    diff = d_value.elements[-1].value - d_value.elements[0].value
    while int(diff) != diff:
        diff *= 10

    intervals_num = 5
    for delimiter in range(6, d_value.elements_num + 1):
        if diff % delimiter == 0:
            intervals_num = delimiter
    diff = d_value.elements[-1].value - d_value.elements[0].value
    interval_size = Decimal(diff / intervals_num)
    return interval_size
