import random, string


#Tamanho da senha
tamanho_senha = 16

#estrutura da senha, letras maiu e minu.
chars = string.ascii_letters  + string.digits + "!@#$%&*()-=+,.;/?<>ç"

rnd = random.SystemRandom()

#printa a senha
print(f''.join(rnd.choice(chars) for i in range(tamanho_senha)))