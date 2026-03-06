alive = True
valid_choice = False


def italic(txt):
    # \033[3m is the code for italics
    # \033[0m is the code to reset formatting
    return f"\033[3m{txt}\033[0m"


def enter_name():
    user_name = input("Hello! What is your name?\nPlease enter your name: ")
    print()
    print("Well met, " + user_name + "! Let us begin the story!\nYour actions affect the outcome!\n")
    print("Godspeed!\n")

def introduction():
    print("You are casually walking down the street on your way home, carefree and \ncontentedly humming to yourself, trying " + italic("not to be assassinated") + ".\n")
    input("Press enter to continue...")
    print("You had an arduous but strangely rewarding day at work, and on your way \nhome you made a stop at your favorite department store to buy some new \nclothes to reward yourself.\n")
    print("The weight and feel of the store's designer bag adds a small boost to \nyour confidence.\n")
    input("Press enter to continue...")

# introduction()

def find_nickel():
    """
    This is the first decision point.
    """
    global alive, valid_choice
    print("during your lackadaisical stroll you perceive a bright glint in your \nperipheral vision. You turn your head to investigate.\n")
    print("On the ground you see a bright and shiny nickel, seemingly freshly minted.  \nIts glimmer is appealing but it's not really worth that much and you're \nnot exactly hurting for cash, either.  You could easily pass it by.\n")
    input("Press enter to continue...")
    print("What would you like to do?")
    print("1: Pick up the nickel")
    print("2: Leave it and walk on")


    while alive:
        while not valid_choice:
            print()
            coin_grab = input("please enter '1' or '2' to decide: ")
            if coin_grab == "1":
                print("\nYou decide that every little bit helps (not to mention that its \nshine is simply too good to pass up).\n")
                print("You bend down to pick up the nickle.  As you grab it you hear a \n'thunk' sound nearby, prompting you to impulsively look in the \nsound's direction as you return to your upright posture.\n")
                print("On a nearby wooden utility pole you see a long piece of still-\nquivering metal -- not much wider than a sewing needle -- firmly \nlodged into the wooden surface at about the same height as your \nneck.\n")
                print("You utter a largely indifferent 'Hm. Blowdart.' and resume your \ntrek home.  After all, it's probably nothing to worry about.\n")
                valid_choice = True
                alive = True
            elif coin_grab == "2":
                print("\nYou decide that a mere nickel is not but a pittance (no matter \nhow it glimmers) and resume your trek home.  Not two steps \ninto your journey you suddenly feel a small pricking sensation in \nyour neck, soon followed by a sense of dizziness.\n")
                print("The last thing you remember is becoming quickly acquainted with \nthe sidewalk.\n")

                valid_choice = True
                alive = False
            else:
                print("\nInvalid choice, try again.")
    return alive

def dead_retry():
    global alive
    alive = False
    print("You've been " + italic("assassinated") + ".\n")
    retry = input("That was unfortunate. Would you like to try again from this scene? (y/n): ")
    if retry == "y":
        print("\nRight. Here's another go.\n")
        alive = True
    elif retry == "n":
        print("\nI guess that's the end of it, then.  \n    Game Over\n")
        alive = False
    else:
        print("\nInvalid choice, try again.")
    return alive

#
# find_nickel()

# def get_scene(scenes):
#     scene_obj = dict(scenes = 0)
#     print(scene_obj["scene"])
#     return scene_obj["choices"]
#
# def get_choice(choices):
#     answer = input()
#     return choices[answer]