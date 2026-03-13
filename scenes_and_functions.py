alive = True
valid_choice = False
scene_successful = False
reached_end = False
replay = False
counter = 0
user_name = None


def italic(txt):
    # \033[3m is the code for italics
    # \033[0m is the code to reset formatting
    return f"\033[3m{txt}\033[0m"

def border():  #Thanks for the idea, Jackie!
    print()
    print("_"*74)

def enter_name():
    """
    The players enter their names here.
    """
    global user_name
    print("\nWelcome! What is your name?\n")
    valid_name = False
    while not valid_name:

        user_name = input("Please enter your name (no spaces): ")

        if user_name.isspace() or user_name == "":
            print("\nPlease " + italic("ACTUALLY ENTER") + " a name.\n")

        elif user_name.isdigit():
            print("\nNumbers are " + italic("NOT") + " names.  If there is a number in your formal name, please \nuse " + italic("Roman Numerals") + " such as " + italic("'I', 'II', 'III'") + ", etc.\n")

        elif user_name.isalpha():
            print()
            print("Well met, " + user_name + "! Let us begin the story!\nYour actions affect the outcome!\n")
            print("And " + italic("don't worry too much about failing") + "!  If you \nmake a mistake you have the option to retry from \n" + italic("the last checkpoint") + ".\n")
            print("Godspeed!\n")
            input("Press enter to continue...")
            border()

            valid_name = True

        else:
            print("\nNo spaces or numbers, or ASCII symbols, please.\n")

    return user_name


def introduction():
    """
    This is the introductory text of the story.
    """
    if alive or replay:
        print("\nYou are casually walking down the street on your way home, carefree and \ncontentedly humming to yourself, trying " + italic("not to be assassinated") + ".\n")
        input("Press enter to continue...")
        border()
        print("\nYou had an arduous but strangely rewarding day at work, and on your way \nhome you made a stop at your favorite department store to buy some new \nclothes to reward yourself.\n")
        print("The weight and feel of the store's designer bag adds a small boost to \nyour confidence.\n")
        input("Press enter to continue...")
        border()


