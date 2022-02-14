def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(2, 3, 9, 8)

def calc(**kwargs):
    print(kwargs)


calc(add=3, multiply=5)
