import os

Automoveis = [{'nome':'Marea','categoria':'sedan','ativo':'true'},
              {'nome':'peugeot 405','categoria':'sedan','ativo':'true'},
              {'nome':'polo','categoria':'sedan','ativo':'true'},
              {'nome':'santana','categoria':'sedan','ativo':'true'}
 ]
 
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print('')

def retorna_menu_principal():
     input('\n Digite qualquer tecla para voltar ao menu principal')
     main()

def mostrar titulo():
print('''
YT Mutimarcas
   ''')

print('1. cadastro de automoveis')
print('2. listar automoveis')
print('3. ativar automoveis')
print('4. sair da aplicaçao')

opcao_escolhida = int (input('escolha uma opeção: '))
print('voce escolheu a opção: ', opcao_escolhida)

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('escolha uma opecao:'))
        print('voce escolheu a opcao:'. opcao_escolhida)

def cadatrar_automoveis() :
    os.system('clear')
    print('cadastrar automoveis...')
    nome_automovel = input('digite o nome do automovel:')
    automoveis.append(nome do carro )
    print(f'{nome_carro}foi adicionado a Yt mutimarcas carros')
    input('digite qualquer tecla para voltar')
    main()
    
    def 

def finalizar_progama():
    os.system('clear')
    print('finalizando progama')

def opcao_invalida():
    print('esse caracter nao e permitido')
    input('digite qualquer tecla')
    main()
    
    def main():
        mostrar titulo()
        

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_carros()
        elif opcao_escolhida == 2:
            mostrar_carros
        elif opcao_escolhida == 3:
            print('Ativar/desativar automovel')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()

 except:
       opcao_invalida()

def cadastrar_carros():
    exibir_subtitulo('Cadastrar automoveis')

    nome_automovel = input('Digite o nome do automovel: ')
    carros.append(nome_automovel)
    print(f'{nome_automovel} foi adicionado a lista de automoveis')
    input('Digite qualquer tecla para voltar')
    main()

def mostrar_carros():
    exibir_subtitulo('Listar automoveis')
    
    for automovel in aultomovel:
         print(f' - automoveis')

    input('Digite qualquer tecla para voltar')
    main()

def finalizar_programa():
        os. syatem('cls')
        print('Finalizando programa')

def opcao_invalida():
        print('Este caracter não é permitido')
        input('Digite qualquer tecla')
        main()

def main():
    mostra_titulo ()
    mostra_escolha()
    escolhe_opcao()

if __name__ == '__main__':
    main()
