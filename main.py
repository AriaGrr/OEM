# Turma 725, Equipe 4:
# Marjorie Luize Martins Costa, RA: 24223084-5
# Paulo Andre de Oliveira Hirata, RA: 24.123.086-1
# Diogo Santos Linna, RA: 24.123.003-6
# Victor Merker Binda, RA:

# Variaveis Globais: float f, lambda, k, w, Em, Bm, I, c, pi.
# Paragrafo explicativo em print
# Funções:  
# Conversores:
# Verificadores:
# Menu: 
# Retorno de valores em 4 significativos

# Bibliotecas
import math
from decimal import Decimal

# Variaveis globais
teste = Decimal(0) # Variável para testar se é a primeira vez que o programa é executado

# Constantes
pi = Decimal(3.1415) # Número pi com 4 significativos
c = Decimal(299792458) # Velocidade da luz no vácuo em m/s
u = Decimal(4) * pi * Decimal('1e-7') # Permeabilidade magnética do vácuo em H/m
e = Decimal(8.854187817 * 10**-12) # Permissividade elétrica do vácuo em F/m

# Variáveis
f = Decimal(0) # Frequência da onda em Hz
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

# Função para calcular frequencia a partir da frequência angular
# Correta
def frequencia_frequencia_angular():
    f = w / (2 * pi)
    return f

# Função para calcular a frequência angular
# Correta
def frequencia_angular():
    w = 2 * pi * f
    return w

# Função para calcular o comprimento apartir do número de onda
# Correta
def comprimento_numero_onda():
    s = (2 * pi) / k
    return s

# Função para calcular a frequência
# Correta
def frequencia():
    f = c / l
    return f

# Função para calcular o comprimento de onda
# Correta
def comprimento_onda():
    l = c / f
    return l

# Função para calcular o número de onda
# Correta
def numero_onda():
    k = 2 * pi / l
    return k

# Função para calcular a amplitude do campo elétrico apartir da intensidade da onda
# Correta
def amplitude_campo_eletrico_intensidade():
    a = Decimal(2) * I
    b = e * c
    d = a / b
    Em = d.sqrt()
    return Em

# Função para calcular a amplitude do campo elétrico
# Correta
def amplitude_campo_eletrico():
    Em = Bm * c 
    return Em

# Função para calcular a intensidade da onda
# Correta
def intensidade_onda():
    I = Decimal(1/2) * e * c * Em**2
    return I

# Função para calcular a amplitude do campo magnético a partir da amplitude do campo elétrico
# Correta
def amplitude_campo_magnetico():
    Bm = Em / c
    return Bm

# Conversores

# Função para converter ut para T
# Correta
def ut_para_t(s):
    t = s / 1000000
    return t

# Função para converter T para ut
# Correta
def t_para_ut(s):
    t = s * 1000000
    return t

# Elevar
def elevar():
    print('Digite o valor:')
    x = Decimal(input('Valor: '))
    y = Decimal(input('E: '))
    z = x * 10**y
    print(f'{x} * 10^{y} = {z}')
    return z

