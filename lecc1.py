# #Código de Jesús Collantes

class Miexcepcion(Exception):
  pass

def introducirnumero():
  while True:
    try:
      num = int(input("Introduce un número entero: "))
      if num > 10:
        raise Miexcepcion("El número es mayor de 10")
      break
    except ValueError:
      print("Debes introducir un número entero")
    except Miexcepcion as e:
      print(e)
  return num

numero = introducirnumero()
print("El número introducido es", numero)

# # -------------------------------

try:
    with open(r"C:\Users\Sus\Desktop\fichero.txt","r") as file:
        # Leemos el contenido del archivo
        text = file.read()
        # Cerramos el archivo
        file.close()
        print(text)
except:
    print("Error al abrir el archivo.")
finally:
  # Cerramos el archivo en cualquier caso
    file.close()



