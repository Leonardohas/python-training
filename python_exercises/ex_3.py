'''
Fazer um algoritmo, utilizando o comando enquanto ...
faça, que: Leia um conjunto de 5 fichas contendo cada uma,
a idade e nome de um indivíduo, calcule e escreva a idade média deste grupo de indivíduos, com a lista de nomes no final.

'''
quant_people = int(input('Digite a quantidade de pessoas: '))
names = []
age = None
avaregeAge = 0
sum = 0 
count = 0

while (count < quant_people):
    age = int(input('Digite a idade da ' + str(count + 1) + '° pessoa: '))
    name = str(input('Digite o nome da ' + str(count + 1) + '° pessoa: '))
    sum += age
    count = count + 1
    names.append(name)

avaregeAge = "{:.2f}".format(sum / quant_people)
print('A media de idades dos ' + str(quant_people) + ' individuos são: ' + str(avaregeAge))
print('E seus nomes são: \n')
for name in names:
    print(name)
    print('--' * 7)
