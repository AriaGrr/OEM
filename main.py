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

# Variaveis globais

# Constantes
pi = float (3.14159265359) # Número pi
c = float (299792458) # Velocidade da luz no vácuo em m/s

# Variáveis
f = float (0) # Frequência em Hz
l = float (0) # Comprimento de onda em m
k = float (0) # Número de onda em rad/m
w = float (0) # Frequência angular em rad/s
Em = float (0) # Amplitude do campo elétrico em V/m
Bm = float (0) # Amplitude do campo eletromagnético em T
I = float (0) # Intensidade da corrente em A


# Função para limpar a tela do terminal
def clear_screen():
    print('\033[H\033[J')

def limpar_variaveis():
    f = 0
    l = 0
    k = 0
    w = 0
    Em = 0
    Bm = 0
    I = 0

# Função para o menu de equações
def menu():
    clear_screen()
    print('Opções de entradas:')
    print('1 - Amplitude do campo elétrico (Em):')
    print('Retorna Bm e I.')
    print('2 - Amplitude do campo magnético (Bm):')
    print('Retorna Em e I.')
    print('3 - Intensidade (I):')
    print('Retornara Bm e Em.')
    print('4 - Frequencia (f):')
    print('Retorna lambda, k e w.')
    print('5 - Comprimento de onda (lambda):')
    print('Retorna f, k e w.')
    print('6 - Número de onda (k):')
    print('Retorna f, lambda e w.')
    print('7 - Frequencia angular (w):')
    print('Retorna f, lambda e k.')
    print('0 - Voltar!')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
    elif option == '2':
        print('Opção 2 selecionada...')
    elif option == '3':
        print('Opção 3 selecionada...')
    elif option == '4':
        print('Opção 4 selecionada...')
    elif option == '5':
        print('Opção 5 selecionada...')
    elif option == '6':
        print('Opção 6 selecionada...')
    elif option == '7':
        print('Opção 7 selecionada...')
    elif option == '0':
        return
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')
    menu()

    

# Menu principal
while True:
    clear_screen()

    # Melhorar para que os seguintes prints apareçam apenas uma vez ao compilar?
    print('OEM: Ondas Eletromagnéticas com Python')
    print('Membros: Marjorie Luize Martins Costa, Paulo Andre de Oliveira Hirata, Diogo, Victor')
    print('Paragrafo com a descrição do programa')

    print('Opções:')
    print('1 - Equações')
    print('2 - Conversores')
    print('3 - Limpar variáveis')
    print('0 - Sair')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Redirecionando para o menu de equações...')
        menu()
    elif option == '2':
        print('Redirecionando para o menu de conversores...')
    elif option == '3':
        print('Limpando variáveis...')
        limpar_variaveis()
    elif option == '0':
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')

print('Finalizando...')
