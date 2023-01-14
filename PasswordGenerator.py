#XIST

#Password-Generator

import itertools

class PasswordGenerator:
   
    def __init__(self, possible_combination: int, combination_type: int):
   
        self.possible_combination = possible_combination
   
        self.combination_type = combination_type
   
        self.special = '!"#$%&\'()*+,-. /:;?@[]^_`{|}~'
   
        self.numeric = '0123456789'
   
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   
        self.get_carecter = ""
        
    def generate_get_carecter(self):
   
        if self.combination_type == 1:
   
            self.get_carecter = self.numeric

        elif self.combination_type == 2:
   
            self.get_carecter = self.alphabet

        elif self.combination_type == 3:
   
            self.get_carecter = self.special

        elif self.combination_type == 4:
   
            self.get_carecter = self.numeric + self.alphabet
        
        elif self.combination_type == 5:
   
            self.get_carecter = self.special + self.numeric
        
        elif self.combination_type == 6:
   
            self.get_carecter = self.special + self.alphabet

        elif self.combination_type == 7:
   
            self.get_carecter = self.special + self.numeric + self.alphabet
        
        else:
   
            raise ValueError("Invalid Password Type")

    def generate_password(self):
   
        for x in itertools.product(*([self.get_carecter] * self.possible_combination)):
   
            yield ''.join(x)

    def write_to_file(self):
   
        with open("password_list.txt", "w") as file:
   
            for i, password in enumerate(self.generate_password()):
   
                file.write(password + "\n")
   
                print(f"{i+1} possible combination: {password}")


print(".................................................................\n.....==......==.....==========.....==========.....==========.....\n.......==..==...........==.........==.................==.........\n.........==.............==.........==========.........==.........\n.......==..==...........==.................==.........==.........\n.....==......==.....==========.....==========.........==.........\n.....Password-Generator..........................................") 

possible_combination = int(input("Password Length ... ?: "))

print("1: Numbers")

print("2: Charecters")

print("3: Special")

print("4: Numbers + Charecters")

print("5: Numbers + Special")

print("6: Charecters + Special")

print("7: Special + Numbers + Charecters")

combination_type = int(input("Password Type (1-6): "))

generator = PasswordGenerator(possible_combination, combination_type)

generator.generate_get_carecter()

generator.write_to_file()

#XIST