from lib.discrete import classes, math_func, vizual_func
from plotly.subplots import make_subplots
from decimal import Decimal


def show_summary(results: list, histogram_interval_size: Decimal | None = None):
    d_value = classes.discrete_value_from_results(results=results)
    print('Группированная выборка')
    for element in d_value.elements:
        print(element.value, '\t|\t', element.times)


    result_average = math_func.get_results_average(d_value=d_value)
    print(f'\nВыборочное среднее:     {result_average}')

    dispersion = math_func.get_dispersion(d_value=d_value)
    print(f'Дисперсия:              {dispersion}')

    right_dispersion = math_func.get_right_dispersion(d_value=d_value)
    print(f'Исправленная дисперсия: {right_dispersion}')

    empiric_func_table = math_func.get_empirical_distribution_func_table(d_value=d_value)
    print('\nЭмпирическая функция распределения')
    vizual_func.print_empirical_distribution_func(intervals=empiric_func_table)

    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=(
            'Функция распределения',
            'Гистограмма',
            'Полигон',
        ),
        vertical_spacing=0.08,
        row_heights=[1, 1, 1],
        shared_xaxes=True
    )
    distribution_func = vizual_func.get_empirical_distribution_func(intervals=empiric_func_table, color='blue')
    fig.add_trace(distribution_func, row=1, col=1)

    if histogram_interval_size is None:
        histogram_interval_size = math_func.get_histogram_interval_size(d_value=d_value)
        print(f'\nРассчитанный размер интервала для гистограммы: {histogram_interval_size}')
    intervals = vizual_func.elements_to_same_intervals(elements=d_value.elements, interval_size=histogram_interval_size)

    print('Интервалы:')
    for interval in intervals:
        print(f'{interval.start} | {interval.stop} | {interval.size}')

    bars = vizual_func.intervals_to_bars_scatter(intervals=intervals)
    fig.add_trace(bars, row=2, col=1)

    poligonom = vizual_func.discrete_value_to_poligonom(d_value=d_value, color='blue')
    fig.add_trace(poligonom, row=3, col=1)

    fig.show()
