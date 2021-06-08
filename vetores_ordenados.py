import numpy as np

class VetoresOrdenados:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print(f'O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'Na posição [{i}]', '=', self.valores[i])


    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade Máxima atingida.')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        #remaneja as posições
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            elif self.valores[i] == valor:
                return i
            elif i == self.ultima_posicao:
                return -1

    def excluir(self, valor):
        #encontra se o valor existe:
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1 #não existe
        #apaga se encontrar:
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1


vetor = VetoresOrdenados(10)

vetor.inserir(2)
vetor.inserir(4)
vetor.inserir(3)
vetor.excluir(2)
vetor.imprime()

print(f'Posição: {vetor.pesquisar(5)}')
print(f'Posição: {vetor.pesquisar(3)}')
print(f'Posição: {vetor.pesquisar(4)}')
print(f'Posição: {vetor.pesquisar(200)}')