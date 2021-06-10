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

    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            elif self.valores[i] == valor:
                return i
            elif i == self.ultima_posicao:
                return -1

    # O( log n )
    def pesquisa_binaria(self, valor):
        limite_inferior = 0 #é o está entre
        limite_superior = self.ultima_posicao #está entre

        #Verifica o intervalo
        while True:
            #encontra a posição:
            posicao_atual = int((limite_inferior + limite_superior) / 2)

            #Se na 1º tentativa, no meio do vetor:
            if self.valores[posicao_atual] == valor:
                return posicao_atual

            #Se nao achou:
            elif limite_inferior > limite_superior:
                return -1

            #Dividir elementos:
            else:
                #Limite inferior:
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1







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


vetor.inserir(8)
vetor.inserir(9)
vetor.inserir(4)
vetor.inserir(1)
vetor.inserir(5)
vetor.inserir(7)
vetor.inserir(11)
vetor.inserir(100)
vetor.inserir(2)

vetor.imprime()

print(f'Posição da Pesquisa binária: {vetor.pesquisa_binaria(11)}')