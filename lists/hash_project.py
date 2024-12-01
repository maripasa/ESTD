from itertools import product
from functools import reduce

def fold(x):
    num = str(x)
    if len(num) <= 2:
        return x % 32
    if len(num) % 2 != 0:
        num = "0" + num
    num = str((int(num[1]) + int(num[2])) % 10) + str((int(num[0]) + int(num[3])) % 10) + num[4:]
    return fold(int(num))

keys = ["apple", "voadora", "banjo", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "xuru", "runin", "xamã", "mirtilho", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "voavanga", "maravilha", "IFCE", "maracanaú", "ceará", "manga", "rendemption", "bobo", "maluco"]

hash_functions = [
    ('sum', lambda x: sum(ord(c) for c in x)),
    ('polynomial', lambda x: sum(ord(c) * (31 ** i) for i, c in enumerate(reversed(x)))),
    ('shift', lambda x: reduce(lambda h, c: ((h << 1) & 0xFFFFFFFF) | (h >> 31) + ord(c), x, 0))
]

compression_functions = [
    ('division', lambda x: x % 32),
    ('fold', fold),
    ('mad', lambda x: (17 * x + 11) % 83 % 32)
]

results = {}
for (h_name, h_func), (c_name, c_func) in product(hash_functions, compression_functions):
    results[(h_name, c_name)] = len(keys) - len({c_func(h_func(key)) for key in keys})

for (h, c), v in sorted(results.items(), key=lambda x: x[1], reverse=True):
    print(f"{h}, {c}: {v}")
