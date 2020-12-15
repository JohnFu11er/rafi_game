import os
import platform
import time
import random

computer_os = platform.system()

class Character():
    def __init__(self, char_name):
        name = char_name.split(" ")
        final_name = str()
        for word in name:
            final_name += (word.upper()[:1] + word.lower()[1:]) + " "
        self._name = final_name[:-1]
    
    def dead(self, dead_player):
        print(f"{dead_player._name} is dead!")
        
    def fight_choice(self, opponent):
    
        def fight(self, opponent):
            clear_screen()
            print(f"{self._name} has chosen to stay and fight the {opponent._name}.")
            while True:
                # Your turn
                print(f"You swing your mighty {self._weapon}...")
                time.sleep(2)
                if random.randrange(0,100) > 30:
                    print(f"and do {self._ap} of damage to {opponent._name}.")
                    opponent._hp -= self._ap
                    if opponent._hp <= 0:
                        Character.dead(self,opponent)
                        exit()
                else:
                    print(f"but you miss {opponent._name} and do no damage.")
                time.sleep(2)
                
                # Opponent's turn
                print(f"{opponent._name} attacks!")
                time.sleep(2)
                if random.randrange(0,100) > 30:
                    print(f"and does {opponent._ap} of damage.")
                    self._hp -= opponent._ap
                    if self._hp <= 0:
                        Character.dead(self, opponent)
                        exit()
                else:
                    print(f"but {opponent._name} misses, and does no damage.")
                time.sleep(2)
            
        def run_away(self):
            clear_screen()
            print(f"{self._name} has chosen to run from the {opponent._name}.")
            
        while True:
            choice = input(f"Do you want to the fight the {opponent._name}? (y/n): ")
            if choice == "n":
                run_away(self)
                exit()
            if choice == "y":
                fight(self, opponent)
                exit()
            else:
                print(f'Please enter "y" or "n"\n')
                time.sleep(3)

    def heal(self):
        self._hp = self._stats["hp"]
        print(f"{self._name} runs away")
        print(f"{self._name} has been healed! HP has been restored to {self._hp}")

    def future_use(self):
        def level_up(self):
            print(f"{self._name} has leveled up")    

        def attack_with_weapon(self):
            pass
        
        def attack_with_magic(self):
            pass
                
class Warrior(Character):
    def __init__(self, char_name):
        super().__init__(char_name)
        self._stats = {
            "hp" : 100,
            "mp" : 20,
            "ap" : 10
        }
        self._hp = self._stats["hp"]
        self._mp = self._stats["mp"]
        self._ap = self._stats["ap"]
        self._weapon = "sword"
    
class Mage(Character):
    def __init__(self, char_name):
        super().__init__(char_name)
        self._stats = {
            "hp" : 70,
            "mp" : 50,
            "ap" : 5
        }
        self._hp = self._stats["hp"]
        self._mp = self._stats["mp"]
        self._ap = self._stats["ap"]
        self._weapon = "magic wand"
    
class Enemy(Character):
    def __init__(self, char_name, hp, mp, ap):
        super().__init__(char_name)
        self._stats = {
            "hp" : hp,
            "mp" : mp,
            "ap" : ap
        }
        self._hp = self._stats["hp"]
        self._mp = self._stats["mp"]
        self._ap = self._stats["ap"]

def clear_screen():
    if computer_os == "Windows":
        os.system('cls')
    if computer_os == "Linux":
        os.system('clear')