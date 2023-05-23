print('programa desenvolvido para conversão de dólar para reais')
dolar = float(input('Digite a quantidade que deseja converter:'))

conversao = dolar * 5.01

print('o seu valor em reais será: R$', conversao)


eu_ro = (input(' deseja saber em euros?: '))
if eu_ro == "sim":
    
    qtd_euro = float(input('Digite a quantidade que deseja converter: £'))
    
    euro_real = qtd_euro * 5.49
    print('Você tem : £', euro_real)
    
elif eu_ro == "não":
    print('até outra vez')
