import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # np.empty cria um array vazio e com o tamanho agora definido pela própria capacidade e de nº inteiros
        self.valores = np.empty(self.capacidade, dtype=int)

    #imprime os dados do vetor
    def imprime(self):
        if self.ultima_posicao == -1:
            print(f'O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'Na posição [{i}]', '=', self.valores[i])

    #insere dados no vetor:
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print(f'Capacidade Máxima já foi atingida.')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor


vetor = VetorNaoOrdenado(5)

vetor.inserir(3)
vetor.inserir(5)
vetor.inserir(8)
vetor.inserir(1)
vetor.inserir(7)
vetor.inserir(9)
vetor.inserir(3)
