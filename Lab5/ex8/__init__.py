def my_function(*args, **kwargs):
    s = 0
    for k, v in kwargs.items():
        s += v
    return s


myFunc = (lambda *args, **kwargs: sum(kwargs.values()))

print(my_function(1, 2, c=3, d=4))
print(myFunc(1, 2, c=3, d=4))
