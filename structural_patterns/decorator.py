from functools import wraps


def decorator_1(func):
    def runs_func():
        print("decorator_1 - no wrapper")
        func()

    return runs_func


def decorator_2(func):
    @wraps(func)
    def runs_func():
        print("decorator_2 - Use wrapper")
        func()

    return runs_func


@decorator_1
def func_1():
    print("func_1 run!")


@decorator_2
def func_2():
    print("func_2 run!")


# execute

func_1()
print("func_1 name: ", func_1.__name__)
print("func_1 doc: ", func_1.__doc__)

print("-" * 50)

func_2()
print("func_2 name: ", func_2.__name__)
print("func_2 doc: ", func_2.__doc__)

print("-" * 50)
print("-" * 50)

deco_func_1 = decorator_1(func_1)
deco_func_1()

print("-" * 50)

deco_func_2 = decorator_1(func_2)
deco_func_2()
