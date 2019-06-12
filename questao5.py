area = float(input('Informe o tamanho em metros quadrads da área a ser pintada:'))
litrosT=(area/3)
if litrosT<18:
    latas=1
    precoT=(latas*80)
    print('A quatidade de tintas a serem compradas é de:', latas)
    print('O preço total a ser pago é de:', precoT)
if litrosT>18:
    latas=(litrosT/18)
    precoT=(latas*80)
    print('A quatidade de tintas a serem compradas é de:', latas)
    print('O preço total a ser pago é de:', precoT)
