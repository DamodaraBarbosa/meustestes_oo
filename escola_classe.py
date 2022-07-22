class Escola:
    def __init__(self, nome, data_nasc, idade, serie, vestibular, port, artes, red, math, hist, filos, soci, geo, ing, quim, fis, bio, edfis, mensalidade, inadimp):
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__idade = idade
        self.__serie = serie
        self.__vestibular = vestibular
        self.__port = port
        self.__artes = artes
        self.__red = red
        self.__math = math
        self.__hist = hist
        self.__filos = filos
        self.__soci = soci
        self.__geo = geo
        self.__ing = ing
        self.__quim = quim
        self.__fis = fis
        self.__bio = bio
        self.__edfis = edfis
        self.__divida = mensalidade * inadimp
        self.__mensalidade = mensalidade
        self.__inadimp = inadimp
    
    def infos_pessoais(self):
        print(f'Nome: {self.__nome}')
        print(f'Data de nascimento: {self.__data_nasc}')
        print(f'Idade: {self.__idade} anos')
    
    def infos_esc(self):
        print(f'Série: {self.__serie}')
        print(f'Vestibular: {self.__vestibular}')
    
    def infos_finan(self):
        print(f'Mensalidade: {self.__mensalidade}')
        print(f'Inadimplência: {self.__inadimp} meses')
    
    def pagamento(self, valor):
        self.__divida -= valor
        if self.__divida == 0:
            divida = valor
            print(f'Sua dívida de R$ {divida:.2f} foi quitada!')
            self.__inadimp = 0
        elif self.__divida < 0:
            print(f'Você possui um crédito de R$ {-(self.__divida):.2f}.')
            self.__inadimp = 0
        else:
            print(f'Faltam R$ {self.__divida:.2f} para quitar sua dívida.')
             

    def notas(self):
        print(f'Português: {self.__port}')
        print(f'Artes: {self.__artes}')
        print(f'Redação: {self.__red}')
        print(f'Matemática: {self.__math}')
        print(f'História: {self.__hist}')
        print(f'Filosofia: {self.__filos}')
        print(f'Sociologia: {self.__soci}')
        print(f'Geografia: {self.__geo}')
        print(f'Inglês: {self.__ing}')
        print(f'Química: {self.__quim}')
        print(f'Física: {self.__fis}')
        print(f'Biologia: {self.__bio}')
        print(f'Ed. Física: {self.__edfis}')
    
    def media_geral(self):
        media_g = (self.__port + self.__red + self.__artes + self.__math + self.__hist + self.__filos + self.__soci + self.__geo + self.__ing + self.__quim + self.__fis + self.__bio + self.__edfis)/13
        return media_g

    def media_humanas(self):
        media_h = (self.__hist + self.__geo + self.__filos + self.__soci)/4
        return media_h
    
    def media_linguagens(self):
        media_l = (self.__port + self.__artes + self.__ing + self.__edfis)/4
        return media_l
    
    def media_natureza(self):
        media_n = (self.__quim + self.__fis + self.__bio)/3
        return media_n

    @property
    def nome(self):
        return self.__nome
    
    @property
    def divida(self):
        return self.__divida
    
    @property
    def inadimp(self):
        return self.__inadimp