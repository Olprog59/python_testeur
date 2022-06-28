def entree():
    entry = input('Entrez votre nom : ')
    if entry.isalpha():
        return entry
    else:
        raise ValueError('Le nom ne peut comporter que des lettres alphabétiques.')


if __name__ == '__main__':
    try:
        nom = entree()
        print(nom)
    except ValueError as v:
        print(v)
    finally:
        print("coucou")
