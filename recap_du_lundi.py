

if __name__ == '__main__':
    x = 34
    print(type(x), id(x), x)

    if x > 10 and x < 40:
        print(x)
    elif x > 50:
        print(x)
    else:
        print(x, sep=' | ', end='-')

    assert x == 34

    while x >= 0:
        print(x ** 2)
        x -= 1

    while True:
        print("coucou")
        x += 1
        if x == 3:
            continue
        if x == 10:
            break
        print(x)

    for i in range(2, 10, 3):
        print(i)
    else:
        print("Tout s'est bien passé!! 👍")
