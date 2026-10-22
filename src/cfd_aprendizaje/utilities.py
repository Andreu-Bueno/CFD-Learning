def media_movil_bucle(a):
    b = a.copy()
    for i in range(1, len(a) - 1):
        b[i] = (a[i - 1] + a[i] + a[i + 1]) / 3
    return b


def media_movil(a):
    b = a.copy()
    b[1:-1] = (a[:-2] + a[1:-1] + a[2:]) / 3
    return b

