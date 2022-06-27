if __name__ == '__main__':
    nombres = [154, 2145, -32, 468, 3, -9, 468, -1, -78, 164, 3, -4567, 9876, 16465]

    max = min = somme = nombres[0]

    for nb in nombres[1:]:
        if nb > max:
            max = nb
        if nb < min:
            min = nb
        somme += nb
    else:
        print(f'La valeur de min est {min}')
        print(f'La valeur de max est {max}')
        print(f'La somme est {somme}')
        # print(f'La moyenne est {somme / len(nombres)}')
        print('La moyenne est %.4f' % (somme / len(nombres)))

    # for i in range(1, len(nombres)):
    #     if nombres[i] > max:
    #         max = nombres[i]
    #
    #     if nombres[i] < min:
    #         min = nombres[i]
    #
    #     somme += nombres[i] # somme = somme + nombres[i]
    # else:
    #     print(f'La valeur de min est {min}')
    #     print(f'La valeur de max est {max}')
    #     print(f'La somme est {somme}')
    #     # print(f'La moyenne est {somme / len(nombres)}')
    #     print('La moyenne est %.4f' % (somme / len(nombres)))
