from contextlib import contextmanager


@contextmanager
def my_context():
    print("Вход")
    yield
    print("Выход")


with my_context():
    print("Внутренность")
