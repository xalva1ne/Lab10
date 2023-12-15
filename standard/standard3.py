class MyClass:
    class_variable = 10

    @classmethod
    def print_class_variable(cls):
        print(cls.class_variable)


MyClass.print_class_variable()
