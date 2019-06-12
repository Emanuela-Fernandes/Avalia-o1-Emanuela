i=1
sim=0
while (i==1):
    a = str(input('Você telefonou para a vítima?'))
    resposta=a
    if resposta=='sim':
        sim=sim+1
    b = str(input('Você esteve no local do crime?'))
    resposta=b
    if resposta=='sim':
        sim=sim+1
    c = str(input('Você mora perto da vítima?'))
    resposta=c
    if resposta=='sim':
        sim=sim+1
    d = str(input('Você devia para a vítima?'))
    resposta=d
    if resposta=='sim':
        sim=sim+1
    e = str(input('Você já trabalhou com a vítima?'))
    resposta=e
    if resposta=='sim':
        sim=sim+1
    if sim==2:
        print('Sua classificação é: Suspeita')
    if sim==3 and sim==4:
        print('Sua classificação é: Cúmplice')
    if sim==5:
        print('Sua classificação é: Assassino')
    if sim==0:
        print('Sua classificação é: Inocente')
    i=i+1