def find_nickel():
    """
    This is the first decision point of the story.
    """
    global alive, scene_successful, valid_choice
    # scene_successful = False
    if alive:
        while not scene_successful and alive:
            valid_choice = False
            print("\nduring your lackadaisical stroll you perceive a bright glint in your \nperipheral vision. You turn your head to investigate.\n")
            input("Press enter to continue...")
            border()

            while not valid_choice:
                print("\nOn the ground you see a bright and shiny nickel, seemingly freshly minted.  \nIts glimmer is appealing but it's not really worth that much and you're \nnot exactly hurting for cash, either.  You could easily pass it by.\n")
                input("Press enter to continue...")
                border()
                print("\nWhat would you like to do?")
                print("1: Pick up the nickel")
                print("2: Leave it")

                print()
                coin_grab = input("please enter '1' or '2' to decide: ")
                if coin_grab == "1":
                    print(
                        "\nYou decide that every little bit helps (not to mention that its \nshine is simply too good to pass up).\n")
                    print(
                        "You bend down to pick up the nickle.  As you grab it you hear a \n'thunk' sound nearby, prompting you to impulsively look in the \nsound's direction as you return to your upright posture.\n")
                    input("Press enter to continue...")
                    border()
                    print("\nOn a nearby wooden utility pole you see a long piece of still-\nquivering metal -- not much wider than a sewing needle -- firmly \nlodged into the wooden surface at about the same height as your \nneck.\n")
                    print("You utter a largely indifferent 'Hm. Blowdart.' and resume your \ntrek home.  After all, it's probably nothing to worry about.\n")
                    input("Press enter to continue...")
                    border()
                    valid_choice = True
                    scene_successful = True
                    alive = True

                elif coin_grab == "2":
                    print("\nYou decide that a mere nickel is not but a pittance (no matter \nhow it glimmers) and resume your trek home.  Not two steps \ninto your journey you suddenly feel a small pricking sensation in \nyour neck, soon followed by a sense of dizziness.\n")
                    print("The last thing you remember is becoming intimately acquainted with \nthe sidewalk.\n")
                    input("Press enter to continue...")
                    border()

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
            print("An audible 'Psst! Over here!' snaps you out of your internal \nmusings and your gaze darts about to find the source of this \nfrightfully rude interruption.\n")
            input("Press enter to continue...")
            border()
            while not valid_choice:
                print("\nIn a nearby dark and dingy alley way stands a man of seemingly \nlow moral fiber, donned in a gray hat and trenchcoat.  It seems \nhe wants to speak with you.\n")
                print("What would you like to do?")
                print("1: Go to him")
                print("2: Ignore him")
                print()
                go_see = input("please enter '1' or '2' to decide: ")
                if go_see == "1":
                    print("\nYou decide that it couldn't hurt to see what he wants and start \ntowards him.  On your way to him, a loud CRASH from behind you \ngives you a real start!\n")
                    print("You spin around to see that in the spot where you had just stood \nlies a broken ceramic flowerpot, its contents now all over the \nsidewalk.\n")
                    input("Press enter to continue...")
                    border()

                    valid_choice = True
                    scene_successful = True
                    alive = True

                elif go_see == "2":
                    print("\n'Yeah, right!  As if I'll fall for that one', you think to your-\nself as you turn your gaze back towards the general direction \nof your intended destination.\n")
                    print("Mid-stride of your first step you feel sudden pain at the top of \nyour cranium, accompanied by an awful smashing sound!  Quite \nunderstandably, you lose consciousness.\n")
                    input("Press enter to continue...")
                    border()
                    print("\nThe " + italic("good news")+ " is that the blow was not instantly fatal, and \nthe " + italic("even better news") + " is that you were swiftly rushed to the \nnearest hospital.\n")
                    print("Unfortunately for you, though, " + italic("THIS IS CANADA") + " and it takes \nlonger for emergencies to be taken care of.  The doctors took \ntoo long to get to you.\n")
                    input("Press enter to continue...")
                    border()
                    print("\nYou were done in by the infamous healthcare system.\n")
                    print("SORE-ee aboot that, eh!\n")

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
            print("\n'They really should place a ban on placing flowerpots on the balustrades! \nSomebody could get hurt!', you say with no small modicum of indignation. \n(NOTE: for those who don't know, that's another term for guard rails on \nbalconies)\n")
            print("In any case, you have a more pressing matter at hand.\n")
            input("Press enter to continue...")
            border()
            while not valid_choice:
                print("\nYou turn your attention back to the gray-clad man of seemingly low moral \nfiber and gaze at him inquisitively.  Knowing that he now has your full \nattention he reaches inside his coat and draws forth a small book.  By \nhis dialogue he seems to be trying to pawn it off on you and he seems \nvery adamant about the matter.\n")
                print("What would you like to do?")
                print("1: Refuse the offer with firm politeness.")
                print("2: Buy the book (the asking price " + italic("is") + " quite cheap).")
                print()

                take_book = input("please enter '1' or '2' to decide: ")
                if take_book == "1":
                    print("\nYou're really not interested in buying another book right now -- and you \nalready have quite the backlog -- so you politely refuse the offer.\n")
                    print("Possibly feeling a touch slighted, the man of seemingly low moral fiber \nabruptly strikes you in the abdomen sending you into a stagger. While \ntrying to maintain your footing, you step into the empty space where a \nmanhole cover usually resides.  Too bad that today there " + italic("just happened") + " \nto be maintenance work.\n")
                    input("Press enter to continue...")
                    border()
                    print("\nAs you fall through the open manhole your head hits the edge, causing \nloss of lucid cognitive functioning -- not to mention consciousness.  \nWhat's worse is that you fell into the water while in this state.\n")
                    print("Up above, the man of seemingly low moral fiber peers down into the darkness \nwith a ghastly pallor coloring his face and a mortified expression on \nhis countenance that clearly says -- in common vernacular -- 'Oh crumbs!'. \n")
                    input("Press enter to continue...")
                    border()
                    print("\nUttering a small, disingenuous 'Not me!' he swiftly places his hands \ninto his pockets and walks off -- innocuously whistling as casually as \nhumanly possible.\n")
                    print("Your died a swift -- and " + italic("very stinky") + " -- death.\n")
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
                    border()
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
            border()
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
                    border()
                    valid_choice = True
                    scene_successful = True
                    alive = True

                elif read_book == "2":
                    print("\nJust a few sentences in you lose all rational thought and start gibbering \ninanely, staggering about without rhyme or reason!\n")
                    print("You wander into a busy intersection and promptly get hit by a garbage \ntruck.  Nearby pedestrians observe the spectacle with an appropriate \namount of confusion.\n")
                    input("Press enter to continue...")
                    border()
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
            border()

            while not valid_choice:
                print("\nIt's probably nothing, but it never hurts to be extra prudent about these \nthings.  Just to be on the safe side, you calmly glance about to find a \nway to lose this potential follower. \n")
                print("Up ahead you see some restrooms.\n")
                print("What would you like to do?")
                print("1: Enter the Men's Room")
                print("2: Enter the Lady's Room")
                print("3: Keep walking")
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
                    border()
                    print("\nGetting back to the story...")
                    print("\nThe moment you walk through the entrance you hear a single startled scream, \nimmediately followed a by a series of more screams!  A mob of very angry \nladies assails you, spraying you with various brands of mace and pepper \nspray and bludgeoning you with their very heavy purses -- all while posting \nabout it on social media.\n")
                    print("You've been " + italic("character assassinated") + ", and the shame of it killed you for real \n(as, did the concussion from the repetitive blunt trauma, those purses \nhad heavy objects in them).\n")
                    input("Press enter to continue...")
                    border()

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
                    print("You're sure she'll be able to handle it.  The timbre of her voice indicates that \nshe can easily take care of herself.\n")
                    input("Press enter to continue...")
                    border()

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
        print("Out of curiosity you peer outside from around the corner, careful not to be seen.  \nScanning the environment your gaze fixes upon a figure -- a lady -- leaning \nagainst a waist-high retaining wall of a flowerbed containing shrubbery.\n")
        print("She's dressed in stark and austere black attire and dark shades obscure her eyes.  \nShe smokes a clove cigarette and appears to be waiting for someone... she wasn't \nthere a moment ago.\n")
        input("Press enter to continue...")
        border()
        while not valid_choice:
            print("\nYou might be just being paranoid, but this woman seems suspect to you.  You try \nto think of what to do, and find yourself glancing at your bag as you weigh your \noptions.\n")
            print("Come to think of it, amongst your purchases were a hat and trenchcoat...\n")
            print("What would you like to do?")
            print("1: Change outfits to disguise yourself")
            print("2: Wait it out")
            print("3: Make the assassin lady fall madly in love with you and no longer want to kill you")
            print()

            options = input("please enter '1', '2', or '3' to decide: ")
            if options == "1":
                print("\nIn a moment of inspired brilliance you decide to don your new clothing as a \ndisguise.  'Not only will I get out of this situation, I'll also get to try \non my new clothes!  Two birds with one stone!  I'm so clever!', you think to \nyourself.\n")
                print("You change into your new outfit -- complete with hat -- and place your old \nclothes into the designer bag (they're still good, after all).  With renewed \nconfidence you walk out of the bathroom (first glancing at the mirror to \nadmire yourself).\n")
                input("Press enter to continue...")
                border()
                print("\nThe moment you exit the bathroom you perceive two things: 1) a 'BLAM!!!' sound; \nand 2) an excruciating pain in your chest -- swiftly followed by death.  In your \nfleeting final moments of consciousness you see the lady walk away.\n")
                print("Your " + italic("'brilliant'") + " plan didn't work because she recognized the very distinct \n" + italic("designer bag") + " you were carrying, you sad silly person.\n")
                print("And no, there's no option to hide or discard it!  That would be too much hard \nwork, and as a tax-paying citizen I am morally opposed to hard work.\n")
                input("Press enter to continue...")
                border()
                alive = False
                valid_choice = True
                scene_successful = True

            elif options == "2":
                print("\nYou wait in the hopes that she'll eventually get bored and go away.\n")
                input("Press enter to continue...")
                border()
                print("\nAbout an hour passes.  A few people have come and gone.  The black-clad lady \nis still there.\n")
                input("Press enter to continue...")
                border()
                print("\nAnother hour passes.  She's still there.  The other men are starting to look at \nyou funny.  They find you suspicious and are quite visibly in a hurry leave.  \nSoon the bathroom is quite empty.\n")
                input("Press enter to continue...")
                border()
                print("\nApparently tired of waiting, the lady breaks societal rules and enters the \nMen's Room with her lips pursed in irritation, draws out a gun and shoots you.  \nWith her work done she casually leaves the scene.")
                alive = False
                valid_choice = True
                scene_successful = True

            elif options == "3":
                your_actions()

            else:
                print("\nInvalid choice, try again.")

    return alive


