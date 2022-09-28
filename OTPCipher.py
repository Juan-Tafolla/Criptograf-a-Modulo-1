class Main():
    def __init__(self):
        
        self.inp_option = input("\n Antes de iniciar, elija una de las siguientes opciones: \n [1] Cifrar \n [2] Descifrar \n Opcion: ")
        self.ct = ''
        
        self.vocab = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ'   
        self.inp_option = int(self.inp_option)
        
        if self.inp_option == 1:
            print("\n ---------------------------------------------------------------------------------- \n \t\t ENCRIPTACION OTP")
            self.pt = input('\nIngrese el texto plano: ')
            self.ck = input('\n\nIngrese la llave: ')
            
            check = self.check_input()
            if check == True:
                self.cipher()
                
        elif self.inp_option == 2:
            print("\n ---------------------------------------------------------------------------------- \n \t\t DESCIFRADOR OTP")
            self.pt = input('\nIngrese el texto cifrado: ')
            self.ck = input('\nIngrese la llave: ')
            
            check = self.check_input()
            if check == True:
                self.decipher()
    
    def check_input(self):
        
        if all(x.isalpha() or x.isspace() for x in self.pt) and all(x.isalpha() or x.isspace() for x in self.ck):
            if len(self.ck) != len(self.pt):
                print('\n[ERROR] El Cifrado OTP requiere que la llave y el texto sean de la misma longitud en caracteres!\n')
                chekerr = False
                return chekerr
            else:
                chekerr = True
                return chekerr
        else:
            print('\n[ERROR] Solo ingrese letras y espacios\n')
            chekerr = False
            return chekerr
    
    def cipher(self):
        for idx,x in enumerate(self.pt):
            
            if x == ' ':
                self.ct += ' '
                continue    
           
            min_check = x.islower()
            
            if min_check == True:
                x = x.upper()
           
            xi = self.vocab.find(x) 
            y = self.ck[idx]
            y = y.upper()
            yi = self.vocab.find(y)      
            res = self.vocab[(xi+yi)%33]
            
            if min_check == True:
                res = res.lower() 
            
            self.ct += res
            print(self.ct)
            
        print("\nTexto cifrado: " + self.ct)

    def decipher(self):
        for idx,x in enumerate(self.pt):
            
            if x == ' ':
                self.ct += ' '
                continue    
           
            min_check = x.islower()
            
            if min_check == True:
                x = x.upper()
           
            xi = self.vocab.find(x) 
            y = self.ck[idx]
            y = y.upper()
            yi = self.vocab.find(y)      
            res = self.vocab[(xi-yi)%33]
            
            if min_check == True:
                res = res.lower() 
            
            self.ct += res
            print(self.ct)
            
        print("\nTexto descifrado: " + self.ct)

if __name__ == '__main__':
    app = Main()
