'''
Num frigorífico existem 10 bois. Cada boi traz preso em seu pescoço 
uma etiqueta contendo seu número
de identificação e seu weight. Fazer um algoritmo que escreva:
o número e o weight do boi mais gordo, o número e o weight do boi mais magro 
e o weight médio dos bois.

'''
quantCattle = int(input('Digite a quantidade de cabeça de gado: '))
cattle = quantCattle 
numberID = None 
cont = cattle_MN = cattle_GN = weight = avaregeWeight = sum = cattle_MP = cattle_GP =  0 

while(cont < cattle):
  numberID = int(input("Digite um numero de identificação: "))
  weight = int(input("Digite o peso do boi: "))
  sum = sum + weight
  cont = 1 + cont
  if(weight < cattle_MP or cattle_MP == 0):
    cattle_MP = weight
    cattle_MN = numberID
  if(weight > cattle_GP):
    cattle_GP = weight
    cattle_GN = numberID

print("O boi mais gordo pesa: " + str(cattle_GP) + " E seu ID é: " + str (cattle_GN))
print("O boi mais magro pesa: " + str (cattle_MP)+ " E seu ID é: " + str (cattle_MN))
avaregeWeight = sum / cattle
print('A media dos pesos é: ', float(avaregeWeight),'Kg')