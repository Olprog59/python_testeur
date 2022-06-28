if __name__ == '__main__':
    nom_fichier = "test_io.txt"
    with open(nom_fichier, 'r') as fichier:
        for ligne in fichier:
            print(ligne[:10], end='')

    with open(nom_fichier, 'a') as fichier:
        fichier.write('Vive les testeurs\n')
        print('Encore vive les testeurs', file=fichier)
