from lib.discrete.classes import *
import plotly.graph_objects as go
from prettytable import PrettyTable


def elements_to_same_intervals(
        elements: list[Element], interval_size: Decimal, start: Decimal = None
) -> list[Interval]:
    result: list[Interval] = []
    if start is None:
        start = elements[0].value - interval_size / 2
    while start < elements[-1].value:
        result.append(
            Interval(
                start=start,
                stop=start + interval_size,
                size=Decimal(0)
            )
        )
        start += interval_size
    for element in elements:
        for i in range(len(result)):
            if result[i].start <= element.value < result[i].stop:
                result[i].size += element.times
                break
    return result


def intervals_to_bars_scatter(intervals: list[Interval], color: str = 'blue', opacity: float = 1) -> go.Scatter:
    x_list = []
    y_list = []
    for interval in intervals:
        x_list += [
            interval.start,
            interval.start,
            interval.stop,
            interval.stop,
            None
        ]
        y_list += [
            0,
            interval.size,
            interval.size,
            0,
            None
        ]
    scatter = go.Scatter(
        x=x_list,
        y=y_list,
        fill="toself",
        fillcolor=color,
        opacity=opacity,
        line={'width': 2, 'color': 'black'}
    )
    return scatter


def discrete_value_to_poligonom(d_value: DiscreteRandomValue, color: str = 'black') -> go.Scatter:
    x = []
    y = []
    # x.append(d_value.elements[0].value)
    # y.append(0)
    for element in d_value.elements:
        x.append(element.value)
        y.append(element.times)
    # x.append(d_value.elements[-1].value)
    # y.append(0)
    return go.Scatter(
        x=x,
        y=y,
        marker=dict(
            color=color
        )
    )


def get_empirical_distribution_func(intervals: list[Interval], color: str='black') -> go.Scatter:
    x = []
    y = []
    diff = intervals[-1].start - intervals[0].stop
    intervals[0].start = intervals[0].stop - diff / len(intervals)
    intervals[-1].stop = intervals[-1].start + diff / len(intervals)
    for interval in intervals:
        x.append(interval.start)
        x.append(interval.stop)
        x.append(None)
        y.append(interval.size)
        y.append(interval.size)
        y.append(None)
    scatter = go.Scatter(
        x=x,
        y=y,
        marker=dict(
            color=color
        )
    )
    return scatter


def print_empirical_distribution_func(intervals: list[Interval], precision: int = 5):
    """Выводит в консоль табличку эмпирической функции распределения"""
    table = PrettyTable(field_names=['Х', 'Вероятность'])
    for interval in intervals:
        table.add_row(
            [
                f'{"(-∞" if interval.start is None else "[" + str(interval.start)}; {interval.stop if interval.stop is not None else "∞"})',
                format(round(interval.size, precision), 'f')
            ]
        )
    print(table)
