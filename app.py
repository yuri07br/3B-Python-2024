import os
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

def finalizar_progama():
    os.system('clear')
    print('finalizando progama')


if opcao_escolhida == 1 :
    print('cadastrar automoveis')
elif opcao_escolhida == 2:
    print('listar automoveis')
elif opcao_escolhida == 3:
    print('ativar/desativar narrador')
else:
    print('voce escolheu a opeçao', opcao_escolhida)
else:
finalizar_progama()

def main():