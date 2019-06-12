a=1
q=0
while (a<=10):
    n1=float(input('informe sua primeira nota:'))
    n2=float(input('informe sua segunda nota:'))
    n3=float(input('informe sua terceira nota:'))
    n4=float(input('informe sua quarta nota:'))
    med=(n1+n2+n3+n4)/4
    media=[med]
    if med>=7.0:
        q=q+1
    a=a+1
print(q)
