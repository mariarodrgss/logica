from random import  randint

print("Jogos de Dados")

dados1= randint(1,6)
dados2= randint(1,6)
Jogador1= dados1 + dados2 

dados3= randint(1,6)
dados4= randint(1,6)
Jogador2= dados3 + dados4 

print("Dado 1:", dados1)
print("Dado 2:", dados2)
print("Dado 3:", dados3)
print("Dado 4:", dados4)

print("Jogador1:",jogador1)
print("Jogador2:",jogador2)

if jogador1 > jogador2:
     print("Jogador1 venceu!")
 else:
     if jogador2 > jogador1:
          print("jogador2 venceu!")
     else:
          print("Empate!")