'''
Faça um programa que receba n número e calcule a raiz quadrada de cada número.

'''
import math

number = 0
sum = 0
count = 0
sum_quant = float(input("Digite quantos calculos de raizes quadradas você deseja fazer:\n "))

while(count < sum_quant):
  number = float(input("Digite um numero na qual você queira saber sua raiz quadrada:\n "))
  sum = math.sqrt(number)
  print("A raiz quadrada de  " + str (number) + " é:\n " + str (sum))
  count = count + 1