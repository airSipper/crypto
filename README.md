# python-crypt
### a collection of scripts to do with encryption

in no particular order...

[sowpods.txt](./sowpods.txt)
 -- This is an english dictionary. Its ~260,000 words are uppercase. One word/line.

[substitution.py](./substitution.py)
 -- This is a simple substitution cipher. It takes a string from the user,
 strips the punctuation and forces it into uppercase. It then transposes
 the characters and returns the ciphertext in blocks of 5 letters.
 It's also possible to decrypt a ciphertext that has been encoded with this cipher.

[string-from-cosets.py](./string-from-cosets.py)
 -- I'm working on a Vigenere decryption problem and I needed this to reverse a function that shifts
 characters in a ciphertext into co-sets. 

[pwgen.py](./pwgen.py)
 -- This is a really simple password generator. It takes a users name and birth year and combines them with some symbols. It then selects characters at random from that list out to n characters to produce the password.

[ceasarshifts.py](./ceasarshifts.py)
 -- Another simple cipher that returns a dict of all ceasar rotations for a given string. 

[prime-or-composite.py](./prime-or-composite.py)
 -- Shows whether numbers in a range are prime or composite
