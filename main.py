#########################################################
#                Just An Ordinary Walk Home
#                  A Simple Text Adventure
#
#Author: John Michael Soza
#########################################################

from scenes_and_functions import enter_name, introduction, find_nickel, alley_guy, offer, book, might_be_followed, abandoned_store, park_entrance, cat, epilogue, new_game, post_script
print()
print("   Just An Ordinary Walk Home    \n")

def main():
    print("Welcome to 'Just An Ordinary Walk Home'!\n")
    playing = True
    enter_name()
    while playing:

        introduction()

        alive = True

        while alive:
            # choices = get_scene(scenes)   #This is not used
            # scenes = get_choice(choices)  #This is not used
            alive = find_nickel()
            alive = alley_guy()
            alive = offer()
            alive = book()
            alive = might_be_followed()
            alive = abandoned_store()
            alive = park_entrance()
            alive = cat()
            end = epilogue()
            if not alive:
                playing = False

            alive = False

            if end:
                your_choice = new_game()
                if your_choice:
                    print("\nExcellent!  Have fun, now!\n")
                    playing = True
                else:
                    print("\nOh well!  Thank you for playing!\n")
                    post_script()
                    playing = False


    return playing


        # if not alive:
        #     try_again = dead_retry()


if __name__ == "__main__":
    main()
