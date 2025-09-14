from lib.discrete.summary import show_summary
from decimal import Decimal

results = [
    '0.9', '0.9', '1.0', '0.4', '0.7', '1.0', '0.8', '0.7', '0.1', '1.0',
    '0.9', '0.2', '0.8', '0.2', '0.5', '0.8', '0.7', '0.6', '0.2', '0.8',
    '0.2', '0.6', '0.9', '0.7', '1.0', '0.2', '0.1', '0.0', '0.6', '0.3'
]

show_summary(results=results)
