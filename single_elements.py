# This script provides classes for Plugboard, PlugLeaed, single (simple) rotor and reflector
# ------------------------------------------------------------------------------------------------------------------------------------------
class PlugLead:
    def __init__(self, mapping):
        # Your code here  
        self.mapping = mapping   

    def encode(self, character):
        # Your code here
                            
        if character == self.mapping[0]:             # PlugLead.encode("A") should return "G"；PlugLead.encode("G") should return "A" 
            return self.mapping[1]
        elif character == self.mapping[1]:
            return self.mapping[0]
        else:
            return character                         # PlugLead.encode("D") should return "D" since it only connects A and G (i.e. the mapping)
# ------------------------------------------------------------------------------------------------------------------------------------------
class Plugboard:
    # Your code here
    def __init__(self):
        self.mapping_pairs = []

    def add(self, obj):
        if obj not in self.mapping_pairs:
            self.mapping_pairs.append(obj.mapping)

    def encode(self, char):
        for i in self.mapping_pairs:
            if (char in i):
                if char == i[0]:
                    return i[1]
                else:
                    return i[0] 
        return char
# ------------------------------------------------------------------------------------------------------------------------------------------
# Define wirings as a dictionary
Rotor_wirings = {
    'Beta':  'LEYJVCNIXWPBQMDRTAKZGFUHOS',
    'Gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD',
    'I':     'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
    'II':    'AJDKSIRUXBLHWTMCQGZNPYFVOE',
    'III':   'BDFHJLCPRTXVZNYEIWGAKMUSQO',
    'IV':    'ESOVPZJAYQUIRHXLNFTGKDCMWB',
    'V':     'VZBRGITYUPSDNHLXAWMJQOFECK',
    'A':     'EJMZALYXVBWFCRQUONTSPIKHGD',
    'B':     'YRUHQSLDPXNGOKMIEBFZCWVJAT',
    'C':     'FVPJIAOYEDRZXWGCTKUQSBNMHL'
}
# ------------------------------------------------------------------------------------------------------------------------------------------
# Define Notch positions of each rotor as a dictionary
Notch_positions = {
    'I':    'Q',
    'II':   'E',
    'III':  'V',
    'IV':   'J',
    'V':    'Z',
    'Beta': 'None',
    'Gamma':'None'
}
# ------------------------------------------------------------------------------------------------------------------------------------------
# Try simple version Rotor to test the code works
class Rotor1:
    def __init__(self, name):
        self.name = name
        self.wiring = Rotor_wirings[name]
        self.rwiring = ["0"] * 26
        for i in range(0, len(self.wiring)):
            self.rwiring[ord(self.wiring[i]) - ord('A')]= chr(ord('A') + i)     

    def encode_right_to_left(self, key):
        index = (ord(key) - ord('A'))%26 
        return self.wiring[index] 

    def encode_left_to_right(self, key):
        index = (ord(key) - ord('A'))%26
        return self.rwiring[index]
# ------------------------------------------------------------------------------------------------------------------------------------------
# Try simple version Reflector to test the code works
class Reflector1(object):
    def __init__(self, name):
        self.name = name
        self.wiring = Rotor_wirings[name]

    def encipher (self, key):
        index = (ord(key) - ord('A'))%26 
        return self.wiring[index] 