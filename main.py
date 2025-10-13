from lib.discrete.summary import show_summary
from decimal import Decimal

res = {
    0: 28,
    1: 47,
    2: 81,
    3: 67,
    4: 53,
    5: 24,
    6: 13,
    7: 8,
    8: 3,
    9: 2,
    10: 1
}

result = []
for key, value in res.items():
    for i in range(value):
        result.append(key)
show_summary(results=result)
