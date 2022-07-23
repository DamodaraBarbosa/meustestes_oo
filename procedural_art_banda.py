from random import randint, uniform, choice, randrange

from scipy import rand
from func_art_banda import nome_funk, nome_hiphop, nome_mpb, nome_pop

art_banda = dict()
catalogo = list()

genero = ['MPB', 'Rock', 'Indie', 'Funk', 'Sertanejo', 'Hip hop', 'Samba', 'Pop', 'Eletrônica']
genero_random = choice(genero)
print(genero_random)

if genero_random == 'MPB':
    print(nome_mpb(randint(1, 100)))
elif genero_random == 'Pop':
    print(nome_pop(randint(1, 100)))
elif genero_random == 'Funk':
    print(nome_funk(randint(1, 100)))
elif genero_random == 'Hip hop':
    print(nome_hiphop(randint(1, 100)))
    
