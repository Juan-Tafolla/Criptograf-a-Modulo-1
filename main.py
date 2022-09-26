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
import tkinter as tk
from tkinter import *


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


    """def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title("Hopfield")
        self.root.wm_minsize(width=500, height=500)
        self.root.wm_resizable(width=False, height=False)
        self.canvas = Canvas(width=500, height=500, bg='white')
    """ 

    #def draw_canvas(self):
        
    
    #def blip_canvas(self):
        
    #def start(self):
     #   tk.mainloop()   
    

if __name__ == '__main__':
    app = Main()

