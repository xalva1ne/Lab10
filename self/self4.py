from functools import wraps


def docstring_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Документация декоратора"""
        return func(*args, **kwargs)
    return wrapper


@docstring_decorator
def decorated_function():
    """Документация функции"""
    pass


print(decorated_function.__doc__)
