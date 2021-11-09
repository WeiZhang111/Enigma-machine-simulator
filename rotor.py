# this file gives classes for Rotor and Reflector
class Reflector(object):
    def __init__(self, wiring=None):
        
        self.wiring = wiring

    def encode (self, key):
        index = (ord(key) - ord('A'))%26 # real index
        index = (index)%26 

        letter = self.wiring[index] # letter generated

        return letter


class Rotor(object):

    def __init__(self, wiring=None, notch=None, state="A", ring="A"):

        if wiring != None:
            self.wiring = wiring
        else:
            self.wiring="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rwiring = ["0"] * 26
        for i in range(0, len(self.wiring)):
            self.rwiring[ord(self.wiring[i]) - ord('A')]= chr(ord('A') + i)
        
        self.notch = notch
        self.state = state
        self.ring = ring

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if name == 'wiring':
            self.rwiring = ["0"]*26
            for i in range(0,len(self.wiring)):
                self.rwiring[ord(self.wiring[i]) - ord('A')] = chr(ord('A')+i)

    def en_r(self, key):
        DIFF = (ord(self.state) - ord(self.ring))
        index = (ord(key) - ord('A'))%26 # real index
        index = (index + DIFF)%26 
        letter = self.wiring[index] # letter generated
        out = chr(ord('A')+(ord(letter) - ord('A') +26 - DIFF)%26) 
        return out

    def en_l(self, key):
        DIFF = (ord(self.state) - ord(self.ring))
        index = (ord(key) - ord('A'))%26
        index = (index + DIFF)%26
        letter = self.rwiring[index]
        out = chr(ord('A')+(ord(letter) - ord('A') + 26 - DIFF)%26)
        return out

    def turn(self, offset=1):
        self.state = chr((ord(self.state) + offset - ord('A')) % 26 + ord('A'))
        # notchnext = self.state in self.notch


    def at_notch(self):
        return self.state == self.notch


ROTOR_Beta = Rotor(wiring="LEYJVCNIXWPBQMDRTAKZGFUHOS")
ROTOR_Gamma = Rotor(wiring="FSOKANUERHMBTIYCWLQPZXVGJD")
ROTOR_I = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ",notch="Q")
ROTOR_II = Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE",notch="E")
ROTOR_III = Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO",notch="V")
ROTOR_IV = Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB",notch="J")
ROTOR_V = Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK",notch="Z")
REFLECTOR_A = Reflector(wiring="EJMZALYXVBWFCRQUONTSPIKHGD")
REFLECTOR_B = Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT")
REFLECTOR_C = Reflector(wiring="FVPJIAOYEDRZXWGCTKUQSBNMHL")
