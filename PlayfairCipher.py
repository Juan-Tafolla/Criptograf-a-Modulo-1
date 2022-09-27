import numpy as np

matriz = ['@', 'I', 'S', 'A', 'Á', 'C', 'N', 'B', 'D', 'É', 'O', 'F', 'G', 'V', 'H', 'L', 'Í',
 'J', 'K', 'M', 'Ñ', 'Ó', 'P', 'R', 'Q', 'U', 'E', 'T', 'Ú', 'Ü', '#', 'W', 'X', 'Y', 'Z', '&']
matriz = np.array(matriz)
matriz = matriz.reshape((6,6))

def cifrar(pt = ""):
  text = pt
  print("El mensaje que quieres cifrar es "+text)
  print("Matriz utilizada:")
  print(matriz)
  text = text.upper().replace(" ","")
  b=1

  for a in text:
    if a == text[b]:
      par = a + text[b]
      text = text.replace(par, a + "#" + text[b])
      b+=1
    else:
      b+=1

  if (len(text) % 2) != 0:
    text = text + "@"

  textC = ""
  x = 0
  while x < len(text):
    index1 = np.where(matriz == text[x])
    index2 = np.where(matriz == text[x+1])
    if int(index1[0]) == int(index2[0]):
      if int(index1[1]) == 5:
        textC = textC + str(matriz[int(index1[0]), 0]) + str(matriz[int(index2[0]), int(index2[1])+1])
      elif int(index2[1]) == 5:
        textC = textC + str(matriz[int(index1[0]), int(index1[1])+1]) + str(matriz[int(index2[0]), 0])
      else:
        textC = textC + str(matriz[int(index1[0]), int(index1[1])+1]) + str(matriz[int(index2[0]), int(index2[1])+1])
    elif int(index1[1]) == int(index2[1]):
      if int(index1[0]) == 5:
        textC = textC + str(matriz[0, int(index1[1])]) + str(matriz[int(index2[0])+1, int(index2[1])])
      elif int(index2[0]) == 5:
        textC = textC + str(matriz[int(index1[0])+1, int(index1[1])]) + str(matriz[0,int(index2[1])+1])
      else:
        textC = textC + str(matriz[int(index1[0])+1, int(index1[1])]) + str(matriz[int(index2[0])+1, int(index2[1])])
    elif int(index1[0]) > int(index2[0]):
      if int(index1[1]) > int(index2[1]):
        textC = textC + str(matriz[int(index1[0]),int(index2[1])]) + str(matriz[int(index2[0]),int(index1[1])])
      else:
        textC = textC + str(matriz[int(index2[0]),int(index1[1])]) + str(matriz[int(index1[0]),int(index2[1])])
    elif int(index1[0]) < int(index2[0]):
      if int(index1[1]) < int(index2[1]):
        textC = textC + str(matriz[int(index1[0]),int(index2[1])]) + str(matriz[int(index2[0]),int(index1[1])])
      else:
        textC = textC + str(matriz[int(index2[0]),int(index1[1])]) + str(matriz[int(index1[0]),int(index2[1])])
    if (x % 4) != 0:
      textC = textC + " "
    x +=2
  print("El mensaje cifrado es "+textC)
  return()

def decifrar(ct = ""):
  textC = ct
  print("El mensaje que quieres descifrar es "+textC)
  print("Matriz utilizada:")
  print(matriz)
  textC = textC.upper().replace(" ","")
  
  textD = ""
  x = 0
  while x < len(textC):
    index1 = np.where(matriz == textC[x])
    index2 = np.where(matriz == textC[x+1])
    if int(index1[0]) == int(index2[0]):
      if int(index1[1]) == 0:
        textD = textD + str(matriz[int(index1[0]), 5]) + str(matriz[int(index2[0]), int(index2[1])-1])
      elif int(index2[1]) == 0:
        textD = textD + str(matriz[int(index1[0]), int(index1[1])-1]) + str(matriz[int(index2[0]), 5])
      else:
        textD = textD + str(matriz[int(index1[0]), int(index1[1])-1]) + str(matriz[int(index2[0]), int(index2[1])-1])
    elif int(index1[1]) == int(index2[1]):
      if int(index1[0]) == 0:
        textD = textD + str(matriz[5, int(index1[1])]) + str(matriz[int(index2[0])-1, int(index2[1])])
      elif int(index2[0]) == 0:
        textD = textD + str(matriz[int(index1[0])-1, int(index1[1])]) + str(matriz[5,int(index2[1])-1])
      else:
        textD = textD + str(matriz[int(index1[0])-1, int(index1[1])]) + str(matriz[int(index2[0])-1, int(index2[1])])
    elif int(index1[0]) > int(index2[0]):
      if int(index1[1]) > int(index2[1]):
        textD = textD + str(matriz[int(index2[0]),int(index1[1])]) + str(matriz[int(index1[0]),int(index2[1])])
      else:
        textD = textD + str(matriz[int(index1[0]),int(index2[1])]) + str(matriz[int(index2[0]),int(index1[1])])
    elif int(index1[0]) < int(index2[0]):
      if int(index1[1]) < int(index2[1]):
        textD = textD + str(matriz[int(index2[0]),int(index1[1])]) + str(matriz[int(index1[0]),int(index2[1])])
      else:
        textD = textD + str(matriz[int(index1[0]),int(index2[1])]) + str(matriz[int(index2[0]),int(index1[1])])
    if (x % 4) != 0:
      textD = textD + " "
    x +=2
  print("El mensaje descifrado es "+textD)
  return()


class main:
  select = int(input("/nQue desea hacer?/n/n1. Cifrar/n2. Descifrar/n3. Salir"))
  while select != 3:
    if select == 1:
      mensaje == input("Inserte el mensaje que desea cifrar")
      cifrar(mensaje)
    elif select == 2:
      mensaje == input("Inserte el mensaje que desea descifrar")
      decifrar(mensaje)
    elif select == 3:
      return()
    else:
      print("Inserte una opcion valida")
    select = int(input("/nQue desea hacer?/n/n1. Cifrar/n2. Descifrar/n3. Salir"))


