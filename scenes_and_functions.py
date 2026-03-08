alive = True
valid_choice = False
scene_successful = False


def italic(txt):
    # \033[3m is the code for italics
    # \033[0m is the code to reset formatting
    return f"\033[3m{txt}\033[0m"


def enter_name():
    """
    The players enter their names here.
    """
    user_name = input("Hello! What is your name?\nPlease enter your name: ")
    print()
    print("Well met, " + user_name + "! Let us begin the story!\nYour actions affect the outcome!\n")
    print("Godspeed!\n")

def introduction():
    """
    This is the introductory text of the story.
    """
    print("You are casually walking down the street on your way home, carefree and \ncontentedly humming to yourself, trying " + italic("not to be assassinated") + ".\n")
    input("Press enter to continue...")
    print("\nYou had an arduous but strangely rewarding day at work, and on your way \nhome you made a stop at your favorite department store to buy some new \nclothes to reward yourself.\n")
    print("The weight and feel of the store's designer bag adds a small boost to \nyour confidence.\n")
    input("Press enter to continue...")

# introduction()

def find_nickel():
    """
    This is the first decision point of the story.
    """
    global alive, scene_successful
    # scene_successful = False
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
                input("Press enter to continue...")


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
    """
    This is the second decision point of the story.
    """
    global alive, valid_choice, scene_successful
    if alive:
        scene_successful = False # This resets the variable to false, otherwise it skips this scene
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
                    print("Unfortunately for you, though, " + italic("THIS IS CANADA") + " and it takes \nlonger for emergencies to be taken care of.  The doctors took \ntoo long to get to you.\n")
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
    """
    This is the third decision point of the story.
    """
    global alive, valid_choice, scene_successful
    if alive:
        scene_successful = False # This resets the variable to false, otherwise it skips this scene
        while not scene_successful and alive:
            valid_choice = False
            print("\n'They really should place a ban on placing flowerpots on the balustrades! \nSomebody could get hurt!', you say with no small modicum of indignance. \n(NOTE: for those who don't know, that's another term for guard rails on \nbalconies)\n")
            print("In any case, you have a more pressing matter at hand.\n")
            input("Press enter to continue...")
            while not valid_choice:
                print("\nYou turn your attention back to the gray-clad man of seemingly low moral \nfiber and gaze at him inquisitively.  Knowing that he now has your full \nattention he reaches inside his code and draws forth a small book.  By \nhis dialogue he seems to be trying to pawn it off on you and he seems \nvery adamant about the matter.\n")
                print("What would you like to do?")
                print("1: Refuse the offer with firm politeness.")
                print("2: Buy the book (the asking price " + italic("is") + " quite cheap).")
                print()

                take_book = input("please enter '1' or '2' to decide: ")
                if take_book == "1":
                    print("\nYou're really not interested in buying another book right now -- and you \nalready have quite the backlog -- so you politely refuse the offer.\n")
                    print("Possibly feeling a touch slighted, the man of seemingly low moral fiber \nabruptly strikes you in the abdomen sending you into a stagger. While \ntrying to maintain your footing you step into the empty space where a \nmanhole cover usually resides.  Too bad that today there " + italic("just happened") + " \nto be maintenance work.\n")
                    input("Press enter to continue...")
                    print("\nAs you fall through the open manhole your head hits the edge, causing \nloss of lucid cognitive functioning -- not to mention consciousness.  \nWhat's worse is that you fell into the water while in this state.\n")
                    print("Up above, the man of seemingly low moral fiber peers down into the darkness \nwith a ghastly pallor coloring his face and a mortified expression on \nhis countenance that clearly says -- in common vernacular -- 'Oh crumbs!'. \n")
                    input("Press enter to continue...")
                    print("\nUttering a small, disingenuous 'Not me!' he swiftly places his hands \ninto his pockets and walks off -- innocuously whistling as casually as \nhumanly possible.\n")
                    print("Your died a swift -- and not to mention " + italic("very stinky") + " -- death.\n")
                    valid_choice = True
                    alive = False

                    try_again = dead_retry()
                    if try_again:
                        scene_successful = False
                    else:
                        scene_successful = True

                elif take_book == "2":
                    print("\nSomething tells you that your life " + italic("literally") + " depends upon the purchase of \nthis book, so you buy it.  Besides, what's a couple of dollars?\n")
                    print("Apparently satisfied, the man of seemingly low moral fiber bids you a \nwonderful day and walks away -- whistling innocuously.  With that little \nmatter resolved, you can now refocus on getting home.\n")
                    input("Press enter to continue...")
                    valid_choice = True
                    scene_successful = True
                    alive = True

                else:
                    print("\nInvalid choice, try again.")

        return alive

