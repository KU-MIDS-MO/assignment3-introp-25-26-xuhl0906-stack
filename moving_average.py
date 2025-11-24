import numpy as np

def moving_average(signal, window_size):
    ### Replace with your own code (begin) ###
    signal = np.array(signal, dtype=float)
    n = len(signal)
    result = np.zeros(n)
    k = (window_size - 1) // 2

    for i in range(n):
        left = max(0, i - k)
        right = min(n - 1, i + k)
        window = signal[left : right + 1]
        result[i] = sum(window) / len(window)

    return result
    ### Replace with your own code (end)   ###

