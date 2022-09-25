import numpy as np 
from egcd import egcd

abc = "abcdefghijklmnopqrstuvwxyz"
to_int = dict(zip(abc, range(len(abc))))
to_letter = dict(zip(range(len(abc)), abc))


def matriz_inversa(matriz, modulo):
    determina = int(np.round(np.linalg.det(matriz)))
    det_inv = egcd(determina, modulo)[1] % modulo
    mat_inv = (det_inv * np.round(determina * np.linalg.inv(matriz)).astype(int) % modulo)
    return mat_inv

def cifrar (mensaje, llave2):
    men_cifrado = ""
    men_numero = []
    for letra in mensaje:
        men_numero.append(to_int[letra])
    texto_numero = [men_numero[i : i + int(llave2.shape[0])]
         for i in range (0, len(men_numero), int(llave2.shape[0]))
         ]

    for a in texto_numero:
        a = np.transpose(np.asarray(a))[:, np.newaxis]

        while a.shape[0] != llave2.shape[0]:
            a = np.append(a, to_int[" "])[: np.newaxis]

        numeros = np.dot(llave2, a) % len(abc)
        longitud = numeros.shape[0]     #Longitud de caracteres del mensaje cifrado 

        #Se regresa el mensaje ya cifrado
        for b in range(longitud):
            numero_act = int(numeros[b,0])
            men_cifrado += to_letter[numero_act]
    return men_cifrado


def decifrar(mensaje, llaveinv):
    mensaje_desifrado = ""
    cifrado_numero = []

    for letra in mensaje:
        cifrado_numero.append(to_int[letra])

    longitud_abc = [
        cifrado_numero[i : i + int(llaveinv.shape[0])]
        for i in range(0, len(cifrado_numero), int(llaveinv.shape[0]))
    ] 

    for c in longitud_abc:
        c = np.transpose(np.asarray(c))[:, np.newaxis]
        numeros = np.dot(llaveinv, c) % len(abc)
        longitud_caracteres = numeros.shape[0]

        for d in range(longitud_caracteres):
            numero_act_2 = int(numeros[d, 0])
            mensaje_desifrado += to_letter[numero_act_2]
    
    return mensaje_desifrado


def main():
    mensaje_claro = input("Escribe una palabra con 6 letras: ")
    #mensaje_claro = "fausto"
    llave = np.matrix([[6, 15, 18], [19, 1, 11], [4, 25, 1]])
    llaveinv = matriz_inversa(llave, len(abc))
    criptograma = cifrar(mensaje_claro, llave)
    criptograma_mensaje_claro = decifrar(criptograma, llaveinv)
    print("mensaje claro : "+ mensaje_claro)
    print("mensaje cifrado : "+ criptograma)
    print("Mensaje desifrado :"+ criptograma_mensaje_claro)
    print(llaveinv)
    
main()
