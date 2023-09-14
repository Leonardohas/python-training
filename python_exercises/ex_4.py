'''
Foi feita uma estatística em n cidades brasileiras para coletar dados sobre
acidentes de trânsito.
Foram obtidos os seguintes dados:
a.   nome da cidade;
b.	 número de veículos de passeio;
c.	número de acidentes de trânsito com vítimas.
Deseja-se saber:
I.	 qual é o maior e qual é o menor índice de acidentes de trânsito e a que cidades pertencem;
II.	 qual é a média de veículos nas cinco cidades juntas;

'''

smaller_city = ""
bigger_city = ""
city = 0
n_cidade = 0
number_vehicles = 0
number_accidents = 0
count = 0
minor_index = 0
higher_index = 0
sum = 0
avarege = 0
city = int(input("digite um numero de cidades brasileiras: "))

while (count < city):
  n_cidade = (input("Digite o nome da cidade: "))
  number_vehicles = int(input("Digite o numero de veiculos: "))
  number_accidents = int(input("Digite o numero de acidentes de trânsito com vitimas: "))
  sum = number_vehicles + sum
  count = count + 1
  if (number_accidents < minor_index or minor_index == 0):
    minor_index = number_accidents
    smaller_city = n_cidade
  elif (number_accidents > higher_index):
    indice_maior = number_accidents
    bigger_city = n_cidade

avarege = "{:.2f}".format(sum / city)
print("O maior indidice de acidente é " + str (indice_maior) + " na cidade: " + str (bigger_city) )
print("O menor indidice de acidente é " + str (minor_index) + " na cidade: " + str (smaller_city) )
print("A media de veiculos nas " + str (city) + " cidades é: " + str (avarege) )