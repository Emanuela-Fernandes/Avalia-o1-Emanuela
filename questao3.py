altura= float(input('Informe a sua altura:'))
sexo= input('Informe seu sexo:')
if sexo== 'masculino':
    pesoideal=((72.7*altura)-58)
    print('O seu peso ideal é:', pesoideal)
else:
    pesoideal=((62.1*altura)-44.7)
    print('O seu peso ideal é:', pesoideal)
    