def abandoned_store():
    """
    This is the sixth decision point of the story.
    """
    global alive, valid_choice, scene_successful
    if alive:
        scene_successful = False  # This resets the variable to false, otherwise it skips this scene
        while not scene_successful and alive:
            valid_choice = False
            print("\nAs the sounds of the commotion fade in the distance behind you.  You decide to step \ninto a coffee shop of which you are quite fond and order your go-to beverage for a \nday such as this.\n")
            print("Roughly half an hour later you leave the shop refreshed but also quite aware of how \nmuch time has passed and you're really wanting to get home as quickly as possible.\n")
            input("Press enter to continue...")
            border()
            print("\nThankfully, you know a [not necessarily legitimate] shortcut that you can use to \nsave time:  An abandoned department store that still remains unleased.  You and a \nfew friends discovered a covert entrance, back in your more reckless and \nyouthful years (around college-age, I'd say).\n")
            print("You discreetly enter the derelict building via the secret entrance, still left \nunchecked after all these years.  The place looks just as desolate as ever.\n")
            input("Press enter to continue...")
            border()
            while not valid_choice:
                print("\nAs you make your way through the vacant building something on a display fixture \ndraws your notice.\n")
                print("It's a teddy bear -- and in conspicuously good condition, I might add.  It sits \nalone.  " + italic("It is unimportant and completely irrelevant to this story") + ".\n")
                print("What would you like to do?")
                print("1: Leave it")
                print("2: Take it")
                print()

                take_bear = input("please enter '1' or '2' to decide: ")
                if take_bear == "1":
                    print("\nYou utter a small 'Huh.  Weird' and resume walking.  What need have you for a \nteddy bear -- especially one that " + italic("is unimportant and completely irrelevant to \nthis story") + "?\n")
                    print("Before too long you find the exit at the other end and leave the store.\n")
                    input("Press enter to continue...")
                    border()

                    valid_choice = True
                    scene_successful = True
                    alive = True

                elif take_bear == "2":
                    print("\nWell it " + italic("WOULD HAVE") + " been completely irrelevant if you hadn't picked it up!  It was \nintended for " + italic("SOMEONE ELSE") + "! >:( \n")
                    print("the bear seems strangely resistant to being picked up, the sensation being akin \nto a pull-string on an old toy.  Before you have any time to reflect upon this \nyou are engulfed in a storm of fire and shrapnel!\n")
                    print("You suffered a " +italic("POINTLESS") + " death by " + italic("TEDDY BEAR") + "!!!  >:( \n")
                    input("Press enter to continue...")
                    border()

                    alive = False
                    valid_choice = True

                    try_again = dead_retry()
                    if try_again:
                        scene_successful = False
                    else:
                        scene_successful = True

                else:
                    print("\nInvalid choice, try again.")

        return alive