# Função para o menu de conversores
def conversores():
    clear_screen()
    print('Opções de conversão:')
    # Correta
    print('1 - Microtesla para Tesla (ut -> T)')
    #
    print('2 - Tesla para Microtesla (T -> ut)')
    # Correta
    print('3 - E')

    print('0 - Voltar!')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
        print('Digite o valor em microtesla (ut):')
        ut = Decimal(input('ut: '))
        T = ut_para_t(ut)
        print(f'{ut} ut = {T:.4g} T')
    elif option == '2':
        print('Opção 2 selecionada...')
        print('Digite o valor em Tesla (T):')
        T = Decimal(input('T: '))
        ut = t_para_ut(T)
        print(f'{T} T = {ut:.4g} ut')
    elif option == '3':
        print('Opção 3 selecionada...')
        elevar()
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
    # Correta
    print('3 - Intensidade da onda (I) em W/m^2:')
    print('Retorna Bm e Em.')
    # Correta
    print('4 - Frequencia da onda (f) em Hz:')
    print('Retorna lambda, k e w.')
    # Correta
    print('5 - Comprimento de onda (lambda) em m:')
    print('Retorna f, k e w.')
    # Correta
    print('6 - Número de onda (k) em rad/m:')
    print('Retorna f, lambda e w.')
    # Correta
    print('7 - Frequencia angular (w) em rad/s:')
    print('Retorna f, lambda e k.')

    print('0 - Voltar!')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
        print('Digite a amplitude do campo elétrico (Em) em V/m:')
        Em = Decimal(input('Em: '))
        Bm = amplitude_campo_magnetico()
        I = intensidade_onda()
        print(f'Amplitude do campo magnético (Bm): {Bm:.4g} T')
        print(f'Intensidade da onda (I): {I:.4g} W/m^2')
        limpar_variaveis()

    elif option == '2':
        print('Opção 2 selecionada...')
        print('A amplitude do campo magnético (Bm) está em T?')
        print('s/n')
        option = input('Escolha uma opção: ')
        if option == 's':
            print('Digite a amplitude do campo magnético (Bm) em T:')
            Bm = Decimal(input('Bm: '))
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
                Bm = ut_para_t(Bm)
                Em = amplitude_campo_eletrico()
                I = intensidade_onda()
                print(f'Amplitude do campo elétrico (Em): {Em:.4g} V/m')
                print(f'Intensidade da onda (I): {I:.4g} W/m^2')
            elif option == '0':
                return
            else:
                print('Opção inválida. Escolha uma opção válida.')
        else:
            print('Opção inválida. Escolha uma opção válida.')
        limpar_variaveis()
    elif option == '3':
        print('Opção 3 selecionada...')
        print('Digite a intensidade da onda (I) em W/m^2:')
        I = Decimal(input('I: '))
        Em = amplitude_campo_eletrico_intensidade()
        Bm = amplitude_campo_magnetico()
        print(f'Amplitude do campo elétrico (Em): {Em:.4g} V/m')
        print(f'Amplitude do campo magnético (Bm): {Bm:.4g} T')
        limpar_variaveis()

    elif option == '4':
        print('Opção 4 selecionada...')
        print('O valor da frequência da onda (f) está E?')
        print('s/n')
        option = input('Escolha uma opção: ')
        if option == 's':
            print('...')
            f = Decimal(elevar())
            l = comprimento_onda()
            k = numero_onda()
            w = frequencia_angular()
            print(f'Comprimento de onda (lambda): {l:.4g} m')
            print(f'Número de onda (k): {k:.4g} rad/m')
            print(f'Frequência angular (w): {w:.4g} rad/s')
        elif option == 'n':
            print('Digite a frequência da onda (f) em Hz:')
            f = Decimal(input('f: '))
            l = comprimento_onda()
            k = numero_onda()
            w = frequencia_angular()
            print(f'Comprimento de onda (lambda): {l:.4g} m')
            print(f'Número de onda (k): {k:.4g} rad/m')
            print(f'Frequência angular (w): {w:.4g} rad/s')
        else:
            print('Opção inválida. Escolha uma opção válida.')
        limpar_variaveis()

    elif option == '5':
        print('Opção 5 selecionada...')
        print('O valor do comprimento de onda (lambda) em m está E?')
        print('s/n')
        option = input('Escolha uma opção: ')
        if option == 's':
            l = Decimal(elevar())
            f = frequencia()
            k = numero_onda()
            w = frequencia_angular()
            print(f'Frequência da onda (f): {f:.4g} Hz')
            print(f'Número de onda (k): {k:.4g} rad/m')
            print(f'Frequência angular (w): {w:.4g} rad/s')
        elif option == 'n':
            print('Digite o comprimento de onda (lambda) em m:')
            l = Decimal(input('lambda: '))
            f = frequencia()
            k = numero_onda()
            w = frequencia_angular()
            print(f'Frequência da onda (f): {f:.4g} Hz')
            print(f'Número de onda (k): {k:.4g} rad/m')
            print(f'Frequência angular (w): {w:.4g} rad/s')
        else:
            print('Opção inválida. Escolha uma opção válida.')
        limpar_variaveis()

    elif option == '6':
        print('Opção 6 selecionada...')
        print('O valor do número de onda (k) em rad/m está E?')
        print('s/n')
        option = input('Escolha uma opção: ')
        if option == 's':
            k = Decimal(elevar())
            l = comprimento_numero_onda()
            f = frequencia()
            w = frequencia_angular()
            print(f'Comprimento de onda (lambda): {l:.4g} m')
            print(f'Frequência da onda (f): {f:.4g} Hz')
            print(f'Frequência angular (w): {w:.4g} rad/s')
        elif option == 'n':
            print('Digite o número de onda (k) em rad/m:')
            k = Decimal(input('k: '))
            l = comprimento_numero_onda()
            f = frequencia()
            w = frequencia_angular()
            print(f'Comprimento de onda (lambda): {l:.4g} m')
            print(f'Frequência da onda (f): {f:.4g} Hz')
            print(f'Frequência angular (w): {w:.4g} rad/s')
        else:
            print('Opção inválida. Escolha uma opção válida.')
        limpar_variaveis()

    elif option == '7':
        print('Opção 7 selecionada...')
        print('O valor da frequência angular (w) em rad/s está E?')
        print('s/n')
        option = input('Escolha uma opção: ')
        if option == 's':
            w = Decimal(elevar())
            f = frequencia_frequencia_angular()
            print(f'Frequência da onda (f): {f:.4g} Hz')
            l = comprimento_onda()
            k = numero_onda()
            print(f'Comprimento de onda (lambda): {l:.4g} m')
            print(f'Número de onda (k): {k:.4g} rad/m')

        elif option == 'n':
            print('Digite a frequência angular (w) em rad/s:')
            w = Decimal(input('w: '))
            f = frequencia_frequencia_angular()
            print(f'Frequência da onda (f): {f:.4g} Hz')
            l = comprimento_onda()
            k = numero_onda()
            print(f'Comprimento de onda (lambda): {l:.4g} m')
            print(f'Número de onda (k): {k:.4g} rad/m')

        else:
            print('Opção inválida. Escolha uma opção válida.')

        limpar_variaveis()

    elif option == '0':
        clear_screen()
        return
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')
    menu()

    

