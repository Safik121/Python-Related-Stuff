def series_sum(n):
    if n == 1:
        return 1
    else:
        return n + series_sum(n - 1)

print(series_sum(100))
