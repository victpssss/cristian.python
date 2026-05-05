g=int(input("cuantos gramos tiene tu lata: "))
s=int(input("cual es el porcentaje de sodio(1%/100%): "))
p=int(input("donde lo va a vender? nacional-1/internacional-2 : "))
if g<500:
    print("-su lata es tamaño normal-")
    lata="normal"
elif g<=1500:
    print("-su lata es tamaño mediano-")
    lata="mediano"
elif g>=1500:
    print("-su lata es tamaño grande-")
    lata="grande"

if s<5:
    print("-su lata queda normal-")
    sodio="su lata queda igual"
elif s>=5 and s<=8:
    print("-es una lata especial-")
    sodio="especial"
elif s>9:
    print("-es una lata acorazada-")
    sodio="acorazada"

if p==1:
    print("-su lata no necesita sticker- ")
    pais="su lata no necesita sticker"
elif p==2:
    print("-su lata necesita esticker sanitario-")
    pais="necesita un stiker sanitario"


print(f"su lata es {lata} gr{g} {sodio} cantidad de sodio %{s} y {pais}")






