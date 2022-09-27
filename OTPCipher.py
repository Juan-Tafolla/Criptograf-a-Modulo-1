
class Main:
    def __init__(self):
        
        self.pt = input('\nIngrese el texto plano: ')
        self.ck = input('\n\nIngrese la llave: ')

        self.vocab = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ'
        self.dictionary = {}
        self.plain_uni = []
        self.ciphkey_uni = []

        self.cipher()
    
    def dict(self):
        for idx,char in enumerate(self.vocab):
            ucode = str(ord(char))
            if ucode == '32':
                continue
            self.dictionary[idx] = ucode
        

    def pt_to_uni(self):
        for char in self.pt:
            ucode = str(ord(char))
            if ucode == '32':
                continue
            self.plain_uni += [ucode]
            
    def ck_to_uni(self):
        for char in self.ck:
            ucode = str(ord(char))
            if ucode == '32':
                continue
            self.ciphkey_uni += [ucode]

    def cipher(self):
        self.dict()
        self.pt_to_uni()
        self.ck_to_uni()

        for idx in self.plain_uni:
        
            val_list = list(self.dictionary.values())
            self.pt_position = val_list.index(idx)
        
        for idx in self.ciphkey_uni:
            # key_list = list(self.dict_mayus.keys())
            val_list = list(self.dictionary.values())
            self.ck_position = val_list.index(idx)
            
        self.ct_uni = ( self.ck_position + self.pt_position ) % 33
        self.ct_plain = self.dictionary[self.ct_uni]  
        print("\n\nEl texto cifrado es: " + chr(int(self.ct_plain)) + '\n')


if __name__ == '__main__':
    app = Main()
