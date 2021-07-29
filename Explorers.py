import time

# User response
answer_A = ["A", "a", "1"]
answer_B = ["B", "b", "2"]
answer_C = ["C", "c", "3"]
yes = ["Y", "y", "yes", "si"]
no = ["N", "n", "no"]

# Title Screen
def start():
    print('\n'
          '*******************************************\n'
          '*                                         *\n'
          '*  Welcome to a Beginner Adventure Game   *\n'
          '*                                         *\n'
          '*******************************************\n')
start()
time.sleep(2.3)  # Seconds

def hello():
    name = str(input("Enter the character's name : "))
    print("\nHello " + str(name))
    return

hello()
time.sleep(.3)  # Seconds

def intro():
    print('''\nAfter a drunken night out at the pub with friends,
    \nyou awaken to the realization that you are not in your own bed.
    \nYou sit up to check what time it is,
    \nand your head spins so hard that you fall back straight into a fluffy pillow.
    \nYou manage to look towards the light that is seeping through the blinds around the window at 
    \nthe opposite end of the room.''')

intro()

def option_bed():
    print("\nWhat's your next move, hero?")
    time.sleep(1)
    print('''    A. Stay in bed awhile to sober up a bit.
    B. Get out of bed.
    C. Lay in bed and contemplate the meaning of life.''')
    choice = input(">>>")
    if choice in answer_A:
        option_sleep()
    elif choice in answer_B:
        print('''\nYou swing your legs over the bed and attempt a landing.
              \nHowever you miss.
              \nYou nail your head firmly on the corner of the bedside table.
              \nWhelp, that was quick.
              \nYou died.\n \n ''')
        intro()
        option_bed()
    elif choice in answer_C:
        print('''You stare at the ceiling pondering the meaning of the significance 
              \nof the number 42 until you pass out.\n''')
        option_sleep()
    else:
        option_bed()

def option_sleep():
    print('''You awaken an indeterminate time later
          \nnoticing that the room is considerably brighter
          \nand your head no longer hurts.
          \nWhat's your next move, hero?
          \nA. Stay in bed awhile longer to get your beauty rest.
          \nB. Get out of bed.
          \nC. Lay in bed and contemplate why did Chester the Cheetah chew a
          \nchunk of cheap cheddar cheese?''')
    choice = input(">>>")
    if choice in answer_A:
        print('''You lay back down sinking deep into a restful sleep.
              \nUnfortunately, you never awake.
              \nYou are incinerated and your body is discovered by firefighters.
              \nWhelp, that sucks. You died.''')
        intro()
        option_bed()
    elif choice in answer_B:
        option_room()
    elif choice in answer_C:
        print('''As you ponder this age old toungue twisting riddle, you fall into a deep sleep.
              \nUnfortunately, you never awake.
              \nYou are incinerated and your body is discovered by firefighters.
              \nWhelp, that sucks. You died.\n''')
        intro()
        option_bed()

def option_room():
    print('''You swing your legs over the side of the bed and stick the landing perfectly.
          \nYou realize that you are in an old hotel on the outskirts of town.
          \nUnsure of how you got here, you quickly leave the room and walk back to town.
          \nHalfway back to town you notice a fire in the distance behind you.
          \nShuddering and shaking your head, you vow to never to speak of this incident to anyone. Ever.''')

    print("Do you wish to play again?")
    choice = input(">>>")
    if choice in yes:
        intro()
        option_bed()
    if choice in no:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print('''
                ######    #######   #######  ########     ########  ##    ## ######## 
                ##    ##  ##     ## ##     ## ##     ##    ##     ##  ##  ##  ##       
                ##        ##     ## ##     ## ##     ##    ##     ##   ####   ##       
                ##   #### ##     ## ##     ## ##     ##    ########     ##    ######   
                ##    ##  ##     ## ##     ## ##     ##    ##     ##    ##    ##       
                ##    ##  ##     ## ##     ## ##     ##    ##     ##    ##    ##       
                 ######    #######   #######  ########     ########     ##    ######## ''')
        print("\n\n\n\n\n\n\nThank you for playing")
        print("Beginner Adventure Game")
        print("By Dapper Nomad Productions")
    time.sleep(80)

option_bed()
