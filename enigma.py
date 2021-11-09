# this file gives encoding machine classes
from rotor import *

#Enigma class is for 3-rotor setting
class Enigma(object):

    def __init__(self, reflector, rotor1, rotor2, rotor3, key="AAA", plugs="", ring="AAA"):

        self.reflector = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3

        self.rotor1.state = key[0]
        self.rotor2.state = key[1]
        self.rotor3.state = key[2]
        self.rotor1.ring = ring[0]
        self.rotor2.ring = ring[1]
        self.rotor3.ring = ring[2]


        plugboard_settings= [(i[0], i[1]) for i in plugs.split()]

        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ALPHABET_out = [" "] * 26
        for i in range(len(ALPHABET)):
            ALPHABET_out[i] = ALPHABET[i]
        for k, l in plugboard_settings:
            ALPHABET_out[ord(k)-ord('A')] = l
            ALPHABET_out[ord(l)-ord('A')] = k

        
        self.transtab = str.maketrans(ALPHABET, "".join(ALPHABET_out))
        

    def encipher(self, text_in):

        output = ''
        plaintext_in_upper = text_in.upper()
        plaintext = plaintext_in_upper.translate(self.transtab)
        for w in plaintext:

            
            if not w.isalpha():
                output = output + w
                continue

            if self.rotor3.at_notch():
                if self.rotor2.at_notch():
                    self.rotor1.turn()
                self.rotor2.turn()


            self.rotor3.turn()

            out1 = self.rotor3.en_r(w)
            out1 = self.rotor2.en_r(out1)
            out1 = self.rotor1.en_r(out1)
            out1 = self.reflector.encode(out1)
            out1 = self.rotor1.en_l(out1)
            out1 = self.rotor2.en_l(out1)
            out1 = self.rotor3.en_l(out1)
            output += out1

        result = output.translate(self.transtab)

        rtn = ""
        for idx, elem in enumerate(result):
            if text_in[idx].islower():
                rtn += elem.lower()
            else:
                rtn += elem
        return rtn

#Enigma4 class is for 4-rotor setting
class Enigma4(object):

    def __init__(self, reflector, rotor1, rotor2, rotor3, rotor4, key="AAA", plugs="", ring="AAA"):

        self.reflector = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.rotor4 = rotor4

        self.rotor1.state = key[0]
        self.rotor2.state = key[1]
        self.rotor3.state = key[2]
        self.rotor4.state = key[3]

        self.rotor1.ring = ring[0]
        self.rotor2.ring = ring[1]
        self.rotor3.ring = ring[2]
        self.rotor4.state = key[3]

        plugboard_settings= [(i[0], i[1]) for i in plugs.split()]

        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ALPHABET_out = [" "] * 26
        for i in range(len(ALPHABET)):
            ALPHABET_out[i] = ALPHABET[i]
        for k, l in plugboard_settings:
            ALPHABET_out[ord(k)-ord('A')] = l
            ALPHABET_out[ord(l)-ord('A')] = k

        
        self.transtab = str.maketrans(ALPHABET, "".join(ALPHABET_out))
        

    def encipher(self, text_in):

        output = ''
        plaintext_in_upper = text_in.upper()
        plaintext = plaintext_in_upper.translate(self.transtab)
        for w in plaintext:

            
            if not w.isalpha():
                output = output + w
                continue

            if self.rotor4.at_notch():
                if self.rotor3.at_notch():
                    if self.rotor2.at_notch():
                        self.rotor1.turn()
                    self.rotor2.turn()
                self.rotor3.turn()
                


            self.rotor4.turn()

            out1 = self.rotor3.en_r(w)
            out1 = self.rotor2.en_r(out1)
            out1 = self.rotor1.en_r(out1)
            out1 = self.reflector.encode(out1)
            out1 = self.rotor1.en_l(out1)
            out1 = self.rotor2.en_l(out1)
            out1 = self.rotor3.en_l(out1)
            output += out1

        result = output.translate(self.transtab)

        rtn = ""
        for idx, elem in enumerate(result):
            if text_in[idx].islower():
                rtn += elem.lower()
            else:
                rtn += elem
        return rtn