def park_entrance():
    """
    This is the seventh decision point of the story.
    """
    global alive, valid_choice, scene_successful
    if alive:
        scene_successful = False  # This resets the variable to false, otherwise it skips this scene
        while not scene_successful and alive:
            valid_choice = False
            print("\nBack in the warm sunlight you soon arrive at a nearby park that's also a regular \nand important shortcut for your daily trips home.  The flora and fauna cause you \nto realize just how nice a day it is.\n")
            print("Just past the entrance to the park grounds you notice a lady sitting silently on \na bench.  She's dressed in stark and austere black attire and dark shades obscure \nher eyes.  She smokes a clove cigarette.\n")
            input("Press enter to continue...")
            border()

            while not valid_choice:
                print("\nShe seems very business-oriented and no-nonsense, but highly attractive.  Maybe \nyou could strike up a conversation.\n")
                print("What would you like to do?")
                print("1: Try talking with her")
                print("2: Leave her be")
                print("3: Make the lady fall madly in love with you and long for you to sweep her off her feet")
                print()

                small_talk = input("please enter '1', '2', or '3' to decide: ")
                if small_talk == "1":
                    print("\nThe worst that could happen is being turned down.  You go over to speak with her.\n")
                    input("Press enter to continue...")
                    border()
                    print("\nAfter a few short awkward exchanges, with her having a strained smile on her face, \nshe gives up all pretence of pleasantries and pulls out a gun and shoots you -- \nher lips pursed in irritation ("+ italic("almost as if she's already had to put up with \nMULTIPLE clumsy attempts at pickups and has had quite enough of it") +")!\n")
                    print("In your last fleeting moments of consciousness you hear the lady say in a cold-\nblooded yet relieved voice '" + italic("FINALLY.  Mission Accomplished.  Job done") + "'.\n")
                    input("Press enter to continue...")
                    border()

                    alive = False
                    valid_choice = True

                    try_again = dead_retry()
                    if try_again:
                        scene_successful = False
                    else:
                        scene_successful = True

                elif small_talk == "2":
                    print("\nJudging by her aforementioned no-nonsense demeaner you suspect that she'd rather \nnot be disturbed, so you walk on past.\n")
                    print("Not but a few moments later, however, you hear footsteps behind you.  As you didn't \nsense anyone else in the vicinity before now, you can logically conclude \nthat they belong to her.\n")
                    print("Maybe she's interested after all, but it's best not to seem too eager.  It would \nreek of desperation, so you pretend not to notice yet and keep on walking.\n")
                    input("Press enter to continue...")
                    border()
                    valid_choice = True
                    scene_successful = True
                    alive = True

                elif small_talk == "3":
                    your_actions()

                else:
                    print("\nInvalid choice, try again.")


        return alive


