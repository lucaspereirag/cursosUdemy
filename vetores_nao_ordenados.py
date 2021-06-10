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


    def imprimir(self):
        print(self.valores)

    #insere dados no vetor:
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print(f'Capacidade Máxima já foi atingida.')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor


    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i #retorna qual posição o nr pesquisado está
        return -1 #elemento não existe


    def excluir(self, valor):
        #encontra se o valor existe:
        posicao = self.pesquisar(valor)
        #apaga se encontrar:
        if posicao == -1:
            return -1 #não existe
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1


vetor = VetorNaoOrdenado(5)

vetor.inserir(3)
vetor.inserir(5)
vetor.inserir(8)
vetor.inserir(1)
vetor.inserir(7)
vetor.imprime()

print('-' * 30)

vetor.excluir(5)
vetor.imprime()
#vetor.imprime()

print('-' * 30)

print(f'Na posição: {vetor.pesquisar(300)}') #retorna -1
print(f'Na posição: {vetor.pesquisar(8)}') #retorna 2

print('-' * 30)
vetor.imprimir()

