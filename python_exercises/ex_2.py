'''
Escreva um algoritmo para calcular a média de um
conjunto de 15 valores inteiros e positivos, fornecidos pelo usuário.
Exiba no final do programa além da média.
'''
quant_numbers = int(3)
sum = int(0)
count = int(0)
value = None
average = float(0)

while (count < quant_numbers):
    value = int(input('Digite 15 valores inteiros positivos: ' + str(count + 1) + '° : '))
    sum = sum + value
    count = count + 1

average = "{:.2f}".format(sum / quant_numbers) # Usando uma formatação de String para que a media tenha apenas duas casas decimais
print('A media é:', average)