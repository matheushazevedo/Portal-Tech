lista = ["banana", "arroz", "feijão", "carne", "macarrão", "molho"]

while True:
    print(f'\033[0;32m{" LOJA ":=^25}\033[0;37m')
    for i in lista:
        print(i)
    print('[1] Remover produto\n[2] Adicionar produto\n[3] Substituir produto\n[0] Sair')
    print(f'\033[0;32m{"-":=^25}\033[0;37m')
    while True:
        try:
            escolha = int(input('Digite um número de uma opção: '))
        except ValueError:
            print('\033[0;31mERRO: digite um valor inteiro válido, tente novamente.\033[0;37m')
        except Exception as erro:
            print(erro)
        else:
            if escolha >= 0 and escolha <= 4:
                break
            else: 
                print('\033[0;31mERRO: não é uma opção válida, tente novamente.\033[0;37m')
                continue
    if escolha == 0: break

    match escolha:
        case(1):
            nomeProduto = str(input('Digite o nome do produto: '))
            lista.pop(lista.index(nomeProduto))
        case(2):
            nomeProduto = str(input('Digite o nome do produto: '))
            lista.append(nomeProduto)
        case(3):
            nomeProduto = str(input('Digite o nome do produto a ser substituido: '))
            novoProduto = str(input('Digite o nome do novo produto: '))
            lista[lista.index(nomeProduto)] = novoProduto
