import numpy as np

matriz = ['@', 'I', 'S', 'A', '�', 'C', 'N', 'B', 'D', '�', 'O', 'F', 'G', 'V', 'H', 'L', '�',
 'J', 'K', 'M', '�', '�', 'P', 'R', 'Q', 'U', 'E', 'T', '�', '�', '#', 'W', 'X', 'Y', 'Z', '&']
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
  cifrar("erick")
  decifrar("erick")


if __name__ == '__main__':
  app = main()