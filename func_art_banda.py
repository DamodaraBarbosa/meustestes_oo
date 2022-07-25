from random import randint, uniform, choice, randrange

def nome_mpb(probabilidade):
    mpb_masc = [['João', 'José', 'Caetano', 'Chico', 'Baden', 'Vinicius', 'Gilberto', 'Nilton', 'Francisco', 'Marcos', 'Zé', 'Tim'], ['Buarque', 'Belquior', 'Moraes', 
    'Gil', 'Silva', 'Ramalho', 'Maia', 'Powell']]
    mpb_fem = [['Ana', 'Gadú', 'Elis', 'Nara', 'Leão', 'Maísa', 'Maria', 'Cássia', 'Clara', 'Marisa', 'Rita', 'Elza', 'Bia'], 
    ['Calcanhoto', 'Nunes', 'Soares', 'Lee', 'Monte', 'Costa', 'Leão', 'Regina', 'Magalhães', 'Betânia']]
    
    nome_art_banda = list()

    
    if probabilidade <= 30:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 40:
            nome_art_banda.append(choice(mpb_fem[0]))
            if choice(mpb_fem) not in nome_art_banda:
                nome_art_banda.append(choice(mpb_fem[1]))
        else:
            nome_art_banda.append(choice(mpb_fem[0]))
    else:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 40:
            nome_art_banda.append(choice(mpb_masc[0]))
            if choice(mpb_fem) not in nome_art_banda:
                nome_art_banda.append(choice(mpb_masc[1]))
        else:
            nome_art_banda.append(choice(mpb_masc[0]))
    return ' '.join(nome_art_banda[0:])

def nome_pop(probabilidade):
    pop_masc = ['Ed', 'Mayer', 'John', 'Walker', 'Bruno', 'Mars', 'Sheeran', 'Justin', 'Elthon', 'Michael', 'Jackson',
    'James', 'Schimidt', 'Kendall', 'Logan', 'Henderson', 'Harry', 'Styles', 'Mac', 'Malik']
    pop_fem = ['Britney', 'Spears', 'Katy', 'Perry', 'Luísa', 'Sonza', 'Larissa', 'Manu', 'Lady', 'Gaga', 'Nick',
    'Lipa', 'Bey', 'Rita', 'Ora', 'Ariana', 'Grande', 'Billie', 'Carey', 'Selena', 'Gomez', 'Aguilera', 'Kelly', 'Stefani', 'Gwen']

    nome_art_banda = list()

    if probabilidade <= 65:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 55:
            nome_art_banda.append(choice(pop_fem))
            if choice(pop_fem) not in nome_art_banda:
                nome_art_banda.append(choice(pop_fem))
        else:
            nome_art_banda.append(choice(pop_fem))
    else:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 55:
            nome_art_banda.append(choice(pop_masc))
            if choice(pop_masc) not in nome_art_banda:
                nome_art_banda.append(choice(pop_masc))
        else:
                nome_art_banda.append(choice(pop_masc))
    
    return ' '. join(nome_art_banda[0:])

def nome_funk(probabilidade):
    funk_masc = ['G9', 'Brinquedo', 'x9', 'Dav3', 'Kdelas', 'Daz Quebradaz', 'Lucas', 'TX', 'Baixada', 'Daleste',
    'Lon', 'GH', '171', 'John', 'HBox', 'Rocinha', 'Favela', 'XT', 'G20', 'Foda']
    funk_fem = ['Tati', 'Zack', 'Carol', 'Maravilha', 'Julia', 'Pocas', 'Mirela', 'Lud', 'Da Quebrada', 'Da Baixada',
    'Mila', 'Baixinha', 'De Niterói', 'Da Faxada']

    nome_art_banda = list()

    if probabilidade <= 75:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 40:
            nome_art_banda.append(f'MC {choice(funk_masc)}')
            if choice(funk_masc) not in nome_art_banda:
                nome_art_banda.append(choice(funk_masc))
        else:
            nome_art_banda.append(f'MC {choice(funk_masc)}')
    else:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 40:
            nome_art_banda.append(f'MC {choice(funk_fem)}')
            if choice(funk_fem) not in nome_art_banda: 
                nome_art_banda.append(choice(funk_fem))
        else:
            nome_art_banda.append(f'MC {choice(funk_fem)}')
    return ' '. join(nome_art_banda[0:])

