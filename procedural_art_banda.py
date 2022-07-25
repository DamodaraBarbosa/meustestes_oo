from random import randint, uniform, choice, randrange

from matplotlib import artist
from func_art_banda import nome_eletronica, nome_funk, nome_hiphop, nome_indie, nome_mpb, nome_pop, nome_rock, nome_samba, nome_sertanejo, num_curtidas, num_fas, num_faturamento

art_banda = dict()
catalogo = list()


for contador in range(1, 21):
    generos = ['MPB', 'Rock', 'Indie', 'Funk', 'Sertanejo', 'Hip hop', 'Samba', 'Pop', 'Eletrônica']
    genero_random = choice(generos)

    if genero_random == 'MPB':
        art_banda['nome'] = nome_mpb(randint(1, 100))
        art_banda['gênero'] = 'MPB'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Pop':
        art_banda['nome'] = nome_pop(randint(1, 100))
        art_banda['gênero'] = 'Pop'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Funk':
        art_banda['nome'] = nome_funk(randint(1, 100))
        art_banda['gênero'] = 'Funk'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Hip hop':
        art_banda['nome'] = nome_hiphop(randint(1, 100))
        art_banda['gênero'] = 'Hip hop'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Indie':
        art_banda['nome'] = nome_indie(randint(1, 100))
        art_banda['gênero'] = 'Indie'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Sertanejo':
        art_banda['nome'] = nome_sertanejo(randint(1, 100))
        art_banda['gênero'] = 'Sertanejo'
        if '&' in art_banda['nome']:
            art_banda['tipo'] = 'Dupla'
        else:
            art_banda['tipo'] = 'Solo'
    elif genero_random == 'Samba':
        art_banda['nome'] = nome_samba(randint(1, 100))
        art_banda['gênero'] = 'Samba'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Eletrônica':
        art_banda['nome'] = nome_eletronica(randint(1, 100))
        art_banda['gênero'] = 'Eletrônica'
        art_banda['tipo'] = 'Solo'
    else:
        art_banda['nome'] = nome_rock(randint(1, 100))
        art_banda['gênero'] = 'Rock'
        art_banda['tipo'] = 'Banda'

    art_banda['fãs'] = num_fas(genero_random)
    art_banda['curtidas'] = num_curtidas(genero_random)
    art_banda['faturamento'] = num_faturamento(genero_random)
    catalogo.append(art_banda.copy())

texto = ''
arquivo = open('dados_catalogo.txt', 'w')

for index, artistas in enumerate(catalogo):
    linha_art_banda = ''
    linha_art_banda += (f"conta{index+1} = ('{artistas['nome']}', '{artistas['gênero']}', '{artistas['tipo']}', {artistas['fãs']}, {artistas['curtidas']}, {artistas['faturamento']})")
    linha_art_banda += '\n'
    texto += linha_art_banda
arquivo.writelines(texto)