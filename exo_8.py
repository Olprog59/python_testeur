def demander_nom():
    nom = input('Entrez le nom : ')
    prenom = input('Entrez le prénom : ')

    return prenom.capitalize() + ' ' + nom.upper()


if __name__ == '__main__':
    nb_str = input('Combien de nom souhaites-tu rentrer ? ')
    nb = int(nb_str)

    names = []
    for i in range(nb):
        names.append(demander_nom())

    print(names)