def nome_sertanejo(probabilidade):
    sert_masc = [['Bruno', 'Matheus', 'Zezé', 'Gustavo', 'Roger', 'Beto', 'Pablo', 'Walter', 'Fabiano', 'Eduardo'], ['Camargo',  'Lima', 'Barreto', 'Costa', 
    'Menotti', 'Bosco', 'João', 'Kauan', 'Mioto', 'Nathan']]
    sert_fem = [['Simone', 'Simaria', 'Maiara', 'Maraísa', 'Marília', 'Paula', 'Roberta', 'Luana', 'Rafaela', 'Solange', 'Maria'], ['Fernandes', 'Mendonça', 'Miranda',
    'Prado', 'Almeida', 'Fagundes', 'Mattos', 'Viola', 'Pinheiro']]

    nome_art_banda = list()

    if probabilidade <= 65:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 35:
            nome_art_banda.append(f'{choice(sert_masc[0])} &')
            if choice(sert_masc[0]) not in nome_art_banda:
                nome_art_banda.append(choice(sert_masc[0]))
        else:
            nome_art_banda.append(choice(sert_masc[0]))
            nome_art_banda.append(choice(sert_masc[1])) 
    else:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 35:
            nome_art_banda.append(f'{choice(sert_fem[0])} &')
            if choice(sert_fem) not in nome_art_banda:
                nome_art_banda.append(choice(sert_fem[0]))
        else:
            nome_art_banda.append(choice(sert_fem[0]))
            if choice(sert_fem) not in nome_art_banda:
                nome_art_banda.append(choice(sert_fem[1]))
    return ' '.join(nome_art_banda[0:])

def nome_hiphop(probabilidade):
    hiphop = ['Chris', 'Luda', 'Jay', 'Akon', 'Z', 'Steve', 'Knight', 'Eminem', 'Fifty', 'Lil', 'Brown', 'Mac', 'Book',
    'Average', 'Sabotage', 'Tupac', 'Notorious', 'BIG', 'Hill', 'Rakim', 'Lil Nas', 'X', 'Malcom', 'Wayne', 'Sean', 'King']

    nome_art_banda = list()

    if probabilidade <= 40:
        nome_art_banda.append(f'Lil {choice(hiphop)}')
        probabilidade_in = randint(1, 100)
        if probabilidade_in >= 50 and choice(hiphop) not in nome_art_banda:
            nome_art_banda.append(choice(hiphop)) 
    else:
        nome_art_banda.append(choice(hiphop))
        if choice(hiphop) not in nome_art_banda:
            nome_art_banda.append(choice(hiphop))
    return ' '.join(nome_art_banda[0:])

def nome_indie(probabilidade):
    indie_masc = ['Tim', 'Bernardes', 'Rex', 'Orange', 'Mac', 'Marco', 'Steve', 'Lace', 'Kevin', 'Parker', 'Ed',
    'Stones', 'Rock', 'Day', 'Brown', 'Matt', 'John', 'Ken', 'Johnes', 'Kirk']
    indie_fem = ['Claire', 'Brown', 'Max', 'Sharpe', 'Vanessa', 'Lorde', 'Girl', 'Red', 'Dua', 'Aurora', 
    'Bird', 'Lore', 'Del', 'Sun', 'Rey', 'Lana', 'Alice', 'Sharon', 'Gabi']

    nome_arte_banda = list()

    if probabilidade <= 50:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 60:
            nome_arte_banda.append(choice(indie_fem))
            if choice(indie_fem) not in nome_arte_banda:
                nome_arte_banda.append(choice(indie_fem))
        else:
            nome_arte_banda.append(choice(indie_fem))
    else:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 60:
            nome_arte_banda.append(choice(indie_masc))
            if choice(indie_masc) not in nome_arte_banda:
                nome_arte_banda.append(choice(indie_masc))
        else:
            nome_arte_banda.append(choice(indie_masc))
    return ' '.join(nome_arte_banda[0:])

def nome_samba(probabilidade):
    samba_masc = [['Zeca', 'Arlindo', 'Diogo', 'Nogueira', 'Xand', 'Cumpadi', 'Cartola', 'Mumuzinho', 'Tiago', 'Chico', 'Paulinho', 'Noel', 'Marcinho'], ['Cruz', 'Pagodinho', 'Washington','Mané', 'Qualé', 'Jorge', 'Aragão', 'Da Viola', 'Rosa']]
    samba_fem = [['Ana', 'Beth', 'Alcione', 'Carvalho', 'Dona', 'Ivone', 'Teresa', 'Leci', 'Martha', 'Paola', 'Clara', 'Nilze'], ['Lara', 'Cristina', 'Brandão', 'Cristina', 'De Lara', 'Nunes', 'Mariene', 'De Castro']]

    nome_art_banda = list()

    if probabilidade <= 20:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 60:
            nome_art_banda.append(choice(samba_fem[0]))
            nome_art_banda.append(choice(samba_fem[1]))
        else:
            nome_art_banda.append(choice(samba_fem[0]))
    else:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 60:
            nome_art_banda.append(choice(samba_masc[0]))
            nome_art_banda.append(choice(samba_masc[1]))
        else:
            nome_art_banda.append(choice(samba_masc[0]))
    return ' '.join(nome_art_banda[0:])

