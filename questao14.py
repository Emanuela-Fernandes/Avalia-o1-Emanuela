frase= input('Informe uma frase:')
vogais=0
branco=0
for caracter in frase:
      if caracter in ' ':
         branco = branco + 1
      if caracter in 'aeiou' :
         vogais = vogais + 1 
print ('Vogais=', vogais)
print ('Espaços em braco=',branco)
