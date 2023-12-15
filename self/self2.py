def decorator_with_arguments(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@decorator_with_arguments('Аргумент 1', 'Аргумент 2')
def add(x, y):
    return x + y


result = add(3, 5)
print(result)
