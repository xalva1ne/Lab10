def simple_decorator(func):
    def wrapper():
        print("До")
        func()
        print("После")
    return wrapper


@simple_decorator
def say_hello():
    print("Привет!")


say_hello()
