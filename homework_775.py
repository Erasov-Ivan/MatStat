from lib.discrete import classes, math_func, vizual_func
from decimal import Decimal
import plotly.graph_objects as go

data_775_1 = [
    14.58, 14.47, 14.43, 14.42,
    14.35, 13.95, 14.56, 14.36,
    14.33, 14.18, 14.34, 14.28,
    14.54, 14.66, 14.38, 14.20,
    14.24, 14.35, 14.56, 14.48,
    14.42, 14.50, 14.32, 14.66,
    14.58, 14.69, 14.41, 14.64,
    14.47, 14.54, 14.14, 14.73,
    14.54, 14.48, 14.29, 14.43,
    14.24, 14.36, 14.31, 14.28,
    14.38, 14.50, 14.30, 14.64,
    14.7, 14.43, 14.28, 14.72,
    14.47, 14.46, 14.51, 14.35,
    14.49, 14.56, 14.37, 14.60,
    14.28, 14.48, 14.14, 14.46
]

data_775_2 = [
    14.50, 14.46, 14.53, 14.30,
    14.35, 14.36, 14.23, 14.38,
    14.69, 14.38, 14.55, 14.55,
    14.60, 14.40, 14.51, 14.36,
    14.54, 14.38, 14.25, 14.24,
    14.42, 14.35, 14.11, 14.23,
    14.68, 14.16, 14.44, 14.16,
    14.54, 14.51, 14.51, 14.17,
    14.55, 14.50, 14.55, 14.37,
    14.33, 14.50, 14.24, 14.38,
    14.56, 14.48, 14.31, 14.46,
    14.36, 14.53, 14.46, 14.12,
    14.36, 14.25, 14.36, 14.28,
    14.15, 14.48, 14.39, 14.23,
    14.48, 14.36, 14.30, 14.38
]

interval_size = Decimal('0.15')
value_775_1 = classes.discrete_value_from_results(results=data_775_1)
value_775_2 = classes.discrete_value_from_results(results=data_775_2)

shared_data = data_775_1 + data_775_2
shared_value = classes.discrete_value_from_results(results=shared_data)

intervals_775_1 = vizual_func.elements_to_same_intervals(
    elements=value_775_1.elements, interval_size=interval_size, start=shared_value.elements[0].value - interval_size / 2
)
bars_775_1 = vizual_func.intervals_to_bars_scatter(intervals=intervals_775_1, color='red', opacity=0.75)

intervals_775_2 = vizual_func.elements_to_same_intervals(
    elements=value_775_2.elements, interval_size=interval_size, start=shared_value.elements[0].value - interval_size / 2
)
bars_775_2 = vizual_func.intervals_to_bars_scatter(intervals=intervals_775_2, color='green', opacity=0.75)


fig = go.Figure(
    data=[bars_775_1, bars_775_2]
)
fig.show()
