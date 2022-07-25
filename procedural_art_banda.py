from random import randint, uniform, choice, randrange
from func_art_banda import nome_eletronica, nome_funk, nome_hiphop, nome_indie, nome_mpb, nome_pop, nome_rock, nome_samba, nome_sertanejo

art_banda = dict()
catalogo = list()

genero = ['MPB', 'Rock', 'Indie', 'Funk', 'Sertanejo', 'Hip hop', 'Samba', 'Pop', 'Eletrônica']
genero_random = choice(genero)
# print(genero_random)

if genero_random == 'MPB':
    print(nome_mpb(randint(1, 100)))
elif genero_random == 'Pop':
    print(nome_pop(randint(1, 100)))
elif genero_random == 'Funk':
    print(nome_funk(randint(1, 100)))
elif genero_random == 'Hip hop':
    print(nome_hiphop(randint(1, 100)))
elif genero_random == 'Indie':
    print(nome_indie(randint(1, 100)))
elif genero_random == 'Sertanejo':
    print(nome_sertanejo(randint(1, 100)))
elif genero_random == 'Samba':
    print(nome_samba(randint(1, 100)))
elif genero_random == 'Eletrônica':
    print(nome_eletronica(randint(1, 100)))
else:
    print(nome_rock(randint(1, 100)))