def cat():
    """
    This is the final decision point of the story.
    """
    global alive, valid_choice, scene_successful
    if alive:
        scene_successful = False  # This resets the variable to false, otherwise it skips this scene
        while not scene_successful and alive:
            valid_choice = False
            print("\nAs you meander through the park, trying to think of a list of potential subject \nmatter for conversation with the lady behind you, you hear a small 'meowing' sound. \nYou look about in search of the source of it.\n")
            print("You hear another meow.  It sounds like it's coming from above.  You look up and see \nan orange, short-haired tabby cat sitting on a branch, staring down at you from the \n'bove.  Now that it has your attention, it 'meows' again.\n")
            input("Press enter to continue...")
            border()

            while not valid_choice:
                print("\nThough it doesn't appear visibly distressed, it's meow does indicate a craving for \nattention and it is looking at you quite intently.  It might be stuck.\n")
                print("You notice that the footsteps behind you have stopped.\n")
                print("What would you like to do?")
                print("1: Climb the tree to help the cat")
                print("2: Leave it be")
                print("3: Gesture to the cat to jump down and that you'll catch it")
                print()

                help_cat = input("please enter '1', '2', or '3' to decide: ")
                if help_cat == "1":
                    print("\nYou have a soft spot for cats, and this might be an excellent way to impress the \nlady -- not to mention an " + italic("excellent conversation starter") + "!  You put down your bags, \nmaking extra sure that your gaze doesn't turn in her direction so that she won't \nrealize you're aware of her presence, and proceed to climb the tree to help the \nlittle guy.\n")
                    print("Upon reaching the branch on which it sits the orange cat lets out a very frightened \n'YeeOWWWWWWLLLLLL!!!' and starts mauling your face with it's razor sharp claws \n-- the pain of which causes you to loose your grip!\n")
                    input("Press enter to continue...")
                    border()
                    print("\nYou know those angles at which you can land from a fall that, though quite painful, \nallow you to survive it?  " + italic("You didn't land at one of those angles") + ".\n")
                    print("If it's any consolation, at least it was over quickly.\n")
                    input("Press enter to continue...")
                    border()
                    alive = False
                    valid_choice = True

                    try_again = dead_retry()
                    if try_again:
                        scene_successful = False
                    else:
                        scene_successful = True

                elif help_cat == "2":
                    print("\nYou recall that cats also have the ability to " + italic("climb back down") + " trees, so despite your \ninnate desire to help the cat, you know that it'll be fine and keep on walking.\n")
                    print("31 paces later you hear behind you the sudden and harshly-unexpected cacophony of \ndeafening screams and an angry 'YeeOWWWWWWLLLLLL!!!' and the subsequent sound of a \nviolent impact!  You instinctively spin around from the fright!\n")
                    print("You see the cat scurry off into the distance, and lowering your gaze a little you see \nthe lady lying on the ground!  There are claw marks on her face!  She's not moving!\n")
                    input("Press enter to continue...")
                    border()
                    print("\nYou rush over to help her if you can, but she's lifeless.  Nearby you see a man with \na briefcase and -- after your urgent cry for his assistance -- he hurriedly makes his \nway to your position.  He just so happens to be a doctor!  The day might be saved!\n")
                    input("Press enter to continue...")
                    border()
                    print("\nHowever, after a brief check the doctor looks at you and shakes his head in a manner \nthat says 'I'm sorry, lad, she's done for'.  He looks at his watch and pronounces her \ndead, turns to you, advises you to go home and try to get your mind off of the matter, \nand promises that he'll call the coroner and take care of things from here.\n")
                    print("Downtrodden in heart -- and with a newfound fear of cats -- you resume your journey \nhome.  At least you're nearly there and you desperately hope that you can forget about \nthis wretched event.  You wonder if there was anything you could have done to prevent \nthis terrible incident.  The trauma has shaken you to your very core.\n")
                    input("Press enter to continue...")
                    border()
                    print("\nLife is such a fragile and transient thing; death so permanent and irreversible; and \nno one should " + italic("EVER") + " make light of such things.  " + italic("NO ONE") + ".\n")
                    input("Press enter to continue...")
                    border()

                    valid_choice = True
                    scene_successful = True
                    alive = True

                elif help_cat == "3":
                    print("\nYou have a soft spot for cats, and this might be an excellent way to impress the \nlady -- not to mention an " + italic("excellent conversation starter") + "!  You put down your bags, \nmaking extra sure that your gaze doesn't turn in her direction so that she won't \nrealize you're aware of her presence, and hold out your arms to tell the cat \nyou'll catch it.\n")
                    print("Apparently understanding your intent, the cat leaps down to your open arms...\n")
                    input("Press enter to continue...")
                    border()
                    print("\n... but in it's fright from the long and rapid descent it utters a very frightened \n'YeeOWWWWWWLLLLLL!!!' and unintentionally mauls you in the face!  You fall back and \nhit your head wrong, causing a concussion swiftly followed by death.  The still-\nfrightened cat runs off into the distance.\n")
                    print("The lady runs over to examine you and sees that you are, in fact, quite dead.  'I \nguess " + italic("that's that") + ", then.' says the black-clad lady.  She casually leaves the scene.\n")
                    input("Press enter to continue...")
                    border()


                    alive = False
                    valid_choice = True

                    try_again = dead_retry()
                    if try_again:
                        scene_successful = False
                    else:
                        scene_successful = True

                else:
                    print("\nInvalid choice, try again.")

        return alive


