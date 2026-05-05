import random
import time
plan=0
lata=0
can=random.randint(10,20)
print("pescaste esta cantidad de peces =",can)
for i in range(can):
    pez=random.randint(1,1600)
    time.sleep(0.5)
    if pez>=800:
        plan+=1
        print(f"este pez se va a la plancha y su peso es de {pez} y esta cantidad se va a la plancha -{plan}-")
        
    elif pez<=800:
        lata+=1
        print(f"este pez se va a la lata y su peso es de {pez} y esta cantidad se va ahi -{lata}-")
print(f"esta cantidad de planchas -{plan}- y esta es de lata -{lata}- ")
        
        

