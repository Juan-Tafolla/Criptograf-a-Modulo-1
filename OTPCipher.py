
class Main:
    def __init__(self):
    
        pt = input('\nIngrese el texto plano: ')
        key = input('\n\n Ingrese la llave para cifrar: ')

        pt = pt.upper()
        self.pt = pt.strip()
        key = key.upper()
        self.key = key.strip()

        self.mayus = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ'
        self.minus = 'abcdefghijklmnñopqrstuvwxyzáéíóúü'
        self.i = 0
        self.j = 0
        
        self.mayus_uni = []
        self.minus_uni = []
        self.dict_mayus = {}
        self.dict_minus = {}
        
        self.pt = 'B'
        self.plain_uni = []
        self.ck = 'K'
        self.ciphkey_uni = []
        
        self.mayus_to_unicode()
        self.mayus_to_dict()
        
        self.minus_to_unicode()
        self.minus_to_dict()

        self.pt_to_uni()
        self.ck_to_uni()

        
        for idx in self.plain_uni:
            

            val_list = list(self.dict_mayus.values())
            self.pt_position = val_list.index(idx)

        
        for idx in self.ciphkey_uni:
            
            # key_list = list(self.dict_mayus.keys())
            val_list = list(self.dict_mayus.values())
            self.ck_position = val_list.index(idx)
            
        self.ct_uni = self.ck_position + self.pt_position
        self.ct_plain = self.dict_mayus[self.ct_uni]
        print(chr(int(self.ct_plain)))
        
        
    def mayus_to_unicode(self):
        for char in self.mayus:
            unic = str(ord(char))
            if unic == '32':
                pass
            self.mayus_uni += [unic]
        
    def minus_to_unicode(self):
            
        for char in self.minus:
            unic = str(ord(char))
            if unic == '32':
                pass
            self.minus_uni += [unic]
            
    def mayus_to_dict(self):
        
        for unic in self.mayus_uni:
            self.dict_mayus[self.i] = unic
            self.i +=1
        
    def minus_to_dict(self):

        for unic in self.minus_uni:
            self.dict_minus[self.j] = unic
            self.j +=1

    def pt_to_uni(self):
        for char in self.pt:
            unic = str(ord(char))
            if unic == '32':
                pass
            self.plain_uni += [unic]
            
    def ck_to_uni(self):
        for char in self.ck:
            unic = str(ord(char))
            if unic == '32':
                pass
            self.ciphkey_uni += [unic]        


if __name__ == '__main__':
    app = Main()
