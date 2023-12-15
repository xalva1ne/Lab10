class ClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("До")
        result = self.func(*args, **kwargs)
        print("После")
        return result

@ClassDecorator
def hello(name):
    print(f"Привет, {name}!")

# Использование
hello("Мир")
