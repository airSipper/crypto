# a simple substitution cipher


class Ciphertext:
    """ a class for operations on a substitution ciphertext  """
    def __init__(self):

        self.charset = {
                        'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W',
                        'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S',
                        'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O',
                        'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K',
                        'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                        'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C',
                        'Y': 'B', 'Z': 'A' }

        self.input_str = ""
        self.output_str = ""
        self.mode = 0

    def get_input_str(self):
        """ get text string from user and force uppercase """
        a = str(input("\nEnter the text string:  "))
        a = "".join([i.upper() for i in a])
        self.input_str = a

    def encrypt_or_decrypt(self):
        """ query user for encrypt or decrypt operation """
        a = str(input("\n[e]encrypt or [d]decrypt ??:  "))
        if a == 'e':
            self.mode = 0
        elif a == 'd':
            self.mode = 1
        else:
            print("[*] Invalid choice, please try again.")
            self.encrypt_or_decrypt()

    def encrypt(self):
        """ shift input string: key to value in charset """
        ciphertext = []
        for i in self.input_str:
            if i in self.charset.keys():
                ciphertext.append(self.charset[i])

        self.output_str = "".join([i for i in ciphertext])

    def encrypt_out(self):
        """ break the ciphertext into blocks of 5 chars """
        ct = list(''.join(l + ' ' * (n % 5 == 4) for n, l in enumerate(self.output_str)))
        self.output_str = "".join(i for i in ct)

    def decrypt(self):
        """ decrypt a text that's been encrypted with this cipher """
        plaintext = []
        for i in self.input_str:
            for k, v in self.charset.items():
                if v == i:
                    plaintext.append(k)
        self.output_str = "".join([i for i in plaintext])

    def start(self):

        self.get_input_str()
        self.encrypt_or_decrypt()

        if self.mode == 0:
            self.encrypt()
            self.encrypt_out()
            print("\n{}\n".format(self.output_str))

        if self.mode == 1:
            self.decrypt()
            print("\n{}\n".format(self.output_str))


def main():
    a = Ciphertext()
    a.start()

if __name__ == '__main__':
    main()
