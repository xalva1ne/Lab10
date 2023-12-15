def repeat(strings):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for string in range(strings):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(strings=3)
def say_hi():
    print("Привет!")


say_hi()
