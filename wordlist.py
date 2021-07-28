import itertools

string = input('Digite a palavra ser permutada: ')

resultado = itertools.permutations(string, len(string))
j = 0

for i in resultado:
    print(f''.join(i))
    j += 1