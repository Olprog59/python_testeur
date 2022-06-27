def boucle_while():
    n = 10
    somme = 0
    i = 1

    while i <= n:
        # somme = somme + i
        # i = i + 1
        somme += i
        i += 1

    print(f'La somme des entiers de 1 à {n} est : {somme}')


if __name__ == '__main__':
    # boucle_while()
    n = 10
    somme = 0

    for i in range(1, n+1, 1):
        # somme = somme + i
        somme += i

    print(f'La somme des entiers de 1 à {n} est : {somme}')

    for i in range(20):
        if i % 2 == 0:
            print(f'{i} est pair')
            continue
        print(f'{i} est impair')
        if i == 11:
            break
    else:
        print('Je suis passé par else')

    prenoms = ['sam', 'sab', 'pat']
    prenoms.append('mick')
    prenoms[1] = 'Sabrina'
    print(prenoms)

