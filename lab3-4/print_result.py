def print_result(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        if isinstance(a, list):
            for i in args: print(args)
        elif isinstance(a, dict):
            for i, j in a.items():
                print(i, " = ", j)
        else:
            print(a)
        return a
    return wrapper