# Menu principal
while True:
    clear_screen()

    if teste == Decimal(0):
        print('OEM: Ondas Eletromagnéticas com Python')
        print('Desnvolvedores: Marjorie Luize Martins Costa, Paulo Andre de Oliveira Hirata, Diogo Santos Linna, Victor Merker Binda')
        # Melhorar a descrição do programa
        print('Este programa foi desenvolvido para realizar cálculos e conversões relacionadas a ondas eletromagnéticas. Ele permite calcular e converter grandezas como frequência, comprimento de onda, intensidade do campo elétrico e magnético, entre outras. O funcionamento do programa é simples: ao iniciá-lo, você será apresentado a um menu com diferentes opções. Após escolher uma opção, siga as instruções fornecidas para inserir os dados necessários. O programa então realizará os cálculos correspondentes e fornecerá os resultados com precisão de 4 significativos. É importante ressaltar que as variáveis utilizadas são automaticamente limpas após cada cálculo, garantindo a integridade dos resultados e a eficiência do programa. Sinta-se à vontade para explorar as funcionalidades oferecidas e utilizar o programa conforme suas necessidades relacionadas a ondas eletromagnéticas.')
        #
        print('Pressione Enter para continuar...')
        input() 
        teste = Decimal(1)

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
        conversores()

    elif option == '3':
        print('Limpando variáveis...')
        limpar_variaveis()

    elif option == '0':
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')

print('Finalizando...')