def nome_eletronica(probabilidade):
    eletronica = ['Fog', 'Sampa', 'Alok', 'David', 'Gueta', 'Snake', 'Chainsmoker', 'Rule', 'Avicii', 'Bambo', 'Vapo',
    'Avek', 'Light', 'Trap', 'Vapo', 'Mathias', 'Yanis', 'Ludaguy', 'Walk', 'Drinker']

    nome_art_banda = list()

    if probabilidade <= 50:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 50:
            nome_art_banda.append(f'DJ {choice(eletronica)}')
            if choice(eletronica) not in nome_art_banda:
                nome_art_banda.append(choice(eletronica))
        else:
            nome_art_banda.append(choice(eletronica))
            if choice(eletronica) not in nome_art_banda:
                nome_art_banda.append(choice(eletronica))
    else:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 50:
            nome_art_banda.append(f'DJ {choice(eletronica)}')
        else:
            nome_art_banda.append(choice(eletronica))
    return ' '.join(nome_art_banda[0:])

def nome_rock(probabilidade):
    rock = ['Beatles', 'Rolling', 'Stones', 'Black', 'Sabath', 'Killers', 'Strokes', 'Tame', 'Impala', 'Guns', 'Roses', 'Pond',
    'Pixies', 'Police', 'Doors', 'Joy', 'Division', 'Led', 'Zepellin', 'Nirvana', 'Queen', 'Iron', 'Maiden', 'Mettalica', 'Pink', 'Floyd',
    'Ramones', 'Bon', 'Jovi', 'Scorpions', 'Kiss', 'Rush', 'Eagles', 'Foo', 'Fighters', 'Linkin', 'Park', 'Slayer', 'Journey', 'Tool']

    nome_art_banda = list()

    if probabilidade <= 35:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 60:
            nome_art_banda.append(f'The {choice(rock)}')
        else:
            nome_art_banda.append(choice(rock))
    else:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 30:
            nome_art_banda.append(f'The {choice(rock)}')
            if choice(rock) not in nome_art_banda:
                nome_art_banda.append(choice(rock))
        else:
            nome_art_banda.append(choice(rock))
            if choice(rock) not in nome_art_banda:
                nome_art_banda.append(choice(rock))
    return ' '.join(nome_art_banda[0:])

def num_fas(genero):
    if genero == 'MPB':
        return (randint(50000, 1000000))
    elif genero == 'Pop':
        return (randint(1000000, 20000000))
    elif genero == 'Funk':
        return (randint(300000, 4000000))
    elif genero == 'Hip hop':
        return (randint(400000, 12000000))
    elif genero == 'Indie':
        return (randint(100000, 3000000))
    elif genero == 'Sertanejo':
        return (randint(500000, 8000000))
    elif genero == 'Samba':
        return (randint(100000, 3000000))
    elif genero == 'Eletrônica':
        return (randint(500000, 5000000))
    else:
        return (randint(6000000, 16000000))

def num_curtidas(genero):
    if genero == 'MPB':
        return (randint(5000, 100000))
    elif genero == 'Pop':
        return (randint(100000, 2000000))
    elif genero == 'Funk':
        return (randint(30000, 400000))
    elif genero == 'Hip hop':
        return (randint(40000, 1200000))
    elif genero == 'Indie':
        return (randint(10000, 300000))
    elif genero == 'Sertanejo':
        return (randint(50000, 800000))
    elif genero == 'Samba':
        return (randint(10000, 300000))
    elif genero == 'Eletrônica':
        return (randint(50000, 500000))
    else:
        return (randint(600000, 1600000))

def num_faturamento(genero):
    if genero == 'MPB':
        return f'USD{(uniform(50000, 1000000))}/ano'
    elif genero == 'Pop':
        return f'USD {(randint(100000, 20000000)):.2f}/ano'
    elif genero == 'Funk':
        return f'USD {(randint(300000, 4000000)):.2f}/ano'
    elif genero == 'Hip hop':
        return f'USD {(randint(400000, 12000000)):.2f}/ano'
    elif genero == 'Indie':
        return f'USD {(randint(100000, 3000000)):.2f}/ano'
    elif genero == 'Sertanejo':
        return f'USD {(randint(500000, 8000000)):.2f}/ano'
    elif genero == 'Samba':
        return f'USD {(randint(100000, 3000000)):.2f}/ano'
    elif genero == 'Eletrônica':
        return f'USD {(randint(500000, 5000000)):.2f}/ano'
    else:
        return f'USD {(randint(600000, 16000000)):.2f}/ano'