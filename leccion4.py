#Código de Jesús Collantes
#Ejercicio 1
import random

lista = [[int(random.random()*100) for i in range(20)],[int(random.random()*10) for i in range(5)],\
        [int(random.random()*20) for i in range(10)]]

maximo =[max(i) for i in lista]

print(f"\nDe la lista {lista} \nsus maximos son {maximo}")

#Ejercicio 2

def par(n):
  return n % 2 == 0

numeros = [int(random.random()*100) for i in range(20)]
pares = filter(par, numeros)
print(f"\n\nLos numeros pares de la lista {numeros} \nson: {list(pares)}")