def variable_args_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Аргументы переданные в функцию: {args}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@variable_args_decorator
def example_function(*args):
    print("Функция с множеством аргументов")


example_function(1, 2, 3)
