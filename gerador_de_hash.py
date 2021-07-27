import hashlib


string = input('Digite a string: ')

menu = int(input('''### MENU - ESCOLHA UM TIPO DE HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print(f'Escolhido a Hash: MD5\n'
          f'O Hash da String[{string}] é: {resultado.hexdigest()}')
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print(f'Escolhido a Hash: SHA1\n'
          f'O Hash da String[{string}] é: {resultado.hexdigest()}')
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print(f'Escolhido a Hash: SHA256\n'
          f'O Hash da String[{string}] é: {resultado.hexdigest()}')
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print(f'Escolhido a Hash: SHA512\n'
          f'O Hash da String[{string}] é: {resultado.hexdigest()}')
else:
    print(f'Erro.')
