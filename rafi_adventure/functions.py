import os
import platform
import time
import random
import json

computer_os = platform.system()

# Fetch enemy data from JSON file
with open('./rafi_adventure/enemies.json', mode='rt') as _data:
    enemy_data = json.loads(_data.read())

class Character():
    def __init__(self, char_name):
        name = char_name.split(" ")
        final_name = str()
        for word in name:
            final_name += (word.upper()[:1] + word.lower()[1:]) + " "
        self._name = final_name[:-1]
    
    def dead(self):
        Game_env.show_character_status(self,1,2)
        print(f"{self._name} is dead!")    
        
    def fight(self, opponent):
        Game_env.show_character_status(self,1,0)
        print(f"{self._name} leaps from cover to fight the {opponent._name}.")
        while True:
            # Your turn
            Game_env.show_character_status(self,1,2)
            print(f"You swing your mighty {self._weapon}...")
            time.sleep(2)
            if random.randrange(0,100) > 30:
                print(f"and do {self._dp} damage to the {opponent._name}.")
                opponent._hp -= self._dp
            else:
                print(f"but you miss the {opponent._name} and do no damage.")
            if opponent._hp <= 0:
                Character.dead(opponent)
                return
            
            # Opponent's turn
            Game_env.show_character_status(self,1,2)
            print(f"{opponent._name} attacks...")
            time.sleep(2)
            if random.randrange(0,100) > 30:
                print(f"and does {opponent._dp} damage to {self._name}.")
                self._hp -= opponent._dp
            else:
                print(f"but the {opponent._name} misses, and does no damage.")
            if self._hp <= 0:
                Character.dead(self)
                return

    def fight_choice(self, opponent):
        while True:
            choice = input(f"Do you want to the fight the beast? (y/n): ")
            if choice == "n":
                Character.run_away(self)
            elif choice == "y":
                Character.fight(self, opponent)
                return
            else:
                print(f'Please enter "y" or "n"\n')
                time.sleep(3)
        
    def run_away(self, opponent):
        Game_env.show_character_status(self,1,2)
        print(f"{self._name} has chosen to run from the {opponent._name}.")

    def heal(self):
        self._hp = self._stats["hp"]
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
            "dp" : 10
        }
        self._hp = self._stats["hp"]
        self._mp = self._stats["mp"]
        self._dp = self._stats["dp"]
        self._weapon = "sword"
    
class Mage(Character):
    def __init__(self, char_name):
        super().__init__(char_name)
        self._stats = {
            "hp" : 70,
            "mp" : 50,
            "dp" : 5
        }
        self._hp = self._stats["hp"]
        self._mp = self._stats["mp"]
        self._dp = self._stats["dp"]
        self._weapon = "battle staff"
    
class Enemy(Character):
    def __init__(self, char_name):
        self._name = char_name
        self._stats = {
            "hp" : enemy_data[self._name]['hp'],
            "mp" : enemy_data[self._name]['mp'],
            "dp" : enemy_data[self._name]['dp'],
        }
        self._hp = self._stats["hp"]
        self._mp = self._stats["mp"]
        self._dp = self._stats["dp"]

class Game_env():
    
    def clear_screen(self):
        if computer_os == "Windows":
            os.system('cls')
        if computer_os == "Linux":
            os.system('clear')
    
    
    def show_character_status(self, clear, wait_time):
        ''' Clears screen, and displays status of character(self).
        
            Parameters:
                clear (bool) -- Clears screen if True.
                wait_time (int) -- # of seconds to sleep the screen.
        
            Returns: None
        
        '''
        
        if wait_time:
            time.sleep(int(wait_time))
        if clear:
                Game_env.clear_screen(None)
        print(f"{self._name} | HP: {self._hp} | MP: {self._mp} | DP: {self._dp}\n")
        