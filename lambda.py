def myfunc(x):
    return lambda n : n + x

new_century = myfunc(100)
print(new_century(2000))

