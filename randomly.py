# # uso del random
# import random
# num=random.randint(1, 10)
# for i in range(num):
#     print("ola",i )

# for i in range(10):
#     print(f"{num}x{i}={num*i}")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# import random
# import time

# num0=random.randint(60, 190)
# num1=random.randint(60, 190)
# num2=random.randint(60, 190)
# if num0>num1:
#     print("ha ganado player 1 con ",num0, "de distancia ")
# elif num1>num2:
#     print("ha ganado player 2 con ",num1, "de distancia ")
# elif num2>num0:
#     print("ha ganado player 3 con ",num2, "de distancia ")
# else:
#     print(f"hubo un empate{num0} {num1} {num2} ")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# #tirar u dado
# import random
# dado=random.randint(1,6)
# dado1=random.randint(1,6)

# print(f"los numeros que salieron son de {dado} / {dado1}" )
# if dado==dado1:
#     print("usted se va a la carcel ")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import random
# total=0
# while total<=50:
#     lanzar=input("lanzar el dado porfavor s/: ")
#     if lanzar=="s":
#         dado=random.randint(1,6)
#         dado1=random.randint(1,6)
#         total+=dado+dado1

#         print(f"los numeros que salieron son de ! {dado} ! {dado1} !" )
#         print(f"este es su lugar del tablero  -{total}-" )
#         if dado==dado1:
#             total-=(dado+dado1)
#             print(f"te vas a la carcel se te resta {dado+dado1} y este es su lugar -{total}-")
#     else:
#         print("trata otra vez")
# print("usted gana ")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import random

i=0
num=random.randint(1, 100)
while i<5:
    num1=int(input("pon un numero "))
    if num1>num:
        print("te pasaste")
        i+=1
    elif num1<num:
        print("esta mas adelante ")
        i+=1
    elif num1==num:
        print("acertaste")
        i=5 #break = hace lo mismo que si terminara el algoritmo
print(f"este es el numero {num}")
    