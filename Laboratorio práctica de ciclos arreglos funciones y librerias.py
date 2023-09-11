import matplotlib.pyplot as plt
import random

print("Laboratorio de suma acumulativa, Billy Mazariegos")
cantidad=int(input("ingrese la cantidad de números que desea sumar: "))

acumulativa=0
s_acu=[]
colors=[]

for _ in range(cantidad):
    num=float(input("ingrese los números: "))
    acumulativa += num
    s_acu.append(acumulativa)
    color = "#{:02x}{:02x}{:02x}".format(random.randint(50, 255), random.randint(0, 255), random.randint(25, 255))
    colors.append(color)
print("La suma acumulativa de los números es: ", acumulativa)


etiquetas = [str(i+1) for i in range(cantidad)]
plt.bar(etiquetas, s_acu, color=colors)
plt.plot( "K")
plt.xlabel('Número de entrada')
plt.ylabel('Suma acumulativa')
plt.title('Sumas acumulativa')
plt.show()

             