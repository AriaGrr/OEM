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
    Em = Bm * c 
    return Em

# Função para calcular a intensidade da onda
# Correta
def intensidade_onda():
    #I = (Em * Bm) / (2 * c)
    I = Decimal(1/2) * e * c * Em**2
    return I

# Função para calcular a amplitude do campo magnético a partir da amplitude do campo elétrico
# Correta
def amplitude_campo_magnetico():
    #Bm = Em / (c * u)
    Bm = Em / c
    return Bm

# Conversores

# Função para converter ut para T
def ut_para_t(s):
    t = s / 1000000
    return t

# Função para converter T para ut
def t_para_ut(s):
    t = s * 1000000
    return t

# Função para o menu de conversores
def conversores():
    clear_screen()
    print('Opções de conversão:')
    #Correta
    print('1 - Microtesla para Tesla (ut -> T)')
    #
    print('2 - Tesla para Microtesla (T -> ut)')
    #
    print('0 - Voltar!')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
        print('Digite o valor em microtesla (ut):')
        ut = Decimal(input('ut: '))
        #if not is_number(ut):
            #print('Valor inválido. Tente novamente.')
            #return
        #ut = Decimal(round(float(ut), 4))
        T = ut_para_t(ut)
        print(f'{ut} ut = {T:.4g} T')
    elif option == '2':
        print('Opção 2 selecionada...')
        print('Digite o valor em Tesla (T):')
        T = Decimal(input('T: '))
        #if not is_number(T):
            #print('Valor inválido. Tente novamente.')
            #return
        #T = Decimal(round(float(T), 4))
        ut = t_para_ut(T)
        print(f'{T} T = {ut:.4g} ut')
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
    # Correta
    print('1 - Amplitude do campo elétrico (Em) em V/m:')
    print('Retorna Bm e I.')
    # Correta
    print('2 - Amplitude do campo magnético (Bm) em T:')
    print('Retorna Em e I.')
    #
    print('3 - Intensidade da onda (I) em W/m^2:')
    print('Retorna Bm e Em.')
    #
    print('4 - Frequencia da onda (f) em Hz:')
    print('Retorna lambda, k e w.')
    #
    print('5 - Comprimento de onda (lambda) em m:')
    print('Retorna f, k e w.')
    #
    print('6 - Número de onda (k) em rad/m:')
    print('Retorna f, lambda e w.')
    #
    print('7 - Frequencia angular (w) em rad/s:')
    print('Retorna f, lambda e k.')
    #
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

        #Bm = Decimal(round(amplitude_campo_magnetico(), 4))
        Bm = amplitude_campo_magnetico()
        I = intensidade_onda()
        # Teste 
        #print(Em)
        #print(Bm)
        #print(I)
        #
        print(f'Amplitude do campo magnético (Bm): {Bm:.4g} T')
        print(f'Intensidade da onda (I): {I:.4g} W/m^2')
    elif option == '2':
        print('Opção 2 selecionada...')
        print('A amplitude do campo magnético (Bm) está em T?')
        print('s/n')
        option = input('Escolha uma opção: ')
        if option == 's':
            print('Digite a amplitude do campo magnético (Bm) em T:')
            Bm = Decimal(input('Bm: '))
            #if not is_number(Bm):
                #print('Valor inválido. Tente novamente.')
                #return
            #Bm = Decimal(round(float(Bm), 4))
            Em = amplitude_campo_eletrico()
            I = intensidade_onda()
            print(f'Amplitude do campo elétrico (Em): {Em:.4g} V/m')
            print(f'Intensidade da onda (I): {I:.4g} W/m^2')
        elif option == 'n':
            print('Escolha uma conversão para T abaixo:')
            print('1 - ut para T')
            print('0 - Voltar!')
            option = input('Escolha uma opção: ')
            if option == '1':
                print('Opção 1 selecionada...')
                print('Digite a amplitude do campo magnético (Bm) em ut:')
                Bm = Decimal(input('Bm: '))
                #if not is_number(Bm):
                    #print('Valor inválido. Tente novamente.')
                    #return
                #Bm = Decimal(round(float(Bm), 4))
                Bm = ut_para_t(Bm)
                Em = amplitude_campo_eletrico()
                I = intensidade_onda()
                print(Bm)
                print(Em)
                print(I)
                print(f'Amplitude do campo elétrico (Em): {Em:.4g} V/m')
                print(f'Intensidade da onda (I): {I:.4g} W/m^2')
            elif option == '0':
                return
            else:
                print('Opção inválida. Escolha uma opção válida.')
        else:
            print('Opção inválida. Escolha uma opção válida.')


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