def book():
    """
    This is the fourth decision point of the story.
    """
    global alive, valid_choice, scene_successful
    if alive:
        scene_successful = False  # This resets the variable to false, otherwise it skips this scene
        while not scene_successful and alive:
            valid_choice = False
            print("\nOnce again you resume your walk home, feeling slightly bewildered after this \nrather impromptu purchase.  Oh well, since you bought it you may as well take \na look at it.  You turn your gaze downward to examine the book. \n")
            input("Press enter to continue...")
            while not valid_choice:
                print("\nIt appears to be a rather old book, judging from the binding.  It is titled \n" + italic("'The King In Yellow'") + ", and on the cover is a strange figure in yellow robes, \npossessing red feathered wings.\n")
                print("What would you like to do?")
                print("1: Don't read it.")
                print("2: Give it a short read to get the gist.")
                print()
                read_book = input("please enter '1' or '2' to decide: ")
                if read_book == "1":
                    print("\nYou really couldn't care less about this book!\n")
                    print("You nonchalantly toss the book into a fortuitously placed dustbin that you \nhappened to be passing by.  It was only a couple of dollars so it's no big \nloss.\n")
                    print(italic("Moving right along") + ", back to heading home!\n")
                    input("Press enter to continue...")
                    valid_choice = True
                    scene_successful = True
                    alive = True

                elif read_book == "2":
                    print("\nJust a few sentences in you lose all rational thought and start gibbering \ninanely, staggering about without rhyme or reason!\n")
                    print("You wander into a busy intersection and promptly get hit by a garbage \ntruck.  Nearby pedestrians observe the spectacle with an appropriate \namount of confusion.\n")
                    input("Press enter to continue...")
                    print("\nYou [indirectly] died from " + italic("things that mankind was not meant to know") + "!\n")

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

def might_be_followed():
    """
    This is the fifth decision point of the story.
    """
    global alive, valid_choice, scene_successful
    if alive:
        scene_successful = False  # This resets the variable to false, otherwise it skips this scene
        while not scene_successful and alive:
            valid_choice = False
            print("\nAs you press onwards your eagerness to try on the new clothes you carry is \nrising to nearly unbearable levels and the anticipation makes you quicken your \npace, but your ears soon perceive that it's not only your pace that quickens.  \n")
            print("You've noticed the sound of the footfalls behind you.  You had been hearing \nthem for a few minutes but your mind didn't register them until they sped up \nto match your pace.\n")
            input("Press enter to continue...")

            while not valid_choice:
                print("\nIt's probably nothing, but it never hurts to be extra prudent about these \nthings.  Just to be on the safe side, you calmly glance about to find a \nway to lose this potential follower. \n")
                print("Up ahead you see some restrooms.\n")
                print("What would you like to do?")
                print("1: Enter the Men's Room")
                print("2: Enter the Lady's Room")
                print("3: Keep Walking")
                print()

                choose_path = input("please enter '1', '2', or '3' to decide: ")
                if choose_path == "1":
                    outcome = mens_room()
                    alive = False
                    valid_choice = True

                    try_again = dead_retry()
                    if try_again:
                        scene_successful = False
                    else:
                        scene_successful = True

                elif choose_path == "2":
                    print("\nSo hey, I forgot to mention that you're " + italic("actually playing as man") + " in this game.  \nSorry about that.  \n\nThat name you entered at the start of this game is " + italic("YOUR") + " name, not the \ncharacter's.  He already has a name and it's " + italic("Tad Asinine") + ".\n")
                    input("Press enter to continue...")
                    print("\nGetting back to the story...")
                    print("\nThe moment you walk through the entrance you hear a single startled scream, \nimmediately followed a by a series of more screams!  A mob of very angry \nladies assails you, spraying you with various brands of mace and pepper \nspray and bludgeoning you with their very heavy purses -- all while posting \nabout it on social media.\n")
                    print("You've been " + italic("character assassinated") + ", and the shame of it killed you for real \n(as, did the concussion from the repetitive blunt trauma, those purses \nhad heavy objects in them).\n")
                    input("Press enter to continue...")

                    alive = False
                    valid_choice = True

                    try_again = dead_retry()
                    if try_again:
                        scene_successful = False
                    else:
                        scene_successful = True

                elif choose_path == "3":
                    print("\nYou think 'Eh, I'm just being paranoid.' and keep on walking.  After all it's \nnot healthy to live in fear.  Your return to emotional equilibrium is cemented \nby whistling to yourself as your journey continues.\n")
                    print("As you cross the street at an intersection you hear a minor commotion behind \nyou.  It sounds like some lads are trying to pick up a lady, and by the sound \nof it she's getting rather irritated with their persistence.\n")
                    print("You're sure she'll be able to handle it.  The timbre of her voice indicates that she \ncan easily take care of herself.\n")
                    input("Press enter to continue...")

                    valid_choice = True
                    scene_successful = True
                    alive = True

                else:
                    print("\nInvalid choice, try again.")

        return alive

