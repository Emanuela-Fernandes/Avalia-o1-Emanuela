data=input('Informe a data no formato dd/mm/aaaa:\n')
mm={1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
dia,mes,ano= data.split("/")
print(dia,'de',mm[int(mes)],'de',ano)
