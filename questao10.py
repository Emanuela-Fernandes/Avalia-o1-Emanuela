nome = input('Informe seu nome de usuário:')
senha = input('Informe sua senha:')
if senha==nome:
    print('A senha não pode ser igual ao nome de usuário, por favor, informe novamente!')
    nome = input('Informe seu nome de usuário:')
    senha = input('Informe sua senha:')
    
