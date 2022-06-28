def nb_moyenne(notes):
    if type(notes) == list:
        # for i in range(len(notes)):
        count = 0
        for note in notes:
            if note > 10:
                count += 1

        return count
    else:
        raise TypeError('Attention, le type passé en argument n\'est pas une liste.')


if __name__ == '__main__':
    notes = [17, 14, 8, 16, 0, 19, 5, 7, 12, 15]
    n = nb_moyenne(notes)
    print(f'Nous avons {n} note(s) au dessus de la moyenne.')
