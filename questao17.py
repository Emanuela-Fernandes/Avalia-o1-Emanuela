numero=input('Informe um número inteiro:')
digitos=0
for caracter in numero:
      if caracter in '1234567890':
         digitos = digitos + 1
print ('digitos =',digitos)
