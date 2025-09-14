from decimal import Decimal
from dataclasses import dataclass


@dataclass
class Element:
    probability: Decimal
    value: Decimal
    times: int


@dataclass
class Interval:
    start: Decimal | None
    stop: Decimal | None
    size: Decimal


class DiscreteRandomValue:
    def __init__(self, elements: list[Element]):
        if len(elements) == 0:
            raise ValueError("Empty elements")
        self.elements = elements
        self.elements_num = len(elements)


def discrete_value_from_results(results: list) -> DiscreteRandomValue:
    for i in range(len(results)):
        results[i] = Decimal(results[i])
    result = {}
    for value in results:
        if value in result.keys():
            result[value] += 1
        else:
            result[value] = 1
    elements: list[Element] = []
    for value, times in result.items():
        elements.append(
            Element(
                probability=Decimal(times) / len(results),
                value=value,
                times=times
            )
        )
    elements = sorted(elements, key=lambda elem: elem.value)
    return DiscreteRandomValue(elements=elements)
