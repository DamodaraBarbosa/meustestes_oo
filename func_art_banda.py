from random import randint, uniform, choice, randrange

def nome_mpb(probabilidade):
    mpb_masc = ['João', 'José', 'Caetano', 'Chico', 'Buarque', 'Belquior', 'Caetano', 'Baden', 'Vinicius', 'Moraes',
    'Gilberto', 'Gil', 'Silva', 'Nilton', 'Francisco', 'Marcos', 'Zé', 'Ramalho', 'Maia', 'Tim']
    mpb_fem = ['Ana', 'Gadú', 'Magalhães', 'Betânia', 'Elis', 'Regina', 'Calcanhoto', 'Nara', 'Leão', 'Maísa', 'Maria',
    'Cássia', 'Clara', 'Costa', 'Marisa', 'Monte', 'Rita', 'Elza', 'Soares', 'Bia', 'Nunes']
    # indie_masc = ['Tim', 'Bernardes', 'Rex', 'Orange', 'Mac', 'Marco', 'Steve', 'Lace', 'Kevin', 'Parker', 'Ed',
    # 'Stones', 'Rock', 'Day', 'Brown', 'Matt', 'John', 'Ken', 'Johnes', 'Kirk']
    # indie_fem = ['Claire', 'Brown', 'Max', 'Sharpe', 'Vanessa', 'Lorde', 'Girl', 'Red', 'Dua', 'Lorde', 'Aurora', 
    # 'Bird', 'Lore', 'Del', 'Sun', 'Rey', 'Lana', 'Alice', 'Sharon', 'Gabi']
    # sert_masc = ['Bruno', 'Camargo', 'Matheus', 'Zezé', 'Gustavo', 'Lima', 'Roger', 'Beto', 'Barreto', 'Pablo', 'Costa',
    # 'Eduardo', 'Walter', 'Fabiano', 'Menotti', 'Bosco', 'João', 'Kauan', 'Mioto', 'Nathan']
    # sert_fem = ['Simone', 'Simaria', 'Maiara', 'Maraísa','Fernandes', 'Mendonça', 'Marília', 'Paula', 'Roberta', 'Miranda',
    # 'Prado', 'Luana', 'Almeida', 'Solange', 'Maria', 'Fagundes', 'Mattos', 'Rafaela', 'Viola', 'Pinheiro']
    # hiphop = ['Chris', 'Luda', 'Jay', 'Akon', 'Z', 'Steve', 'Knight', 'Eminem', 'Fifty', 'Lil', 'Brown', 'Mac', 'Book',
    # 'Average', 'Sabotage', 'Tupac', 'Notorious', 'BIG', 'Hill', 'Rakim', 'Lil Nas', 'X', 'Malcom', 'Wayne', 'Sean', 'King']
    # samba_masc = ['Zeca', 'Arlindo', 'Diogo', 'Nogueira', 'Pagodinho', 'Xand', 'Cumpadi', 'Washington', 'Cartola', 'Cruz',
    # 'Mumuzinho', 'Tiago', 'Chico', 'Mané', 'Qualé', 'Jorge', 'Aragão', 'Paulinho', 'Da Viola', 'Noel', 'Rosa', 'Marcinho']
    # samba_fem = ['Ana', 'Beth', 'Alcione', 'Carvalho', 'Dona', 'Ivone', 'Lara', 'Teresa', 'Cristina', 'Leci', 'Brandão', 'Cristina',
    # 'Matha', 'Paola', 'De Lara', 'Clara', 'Nunes', 'Mariene', 'De Castro', 'Nilze']
    # eletronica = ['Fog', 'Sampa', 'Alok', 'David', 'Gueta', 'Snake', 'Chainsmoker', 'Rule', 'Avicii', 'Bambo', 'Vapo',
    # 'Avek', 'Light', 'Trap', 'Vapo', 'Mathias', 'Yanis', 'Ludaguy', 'Walk', 'Drinker']
    # rock = ['Beatles', 'Rolling', 'Stones', 'Black', 'Sabath', 'Killers', 'Strokes', 'Tame', 'Impala', 'Guns', 'Roses', 'Pond',
    # 'Pixies', 'Police', 'Doors', 'Joy', 'Division', 'Led', 'Zepellin', 'Nirvana', 'Queen', 'Iron', 'Maiden', 'Mettalica', 'Pink', 'Floyd',
    # 'Ramones', 'Bon', 'Jovi', 'Scorpions', 'Kiss', 'Rush', 'Eagles', 'Foo', 'Fighters', 'Linkin', 'Park', 'Slayer', 'Journey', 'Tool']

    nome_art_banda = list()

    
    if probabilidade <= 30:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 40:
            nome_art_banda.append(choice(mpb_fem))
            if choice(mpb_fem) not in nome_art_banda:
                nome_art_banda.append(choice(mpb_fem))
        else:
            nome_art_banda.append(choice(mpb_fem))
    else:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 40:
            nome_art_banda.append(choice(mpb_masc))
            if choice(mpb_fem) not in nome_art_banda:
                nome_art_banda.append(choice(mpb_masc))
        else:
            nome_art_banda.append(choice(mpb_masc))
    return ' '. join(nome_art_banda[0:])

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
    sert_masc = ['Bruno', 'Camargo', 'Matheus', 'Zezé', 'Gustavo', 'Lima', 'Roger', 'Beto', 'Barreto', 'Pablo', 'Costa',
    'Eduardo', 'Walter', 'Fabiano', 'Menotti', 'Bosco', 'João', 'Kauan', 'Mioto', 'Nathan']
    sert_fem = ['Simone', 'Simaria', 'Maiara', 'Maraísa','Fernandes', 'Mendonça', 'Marília', 'Paula', 'Roberta', 'Miranda',
    'Prado', 'Luana', 'Almeida', 'Solange', 'Maria', 'Fagundes', 'Mattos', 'Rafaela', 'Viola', 'Pinheiro']

    nome_art_banda = list()

    if probabilidade <= 65:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 35:
            nome_art_banda.append(f'{choice(sert_masc)} &')
            if choice(sert_masc) not in nome_art_banda:
                nome_art_banda.append(choice(sert_masc))
        else:
            nome_art_banda.append(choice(sert_masc))
            if choice(sert_masc) not in nome_art_banda:
                nome_art_banda.append(choice(sert_masc))
    else:
        probabilidade_in = randint(1, 100)
        if probabilidade_in <= 35:
            nome_art_banda.append(f'{choice(sert_fem)} &')
            if choice(sert_fem) not in nome_art_banda:
                nome_art_banda.append(choice(sert_fem))
        else:
            nome_art_banda.append(choice(sert_fem))
            if choice(sert_fem) not in nome_art_banda:
                nome_art_banda.append(choice(sert_fem))
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
    