class Art_banda:
    def __init__(self, nome, genero, tipo, fans, curtidas, faturamento):
        self._nome = nome
        self.genero = genero
        self.tipo = tipo
        self._fans = fans
        self._curtidas = curtidas
        self._faturamento = faturamento
    
    @property
    def curtidas(self):
        return self._curtidas

    @property
    def fans(self):
        return self._fans

    @property
    def nome(self):
        return self._nome
    
    @property
    def faturamento(self):
        return self._faturamento

    def __str__(self):
        return f'Nome: {self._nome} | Gênero: {self.genero} | Tipo: {self.tipo} | Fãs: {self._fans} | Curtidas: {self._curtidas} | Faturamento: USD {self._faturamento}/ano'
    
    def __getitem__(self, item):
        return self._faturamento[item]

    def faturamento(self):
        return self._faturamento
    
    def sortear(self):
        return sorted(self._curtidas)


class Playlist:
    def __init__(self, artistas):
        self._artistas = artistas
    
    def __getitem__(self, item):
        return self._artistas[item]

    def __len__(self):
        return len(self._artistas)