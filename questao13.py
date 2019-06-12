vendedor= [0,0,0,0,0,0,0,0,0]
i=0
a=0
resposta=str(input('Responda "s" para alocar seu salário:'))
salario=float(input('Informe seu salário:'))
while (resposta=='s'):
    if 200>salario<299:
        vendedor[0]=vendedor[0]+1
    elif 300>salario<399:
        vendedor[1]=vendedor[1]+1
    elif 400>salario<499:
        vendedor[2]=vendedor[2]+1
    elif 500>salario<599:
        vendedor[3]=vendedor[3]+1
    elif 600>salario<699:
        vendedor[4]=vendedor[4]+1
    elif 700>salario<799:
        vendedor[5]=vendedor[5]+1
    elif 800>salario<899:
        vendedor[6]=vendedor[6]+1
    elif 900>salario<999:
        vendedor[7]=vendedor[7]+1
    elif salario>1000:
        vendedor[8]=vendedor[8]+1
    resposta=str(input('Deseja continuar? (s ou n):'))
    if resposta=='n':
        break
    a=a+1
while i<9:
    print(vendedor[i])
    i=i+1
    
    
