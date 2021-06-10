import numpy as np


class Pilha:
    def __init__(self, __capacidade):
        self.__capacidade = __capacidade
        self.__topo = -1  # Serve para caso o vetor esteja em branco/vazio
        self.__valores = np.empty(self.__capacidade, dtype=int)  # cria a array inicialmente vazia

    # Verifica se a pilha já está cheia
    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False

    # Verifica se está vazia
    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha está cheia,impossível empilhar mais itens.')
        else:
            self.__topo += 1  # Adiciona ao topo
            self.__valores[self.__topo] = valor  # Adiciona na array o valor que foi passado c/parametro

    # Não passa valor porque sempre vai desempilhar o próprio TOPO
    def desempilhar(self):
        if self.__pilha_vazia():
            print('Pilha já está vazia, impossível desempilhar mais itens.')
        else:
            self.__topo -= 1


    def ver_topo(self):
        if self.__topo != -1:  # Se o topo for diferente de estar vazio.
            return self.__valores[self.__topo]
        else:
            return -1



pilha = Pilha(5)

pilha.empilhar(3)
pilha.empilhar(6)
pilha.empilhar(1)
pilha.empilhar(50)
pilha.empilhar(200)
print(pilha.ver_topo())

print(f'-' * 30)

pilha.desempilhar()
print(pilha.ver_topo())