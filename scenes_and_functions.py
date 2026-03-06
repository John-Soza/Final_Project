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
    print("\nYou had an arduous but strangely rewarding day at work, and on your way \nhome you made a stop at your favorite department store to buy some new \nclothes to reward yourself.\n")
    print("The weight and feel of the store's designer bag adds a small boost to \nyour confidence.\n")
    input("Press enter to continue...")

# introduction()

def find_nickel():
    """
    This is the first decision point.
    """

    global alive
    scene_successful = False
    while not scene_successful and alive:
        global valid_choice
        valid_choice = False
        print("\nduring your lackadaisical stroll you perceive a bright glint in your \nperipheral vision. You turn your head to investigate.\n")

        while not valid_choice:
            print("On the ground you see a bright and shiny nickel, seemingly freshly minted.  \nIts glimmer is appealing but it's not really worth that much and you're \nnot exactly hurting for cash, either.  You could easily pass it by.\n")
            input("Press enter to continue...")
            print("\nWhat would you like to do?")
            print("1: Pick up the nickel")
            print("2: Leave it and walk on")

            print()
            coin_grab = input("please enter '1' or '2' to decide: ")
            if coin_grab == "1":
                print(
                    "\nYou decide that every little bit helps (not to mention that its \nshine is simply too good to pass up).\n")
                print(
                    "You bend down to pick up the nickle.  As you grab it you hear a \n'thunk' sound nearby, prompting you to impulsively look in the \nsound's direction as you return to your upright posture.\n")
                input("Press enter to continue...")
                print("\nOn a nearby wooden utility pole you see a long piece of still-\nquivering metal -- not much wider than a sewing needle -- firmly \nlodged into the wooden surface at about the same height as your \nneck.\n")
                print("You utter a largely indifferent 'Hm. Blowdart.' and resume your \ntrek home.  After all, it's probably nothing to worry about.\n")
                input("Press enter to continue...")
                valid_choice = True
                scene_successful = True
                alive = True

            elif coin_grab == "2":
                print("\nYou decide that a mere nickel is not but a pittance (no matter \nhow it glimmers) and resume your trek home.  Not two steps \ninto your journey you suddenly feel a small pricking sensation in \nyour neck, soon followed by a sense of dizziness.\n")
                print("The last thing you remember is becoming intimately acquainted with \nthe sidewalk.\n")


                valid_choice = True
                alive = False
                try_again = dead_retry()
                if try_again:
                    scene_successful = False
                else:
                    scene_successful = True

            else:
                print("\nInvalid choice, try again.")

    return alive

def alley_guy():
    global alive, valid_choice
    if alive:
        scene_successful = False
        while not scene_successful and alive:
            valid_choice = False
            print(italic("\nANYWAY") + ", you continue your carefree trip home down the street, \neager to return home and try on your recently acquired apparel \nand enjoy some well-deserved leisure time.\n")
            print("An audible 'Psst! Over here!' snaps you out of your internal \nmusings and your gaze darts about to find the this frightfully \nrude interruption.\n")
            input("Press enter to continue...")
            while not valid_choice:
                print("\nIn a nearby dark and dingy alley way stands a man of seemingly \nlow moral fiber, donned in a gray hat and trenchcoat.  It seems \nhe wants to speak with you.\n")
                print("What would you like to do?")
                print("1: Go to him.")
                print("2: Ignore him.")
                print()
                go_see = input("please enter '1' or '2' to decide: ")
                if go_see == "1":
                    print("\nYou decide that it couldn't hurt to see what he wants and start \ntowards him.  On your way to him you a loud CRASH from behind \nyou gives you a real start!\n")
                    print("You spin around to see that in the spot where you had just stood \nlies a broken ceramic flowerpot, its contents now all over the \nsidewalk.\n")
                    input("Press enter to continue...")

                    valid_choice = True
                    scene_successful = True
                    alive = True
                elif go_see == "2":
                    print("\n'Yeah, right!  As if I'll fall for that one', you think to your-\nself as you turn your gaze back towards the general direction \nof your intended destination.\n")
                    print("Mid-stride of your first step you feel sudden pain the top of \nyour cranium, accompanied by an awful smashing sound!  Quite \nunderstandably, you lose consciousness.\n")
                    input("Press enter to continue...")
                    print("\nThe " + italic("good news")+ " is that the blow was not instantly fatal, and \nthe " + italic("even better news") + " is that you were swiftly rushed to the \nnearest hospital.\n")
                    print("Unfortunately for you, though, " + italic("THIS IS CANADA") + " and it takes \nlonger for emergencies to be taken care of.  The doctors took \ntoo long to get too you.\n")
                    input("Press enter to continue...")
                    print("\nYou were done in by the infamous healthcare system.\n")

                    valid_choice = True
                    alive = False

                    try_again = dead_retry()
                    if try_again:
                        scene_successful = False
                    else:
                        scene_successful = True

                else:
                    print("\nInvalid choice, try again.")

        return alive

def offer():
    if alive:
        print("alive")
        # scene_successful = False
        # while not scene_successful and alive:

def dead_retry():
    global alive, valid_choice
    print("You've been " + italic("assassinated") + ".\n")
    retry_result = False
    input_received = False
    while not input_received:
        retry = input("That was unfortunate. Would you like to try again from this scene? (y/n): ")
        if retry.lower() == "y":
            print("\nRight. Here's another go.\n")
            alive = True
            valid_choice = False
            retry_result = True
            input_received = True
        elif retry.lower() == "n":
            print("\nI guess that's the end of it, then.  \n\n    Game Over\n")
            alive = False
            retry_result = False
            input_received = True
        else:
            print("\nInvalid choice, try again.")
    return retry_result

# enter_name()
# introduction()
# scene = find_nickel()
# scene = alley_guy()

# def get_scene(scenes):
#     scene_obj = dict(scenes = 0)
#     print(scene_obj["scene"])
#     return scene_obj["choices"]
#
# def get_choice(choices):
#     answer = input()
#     return choices[answer]