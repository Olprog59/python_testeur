def demander(chaine):
    n = input(f'Entrez votre {chaine} : ')
    if n.isalpha():
        return n
    else:
        raise ValueError('Il ne faut que des caractères alphabétiques.')


def demander_number(chaine, type_number='int'):
    n = input(f'Entrez votre {chaine} : ')
    if isfloat(n) and type_number == 'float':
        return float(n)
    elif n.isdecimal():
        return int(n)
    else:
        raise ValueError('Il ne faut que des caractères numériques.')


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    a = demander_number('poids', type_number='float')
    print(type(a))

