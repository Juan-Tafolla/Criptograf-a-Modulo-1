
class Main:
    def __init__(self):
    
        pt = input('\nIngrese el texto plano: ')
        key = input('\n\n Ingrese la llave para cifrar: ')

        pt = pt.upper()
        self.pt = pt.strip()
        key = key.upper()
        self.key = key.strip()

        self.opt_cipher()

    def opt_cipher(self):
        idx = 0
        for i in self.pt:
            self.cp = i ^ self.key[idx]
            print(self.cp)
        
    def opt_decipher(self):
        self.pt = self.cp[i] ^ self.key[i]
        
if __name__ == '__main__':
    app = Main()
