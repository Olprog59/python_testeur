"""
Créer une fonction qui retourne le prix d'un article avec la réduction.
Ex : 100 € avec une réduction de 20% → la fonction doit retourner le prix de 80€.
1. 1280€ avec 26% de remise
2. 12.2€ avec 9% de remise
3. 5.99€ avec 38% de remise
4. 349.8€ avec 65% de remise
"""


def reduction(prix, reduction):
    if isinstance(prix, (int, float)) and isinstance(reduction, (int, float)):
        return prix - prix * (reduction / 100)
    else:
        raise TypeError('Attention, le type n\'est pas correct.')


if __name__ == '__main__':
    print(reduction(100, 20))
    print(reduction(1280, 26))
    print(reduction(12.2, 9))
    print(reduction(5.99, 38))
    print(reduction(349.8, 65))