def epilogue():
    """
    This is the story's end.
    """
    global alive, reached_end
    if alive:
        print("\nAt long last you enter the door to your abode, quickly turning on the lights \nbecause the darkness only adds to your gloom.  You lifelessly look about the \nliving room in the vain hope of finding something to occupy your mind and \nsuperficially numb the depression -- knowing on an intellectual level that \nnothing could " + italic("EVER") + " do so, yet still you look.\n")
        print("\nFinding nothing that could ever fill this newly developed void in your soul you \nclose your eyes and emit a long, hollow sigh.\n")
        input("Press enter to continue...")
        border()
        print("\nNow that you're home you finally notice the lack of weight in your left hand, \nmeaning that in your trauma you completely forgot about your new clothes and left \nthem at the park.  In this moment you could care less about something so trivial \nas the vanity of trends and fashion -- in fact " + italic("TO HELL WITH THEM") + "!\n")
        print("At a loss from it all you move across the room in a listless, emotional auto-\npilot state and blankly switch on the radio from the sheer force of routine, \nand glumly plop yourself onto your favorite recliner.  You just sit there, half-\nheartedly listening to the news with the most vacant stare that could ever be \nfound on a human face...\n")
        input("Press enter to continue...")
        border()
        print("\n...but hark!  You're snapped out of your introspective melancholia by the news \nupon hearing about something very familiar to you and you lean in closely to \nhear, eyes wide and intense!\n")
        input("Press enter to continue...")
        border()
        print("\n'...was found dead in a local park, the cause of which\n was officially attributed to blunt trauma suffered on\n her occipital bone.  Based on the " + italic("deep lacerations on\n her face") + " she had been attacked by some kind of animal\n -- " + italic("maybe a cat") + " or something similar.'\n")
        print("'Upon inspection the police found she was in possession\n of several " + italic("concealed armaments") + " and that she carried\n multiple IDs, " + italic("all of them counterfeit") + ".  Upon questioning\n a doctor who was at the scene, he said...'\n")
        input("Press enter to continue...")
        border()
        print("\nThe massive weight you bore upon your heart immediately evaporates in that very \nmoment!  A new levity lifts your soul into the stratosphere!  This is BIG NEWS -- \nand the serendipity of your subconscious habit leading you to this discovery \nnothing short of astronomical!\n")
        print("That woman had been " + italic("dangerous") + " -- and to think that you had been fancying the idea \nof " + italic("talking with her") + "!  From what the reporter had detailed she could have been \na mobster; a Terrorist; an " + italic("ASSASSIN") + "!  For all you know she " + italic("could have been trying \nto kill you") + "!  That's entirely ridiculous of course -- that only happens in the movies\n -- BUT STILL, such a dangerous person is better off gone from this world!\n")
        input("Press enter to continue...")
        border()
        print("\nYou feel utterly silly for ever having felt so depressed over her death, and with \nrenewed vigor you feel like you could take on the world!  You plan to celebrate \nthis newfound lease on life with some takeout from your favorite " + italic("[insert preferred \nclassification of cuisine here]") + " joint and giddily proceed to phone in your order!\n")
        print("With that done your mind recalls the bag you left behind at the park.  If you leave \nnow it might still be there!  There's plenty of time before the food arrives \nso what are you waiting for!  You set off for the park, POST HASTE!\n")
        input("Press enter to continue...")
        border()
        print("\nThe next day, at the laboratory at which you work, you make a small but utterly \nfatal error that results in an apocalyptic chain reaction that spreads throughout \nthe entire world -- consuming " + italic("all life") + " in its wake!\n")
        print("You've unwittingly " + italic("assassinated") + " the world and all life within it.\n")
        input("Press enter to continue...")
        border()
        print("\n... OH!...I say...\n")
        input("Press enter to continue...")
        border()
        print("\n...\n")
        input("Press enter to continue...")
        border()
        print("\n...Welllll...\n")
        input("Press enter to continue...")
        border()
        print("\n... " + italic("Alright, then") + ".\n")
        print("           " +italic("FIN"))
        input("\nPress enter to complete the game...")
        border()

        reached_end = True
    return reached_end