def mens_room():
    """
    This is an offshoot decision point for the might_be_followed function
    """
    global alive, valid_choice, scene_successful
    scene_successful = False
    while not scene_successful and alive:
        valid_choice = False
        print("\nYou enter the men's room, hopefully you'll be safe here.\n")
        print("Out of curiosity you peer outside from around the corner, careful to not be seen.  \nScanning the environment your gaze fixes upon a figure -- a lady -- leaning \nagainst a waist-high retaining wall of a flowerbed containing shrubbery.\n")
        print("She's dressed in stark and austere black attire and dark shades obscure her eyes.  \nShe smokes a clove cigarette and appears to be waiting for someone... she wasn't \nthere a moment ago.\n")
        input("Press enter to continue...")
        while not valid_choice:
            print("\nYou might be just being paranoid, but this woman seems suspect to you.  You try \nto think of what to do, and find yourself glancing at your bag as you weigh your \noptions.\n")
            print("Come to think of it, amongst your purchases were a hat and trenchcoat...\n")
            print("What would you like to do?")
            print("1: Change outfits to disguise yourself")
            print("2: Wait it out")
            print("3: Make the assassin lady fall madly in love with you and no longer want to kill you.")
            print()

            options = input("please enter '1', '2', or '3' to decide: ")
            if options == "1":
                print("\nIn a moment of inspired brilliance you decide to don your new clothing as a \ndisguise.  'Not only will I get out of this situation, I'll also get to try \non my new clothes!  Two birds with one stone!  I'm so clever!', you think to \nyourself.\n")
                print("You change into your new out fit -- complete with hat -- and place your old \nclothes into the designer bag (they're still good, after all).  With renewed \nconfidence you walk out of the bathroom (first glancing at the mirror to \nadmire yourself).\n")
                input("Press enter to continue...")
                print("\nThe moment you exit the bathroom you perceive two things: 1) a 'BLAM!!!' sound; \nand 2) an excruciating pain in your chest -- swiftly followed by death.  In your \nfleeting final moments of consciousness you see the lady walk away.\n")
                print("Your " + italic("'brilliant'") + " plan didn't work because she recognized the very distinct \n" + italic("designer bag") + " you were carrying, you sad silly person.\n")
                print("And no, there's no option to hide or discard it!  That would be too much hard \nwork, and as a tax-paying citizen I am morally opposed to hard work.\n")
                input("Press enter to continue...")
                alive = False
                valid_choice = True
                scene_successful = True

            elif options == "2":
                print("\nYou wait in the hopes that she'll eventually get bored and go away.\n")
                input("Press enter to continue...")
                print("\nAbout an hour passes.  A few people have come and gone.  The black-clad lady \nis still there.\n")
                input("Press enter to continue...")
                print("\nAnother hour passes.  She's still there.  The other men are starting to look at \nyou funny.  They find you suspicious and are quite visibly in a hurry leave.  \nSoon the bathroom is quite empty.\n")
                input("Press enter to continue...")
                print("\nApparently tired of waiting, the lady breaks societal rules and enters the \nMen's Room with her lips pursed in irritation, draws out a gun and shoots you.  \nWith her work done she casually leaves the scene.")
                alive = False
                valid_choice = True
                scene_successful = True

            elif options == "3":
                your_actions()

            else:
                print("\nInvalid choice, try again.")

    return alive

def your_actions():
    """
    This is just for my own amusement.
    """
    print("\nYOU ONLY HAVE CONTROL OVER " + italic("YOUR") + " ACTIONS.  \nYOU CAN ONLY AFFECT WHAT " + italic("YOU") + " DO.  YOU HAVE \nNO INFLUENCE OVER THE THOUGHTS AND DECISIONS \nOF OTHER CHARACTERS IN THIS STORY.\n")
    print("GO BACK AND TRY AGAIN.\n")
    input("Press enter to continue...")

def dead_retry():
    """
    This offers the players another chance at the story, should they die.
    """
    global alive, valid_choice
    print("\nYou've been " + italic("assassinated") + ".\n")
    retry_result = False
    input_received = False
    while not input_received:
        retry = input("That was unfortunate.  \nWould you like to try again from this scene? (y/n): ")
        if retry.lower() == "y":  #This sends the player back to the last checkpoint to try again.
            print("\nRight. Here's another go.\n")
            alive = True
            valid_choice = False
            retry_result = True
            input_received = True
        elif retry.lower() == "n":  #This ends the game.
            print("\nI guess that's the end of it, then.  \n\n    Game Over\n")
            alive = False
            retry_result = False
            input_received = True
        else:
            print("\nInvalid choice, try again.")
    return retry_result


#####  These calls are for testing!  #####
# enter_name()
# introduction()
# scene = find_nickel()
# scene = alley_guy()
# offer()
# book()
# scene = might_be_followed()
# scene = mens_room()

#####  These functions are unused for this build  #####
#####  They're also not quite right, at the moment  #####

# def get_scene(scenes):
#     scene_obj = dict(scenes = 0)
#     print(scene_obj["scene"])
#     return scene_obj["choices"]
#
# def get_choice(choices):
#     answer = input()
#     return choices[answer]