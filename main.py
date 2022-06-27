if __name__ == '__main__':
    x = y = 19
    print(x, y, sep=' | ', end='.')

    # assert x == y
    # assert x != y

    reponse = input('Quel est ton age ?')
    print(reponse, type(reponse))

    age = int(reponse)
    print(age, type(age))

    # la concaténation ne peut se faire qu'avec le type 'str'
    print('Votre age est de ' + str(age) + ' ans')
    print(f'Votre age est de {age} ans')
    print('Votre age est de {0} ans. {1}'.format(age, x))
    print('Votre age est de %.2f ans' % age)
    """
    int -> entier
    float -> réel
    str -> chaine de caractères
    booléen -> bool
    """
