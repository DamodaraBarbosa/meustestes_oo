import random

def probabilidade_primeiro_nome(nome, probabilidade):
    primeiro_nome_masc = ['José',  'João',  'Antônio', 'Francisco', 'Carlos']
    primeiro_nome_fem = ['Maria', 'Ana', 'Francisca', 'Antônia', 'Márcia']
    nome_masc = ['Miguel', 'Arthur', 'Gael', 'Heitor', 'Theo', 'Davi', 'Gabriel', 'Bernardo', 'Samuel', 'Enzo']
    nome_fem = ['Helena', 'Alice', 'Laura', 'Maria', 'Valentina', 'Heloísa', 'Clara', 'Cecília', 'Júlia', 'Sophia']
    if nome in nome_masc:
        if probabilidade <= 30:
            return random.choice(primeiro_nome_masc)
    elif nome in nome_fem:
        if probabilidade <= 30:
            return random.choice(primeiro_nome_fem)

def serie_aluno(idade, probabilidade):
    if idade == 14:
        return '1º ano'
    elif idade == 15:
        if probabilidade < 30:
            return '2º ano'
        else:
            return '1º ano'
    elif idade == 16:
        if probabilidade < 30:
            return '3º ano'
        else:
            return '2º ano'
    elif idade == 17:
        return '3º ano'

def mensalidade_serie(serie):
    mensalidade_1ano = 0
    mensalidade_2ano = 0
    mensalidade_3ano = 0

    if serie == '1º ano':
        mensalidade_1ano = random.uniform(700, 1000)
        return f'R$ {mensalidade_1ano:.2f}'
    elif serie == '2º ano':
        mensalidade_2ano = random.uniform(700, 1000)
        if mensalidade_2ano <= mensalidade_1ano:
            mensalidade_2ano = random.uniform(700, 1000)
        else:
            return f'R$ {mensalidade_2ano:.2f}'
    elif serie == '3º ano':
        mensalidade_3ano = random.uniform(700, 1000)
        if mensalidade_3ano <= mensalidade_2ano:
            mensalidade_3ano = random.uniform(700, 1000)
        else:
            return f'R$ {mensalidade_3ano}'

def aluno_inadimplencia(probabilidade):
    if probabilidade >= 50:
        return 0
    elif probabilidade < 50:
        return random.randint(1, 2)
    elif probabilidade < 30:
        return random.randint(3, 6)
    elif probabilidade < 20:
        return random.randint(7, 9)
    elif probabilidade < 10:
        return random.randint(10, 12)
    elif probabilidade < 5:
        return random.randint(13, 24)



