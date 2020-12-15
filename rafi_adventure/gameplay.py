import time
from functions import *

def main():
    char_setup()
    level_1()
    # level_2()
    # level_3()
    # testing()
# Global vars
player_1 = str()
great_frost_dragon = Enemy("Great Frost Dragon", 20, 0, 7)


def char_setup():
    global player_1
    
    # Define character name
    clear_screen()
    char_name = input("What is your character's name: ")
    
    # Define character type
    char_sel = ()
    while not char_sel:
        clear_screen()
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
            clear_screen()
            print(f'"{char_sel}" is not a valid selection.\n')
            print('Select "1" if you want to be a Warrior.')
            print('Select "2" if you want to be a Mage.')
            char_sel = ()
            time.sleep(5)
            
        
def level_1():
    clear_screen()
    print("You wake up near a hedge on the edge of a grove. You hear a rustling")
    print("in the forest across the grove as trees sway from the movements of a")
    print("large creature. As you crouch behind a nearby bush, the great beast")
    print("comes into view. It's huge form stands before you as you decide what")
    print("to do next.\n")
    Character.fight_choice(player_1, great_frost_dragon)


def level_2():
    print("This is level 2.")
    
    
def level_3():
    print("This is level 3.")


def testing():
    ### Debug code ###
    print("Player :")
    print(f"Name: {player_1._name} | HP: {player_1._hp} | MP: {player_1._mp} | AP: {player_1._ap}")
    player_1._hp -= 40
    print(f"player 1 hp: {player_1._hp}")
    Character.heal(player_1)
    print(f"player 1 hp: {player_1._hp}")
    print(f"enemy hp: {great_frost_dragon._hp}")
    Character.fight(player_1, great_frost_dragon)
    
if __name__ == "__main__":
    main()       