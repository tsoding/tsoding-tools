def arrow(x, *fs):
    result = x
    for f in fs:
        result = f(result)
    return result
