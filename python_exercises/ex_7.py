'''
Exiba a tabuada de um número (1 a 10) fornecido pelo usuário.
Por exemplo se ele digitar o número 5, então será mostrado:
5	x	1	=	5
5	x	2	=	10
5	x	3	=	15
5	x	4	=	20
5	x	5	=	25
5	x	6	=	30
5	x	7	=	35
5	x	8	=	40
5	x	9	=	45
5 x 10 =	50

'''

num = float(input("Digite um nuemro para ver sua tabuada: "))
sum = 0
for c in range(1,11):
  sum = num * c
  print(str (num) + " x " + str (c) + " = " + str (sum))