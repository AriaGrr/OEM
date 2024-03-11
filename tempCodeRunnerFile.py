    print('Digite a frequência da onda (f) em Hz:')
            f = Decimal(input('f: '))
            #if not is_number(f):
                #print('Valor inválido. Tente novamente.')
                #return
            #f = Decimal(round(float(f), 4))
            l = comprimento_onda()
            k = numero_onda()
            w = frequencia_angular()
            print(f'Comprimento de onda (lambda): {l:.4g} m')
            print(f'Número de onda (k): {k:.4g} rad/m')
            print(f'Frequência angular (w): {w:.4g} rad/s')
            limpar_variaveis()