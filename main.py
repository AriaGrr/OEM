# Turma 725, Equipe 4:
# Marjorie Luize Martins Costa, RA:
# Paulo Andre de Oliveira Hirata, RA:
# Diogo, RA:
# Victor, RA:

# Variaveis Globais: float f, lambda, k, w, Em, Bm, I, c, pi.
# Paragrafo explicativo em print
# Funções:  
# Conversores:
# Menu: 

def clear_screen():
    # Função para limpar a tela do terminal
    print('\033[H\033[J')


# Menu principal
while True:
    clear_screen()

    # Melhorar para que os seguintes prints apareçam apenas uma vez ao compilar?
    print('OEM: Ondas Eletromagnéticas com Python')
    print('Membros: Marjorie Luize Martins Costa, Paulo Andre de Oliveira Hirata, Diogo, Victor')
    print('Paragrafo com a descrição do programa')

    print('Opções:')
    print('1 - Teste')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Teste')
    elif option == '0':
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')

print('Finalizando...')