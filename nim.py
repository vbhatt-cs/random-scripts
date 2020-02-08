import numpy as np

n = 25
wins = np.zeros(n + 1, dtype=np.int) - 1
acts = np.zeros(n + 1, dtype=np.int) - 1
wins[0] = 0


def get_child(x):
    actions = np.array([1, 3, 4])
    c = x - actions
    return c[c >= 0]


for i in range(1, n + 1):
    children = get_child(i)
    wins[i] = 0
    for ch in children:
        if wins[ch] == 0:
            wins[i] = 1
            acts[i] = ch

assert all(wins != -1)

i = 25
print("Win:", wins[i])
