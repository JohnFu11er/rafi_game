import time
import random
from functions import *


def main():
    while True:
        char_setup()
        level_1()
        # level_2()
        # level_3()
        # testing()
        play_again()

# Global vars
player_1 = str()

def char_setup():
    global player_1
    
    # Define character name
    Game_env.clear_screen(None)
    char_name = input("What is your character's name: ")
    
    # Define character type
    char_sel = ()
    while not char_sel:
        Game_env.clear_screen(None)
        print("Character Selection")
        print("*******************")
        print("1. Warrior")
        print("2. Mage")
        print("\n")
        char_sel = input("Enter the number of your character type: ")
        
        # Input validation
        if char_sel == '1':
            # Warrior
            player_1 = Warrior(char_name)
        elif char_sel == '2':
            # Mage
            player_1 = Mage(char_name)
        else:
            Game_env.clear_screen(None)
            print(f'"{char_sel}" is not a valid selection.\n')
            print('Select "1" if you want to be a Warrior.')
            print('Select "2" if you want to be a Mage.')
            char_sel = ()
            time.sleep(5)
            
        
def level_1():
    Game_env.show_character_status(player_1,1,0)
    print("You wake up near a hedge on the edge of a grove. You hear a rustling")
    print("in the forest across the grove as trees sway from the movements of a")
    print("large creature. As you crouch behind a nearby bush, the great beast")
    print("comes into view. It's huge form stands before you as you decide what")
    print("to do next.\n")
    possible_enemies = [
        Enemy('Great Frost Dragon'),
        Enemy('Fluffy Puppy'),
        Enemy('Monolith')
        ]
    Character.fight_choice(
        player_1, random.choice(possible_enemies)
        )


def level_2():
    print("This is level 2.")
    
    
def level_3():
    print("This is level 3.")


def play_again():
    while True:
        choice = input(f"Do you want to play again? (y/n): ")
        if choice == "n":
            exit()
        if choice == "y":
            return
        else:
            print(f'Please enter "y" or "n"\n')
            time.sleep(3)

# def testing():
    # ### Debug code ###
    # print("Player :")
    # print(f"Name: {player_1._name} | HP: {player_1._hp} | MP: {player_1._mp} | AP: {player_1._ap}")
    # player_1._hp -= 40
    # print(f"player 1 hp: {player_1._hp}")
    # Character.heal(player_1)
    # print(f"player 1 hp: {player_1._hp}")
    # print(f"enemy hp: {great_frost_dragon._hp}")
    # Character.fight(player_1, great_frost_dragon)
    
if __name__ == "__main__":
    main()