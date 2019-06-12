maca = float(input('Informe a quatidade em Kg de maca que você irá comprar:'))
morango = float(input('Informe a quatidade em Kg de morango que você irá comprar:'))
valor=((maca*1.50)+(morango*2.20))
if maca<=5 and morango<=5:
    paga=((maca*1.80)+(morango*2.50))
    pagar=(paga-(paga*0.10))
    print('O valor a ser pago é de:', pagar)
if maca>5 and morango>5:
    paga=((maca*1.50)+(morango*2.20))
    print('O valor a ser pago é de:', paga)
if valor==25.00:
    pagar=(valor-(valor*0.10))
    print('O valor a ser pago é de:', pagar)
    

    