def new_game():
    global scene_successful, replay, reached_end, counter, user_name
    if reached_end:

        print(f"\nCongratulations, {user_name}!  You have reached the end of my game!\n")
        if counter < 1:
            print("And great job on not dying until you " + italic("accidentally destroyed the world") + "!\n")
        elif counter == 1:
            print("And you only died " + italic("ONCE") + " on your way to " + italic("accidentally destroying the world") + "!\n")
        elif 0 < counter < 11:
            print(f"And it only took you {italic(counter)} deaths on your way to " + italic(
                "accidentally \ndestroying the world") + "!\n")
        elif 11 <= counter < 20:
            print("And you made " + italic("EVERY mistake in the book") + "! And that \nwas " + italic("BEFORE") + " you " + italic(
                "accidentally destroyed the world") + "!\n")
        elif counter < 0:  #This is a joke
            print("The ability to reach this result " + italic("doesn't exist! HOW DID YOU GET HERE!?\n"))
        else:
            print(italic(f"{counter} DEATHS???  I don't even know how you got through this story!\n"))  #Thanks for the idea, Leah!
        print("Would you like to have another go at the story and try to find all the different \nutterly ridiculous ways to di-- I mean ENDINGS of the game?")
        replay = False
        input_received = False
        while not input_received:
            answer = input("\nWhat say you? (y/n): ")
            if answer == "y":
                replay = True
                scene_successful = False
                reached_end = False
                input_received = True
                counter = 0
            elif answer == "n":
                replay = False
                input_received = True
            else:
                print("\nInvalid choice, try again.")
    return replay


