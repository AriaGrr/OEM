# Turma 725, Equipe 4:
# Marjorie Luize Martins Costa, RA:
# Paulo Andre de Oliveira Hirata, RA:
# Diogo, RA:
# Victor, RA:

# Variaveis Globais: float f, lambda, k, w, Em, Bm, I, c, pi.
# Paragrafo explicativo em print
# Funções:  
# Conversores:
# Verificadores:
# Menu: 
# Retorno de valores em 4 significativos

from decimal import Decimal

# Variaveis globais

# Constantes
#pi = Decimal(3.14159265359) # Número pi
pi = Decimal(3.1415) # Número pi com 4 significativos
c = Decimal(299792458) # Velocidade da luz no vácuo em m/s
#c = Decimal(3 * 10**8) # Velocidade da luz no vácuo em m/s
#u = Decimal(4 * pi * 10**-7) # Permeabilidade magnética do vácuo em H/m
u = Decimal(4) * pi * Decimal('1e-7') # Permeabilidade magnética do vácuo em H/m
e = Decimal(8.854187817 * 10**-12) # Permissividade elétrica do vácuo em F/m

# Variáveis
f = Decimal(0) # Frequência em Hz
l = Decimal(0) # Comprimento de onda em m
k = Decimal(0) # Número de onda em rad/m
w = Decimal(0) # Frequência angular em rad/s
Em = Decimal(0) # Amplitude do campo elétrico em V/m
Bm = Decimal(0) # Amplitude do campo eletromagnético em T
I = Decimal(0) # Intensidade da onda eletromagnética em W/m^2


# Função para limpar a tela do terminal
def clear_screen():
    print('\033[H\033[J')

def limpar_variaveis():
    f = Decimal(0)
    l = Decimal(0)
    k = Decimal(0)
    w = Decimal(0)
    Em = Decimal(0)
    Bm = Decimal(0)
    I = Decimal(0)

# Função para verificar se o valor é um número
#def is_number(s):
    #try:
        #float(s)
        #return True
    #except ValueError:
        #return False

# Corrigir as funções de calculo abaixo.

# Função para calcular a frequência angular
def frequencia_angular():
    w = 2 * pi * f
    return w

# Função para calcular a frequência
def frequencia():
    f = w / (2 * pi)
    return f

# Função para calcular o comprimento de onda
def comprimento_onda():
    l = c / f
    return l

# Função para calcular o número de onda
def numero_onda():
    k = 2 * pi / l
    return k

# Função para calcular a amplitude do campo elétrico
def amplitude_campo_eletrico():
    Em = Bm * c * u
    return Em

# Função para calcular a intensidade da onda
def intensidade_onda():
    I = (Em * Bm) / (2 * c)
    return I

# Função para calcular a intensidade da onda
def intensidade_onda():
    #I = (Em * Bm) / (2 * c)
    I = (1/2) * e * c * Em**2
    return I

# Função para calcular a amplitude do campo magnético a partir da amplitude do campo elétrico
def amplitude_campo_magnetico():
    Bm = Em / (c * u)
    return Bm


# Função para o menu de conversores
def conversores():
    clear_screen()
    print('Opções de conversão:')
    print('1 - Hz para rad/s:')
    print('2 - rad/s para Hz:')
    print('0 - Voltar!')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
    elif option == '2':
        print('Opção 2 selecionada...')
    elif option == '0':
        return
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')
    conversores()

# Função para o menu de equações
def menu():
    global f, l, k, w, Em, Bm, I
    clear_screen()
    print('Opções de entradas:')
    print('1 - Amplitude do campo elétrico (Em) em V/m:')
    print('Retorna Bm e I.')
    print('2 - Amplitude do campo magnético (Bm):')
    print('Retorna Em e I.')
    print('3 - Intensidade da onda (I):')
    print('Retorna Bm e Em.')
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
        #print('O valor da amplitude do campo elétrico (Em) está em V/m?')
        #print('s/n')
        #option = input('Escolha uma opção: ')
        #if option == 's':

        print('Digite a amplitude do campo elétrico (Em) em V/m:')
        Em = Decimal(input('Em: '))
        #if not is_number(Em):
            #print('Valor inválido. Tente novamente.')
            #return
        #Em = Decimal(round(float(Em), 4))

        Bm = Decimal(round(amplitude_campo_magnetico(), 4))
        
        I = intensidade_onda()
        
        # Teste verificando se está salvando corretamente, resposta da saida em conflito no tester do moodle!
        print(Em)
        print(Bm)
        print(I)
        #
        print(f'Amplitude do campo magnético (Bm): {Bm:.4g}')
        print(f'Intensidade da onda (I): {I:.4g}')


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
