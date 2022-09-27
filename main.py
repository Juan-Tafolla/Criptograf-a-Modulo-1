#####################################################################
#### Primer proyecto del modulo 1 de la asignatura de criptografia
# 
# Integrantes del equipo:
#       - Avalos Villarruel Isaac Naason
#       - Mora Carbajal Erick Fernando
#       - Tafolla Fraga Juan Pablo
#
#####################################################################

import HillCipher as hill
import PlayfairCipher as plfr
import OTPCipher as otp


class Main:
  
    eleccion = input("Elige cual metodo quieres usar para codificar \n\n1. Cifrado HillCipher \n2. Cifrado PlayCipher \n3. Cifrado OtpCipher\n")
    
    if(eleccion == "1"):
        print(hill.main())
        quit()
    if(eleccion == "2"):
        print(plfr.main())
        quit()
    if(eleccion == "3"):
        print(otp.Main())
        quit()
    else:
        print("Opcion invalida")


if __name__ == '__main__':
    app = Main()

