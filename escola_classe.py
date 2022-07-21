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
        self.__mensalidade = mensalidade
        self._inadimp = inadimp

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