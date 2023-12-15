from functools import wraps


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Происходит вызов декорируемой функции")
        return f(*args, **kwargs)
    return wrapper


@my_decorator
def example():
    """Документация"""
    print("Я функция пример")


example()
print(example.__name__)
print(example.__doc__)
