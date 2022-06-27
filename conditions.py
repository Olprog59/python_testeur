
if __name__ == '__main__':

    resultat = None
    n = 10

    if n > 0:
        resultat = 'positif'
    elif n < 0:
        resultat = "negatif"
    else:
        resultat = 'nul'

    print(resultat)

    if n > 0 and n < 100:
        print('Le numéro est compris entre 0 et 100')

    if not resultat == 'nul':
        print('Resultat n\'est pas nul')

    if resultat == 'positif' or resultat == 'negatif':
        print('Le résultat est négatif ou positif')

    # déterminer si n est pair ou impair
    if n % 2 == 0:
        print(f'{n} est pair')
    else:
        print(f'{n} est impair')

    # Demander à l'utilisateur son age et indiquez s'il est :
    # - un adulte
    # - un adolescent (12 à 18)
    # - un enfant
    response = input('Quel est votre age ? ')
    age = int(response)
    if age >= 18:
        print('Vous êtes un adulte.')
    elif age >= 12:
        print('Vous êtes un adolescent.')
    else:
        print('Vous êtes un enfant.')

