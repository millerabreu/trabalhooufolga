print("Olá, hoje é dia de trabalho ou de folga?")
dia = str(input("que dia é hoje?"))
if dia == 'segunda':
    print("Hoje é dia de trabalho, vamos lá!")
if dia == 'terça':
    print("Hoje ainda é terça, dia de trabalho!")
if dia == 'quarta':
    print("Ainda estamos no meio da semana, dia de trabalho! Siga em frente")
if dia == 'quinta':
    print("Quinta é quase sexta, vamos em frente! Bom trabalho!")
if dia == 'sexta':
    print("Finalmente a sexta feira, dia de happy hour, mas tem expediente! Bom trabalho!")
if dia == 'sábado':
    print("Hoje o dia é de meio expediente. Bom trabalho")
if dia == 'domingo':
    print("O sétimo dia é de descanso! Folga! Aproveite! :) ")

from time import asctime
print(asctime())