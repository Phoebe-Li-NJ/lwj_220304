print(7%(7//2))
print(7//2)
print(7/2)

def func1():
    return [lambda x:i*x for i in range(4)]

print([m(2) for m in func1()])