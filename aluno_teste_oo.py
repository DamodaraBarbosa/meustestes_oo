import random
import probabilidade_aluno 

nomes = ['Miguel', 'Arthur', 'Gael', 'Heitor', 'Theo', 'Davi', 'Gabriel', 'Bernardo', 'Samuel', 'Enzo', 
'Helena', 'Alice', 'Laura', 'Letícia', 'Valentina', 'Heloísa', 'Clara', 'Cecília', 'Júlia', 'Sophia']
sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Ferreira', 'Alves', 'Pereira', 'Lima', 'Gomes', 'Ribeiro', 'Martins', 'Almeida', 'Andrade', 'Barros', 'Batista', 'Borges', 'Campos', 'Cardoso', 'Carvalho', 'Castro', 'Costa', 'Dias', 'Duarte', 'Freitas', 'Fernandes', 'Garcia', 'Gonçalves', 'Lima', 'Lopes', 'Machado']
aluno = list()
dados = list()

for i in range(0, 20):
    nomes = ['Miguel', 'Arthur', 'Gael', 'Heitor', 'Theo', 'Davi', 'Gabriel', 'Bernardo', 'Samuel', 'Enzo', 
    'Helena', 'Alice', 'Laura', 'Letícia', 'Valentina', 'Heloísa', 'Clara', 'Cecília', 'Júlia', 'Sophia']
    
    nome = random.choice(nomes)
    aluno.append(nome)
    p_nome = probabilidade_aluno.probabilidade_primeiro_nome(nome, random.randrange(1, 100))
    if p_nome != None:
        aluno.insert(0, p_nome)
    aluno.append(random.choice(sobrenomes))
    aluno.append(random.choice(sobrenomes))

    dia = random.randint(1, 31)
    mes = random.randint(1, 12)
    ano = random.randint(2005, 2008)
    idade = 2022 - ano
    if len(list(f'{mes}')) == 2:
        aluno.append(f'Data de nascimento: {dia}/{mes}/{ano}')
    else:
        aluno.append(f'Data de nascimento: {dia}/0{mes}/{ano}')
    aluno.append(f'Idade: {idade} anos')
    serie = probabilidade_aluno.serie_aluno(idade, random.randrange(1, 100))
    aluno.append(f'Série: {serie}')
    if serie == '3º ano':
        vest = ['ENEM', 'UECE', 'ITA', 'IME', 'Fuvest', 'Unifor', 'EPCAR']
        aluno.append(f'Vestibular: {random.choice(vest)}')
    aluno.append(f'Português: {random.uniform(0, 10):.2f}') 
    aluno.append(f'Artes: {random.uniform(0, 10):.2f}')
    aluno.append(f'Redação: {random.uniform(0, 10):.2f}')
    aluno.append(f'Matemática: {random.uniform(0, 10):.2f}')
    aluno.append(f'História: {random.uniform(0, 10):.2f}')
    aluno.append(f'Filosofia: {random.uniform(0, 10):.2f}')
    aluno.append(f'Sociologia: {random.uniform(0, 10):.2f}')
    aluno.append(f'Geografia: {random.uniform(0, 10):.2f}')
    aluno.append(f'Inglês: {random.uniform(0, 10):.2f}')
    aluno.append(f'Química: {random.uniform(0, 10):.2f}')
    aluno.append(f'Física: {random.uniform(0, 10):.2f}')
    aluno.append(f'Biologia: {random.uniform(0, 10):.2f}')
    aluno.append(f'Ed. Física: {random.uniform(0, 10):.2f}')
    mensalidade = probabilidade_aluno.mensalidade_serie(serie)
    aluno.append(f'Mensalidade: {mensalidade}')
    inadimplencia = probabilidade_aluno.aluno_inadimplencia(random.randrange(1, 100))
    aluno.append(f'Inadimplência: {inadimplencia} meses.')
    dados.append(aluno[:])
    aluno.clear()

texto = ''
arquivo = open('dados_alunos.txt', 'w')
# for i, v in enumerate(dados):
#     listaIndex=''
#     for j in v:
#         listaIndex += f"{j} "
#     listaIndex += "\n"
#     texto += listaIndex
# arquivo.writelines(texto)

for dado in dados:
    texto += f"Nome: {dado["nome"]}, Idade: {dado["idade"]}\n"



