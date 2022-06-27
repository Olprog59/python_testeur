if __name__ == '__main__':

    nb_personnes = input("Combien de personnes souhaites-tu enregistrer ? ")
    if nb_personnes.isdecimal():
        nb_personnes = int(nb_personnes)

        liste_nom = []
        i = 0
        while i < nb_personnes:
            prenom = input('Indiquez votre prénom ')
            if not prenom.isalpha():
                print('Attention il y a autre chose que des caractères.')
                continue

            nom = input('Indiquez votre nom ')
            if not nom.isalpha():
                print('Attention il y a autre chose que des caractères.')
                continue

            liste_nom.append(prenom.capitalize() + ' ' + nom.upper())
            i += 1

        else:
            print(liste_nom)