def post_script():
    if reached_end and not replay:
        print("\nWith " + italic("absolutely NO") + " apologies whatsoever for any stolen jokes -- ALL " + italic("TWO") + " OF THEM!\n")
        input("Press enter to continue...")
        border()
        print("\nWhoever correctly guesses which ones they are will receive a " + italic("non-corporeal") + " prize!\n")
        input("Press enter to continue...")
        border()
        print("\nAnd for anyone who is concerned that I made the assassin a woman, it was ONLY \nso that I could twice use a particular joke -- You might have even seen it at \nleast once in your playthrough(s).\n")
        input("Press enter to continue...")
        border()
        print("\nAnd once again: THANKS FOR PLAYING!\n")
        print(f"{italic("-John Michael Soza"):>49}")


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
    global alive, valid_choice, replay, counter
    print("\nYou've been " + italic("assassinated") + ".\n")
    retry_result = False
    input_received = False
    while not input_received:
        retry = input("That was unfortunate.  \nWould you like to try again from this scene? (y/n): ")
        if retry.lower() == "y":  #This sends the player back to the last checkpoint to try again.
            print("\nRight. Here's another go.\n")
            counter += 1
            alive = True
            valid_choice = False
            retry_result = True
            input_received = True
        elif retry.lower() == "n":  #This ends the game.
            print("\nI guess that's the end of it, then.  \n\n    Game Over\n")
            alive = False
            retry_result = False
            input_received = True
            replay = False

        else:
            print("\nInvalid choice, try again.")
    return retry_result




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