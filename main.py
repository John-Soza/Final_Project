#########################################################
#                Just An Ordinary Walk Home
#                  A Simple Text Adventure
#
#Author: John Michael Soza
#########################################################

from scenes_and_functions import enter_name, introduction, find_nickel, alley_guy, offer, book, might_be_followed

print("   Just An Ordinary Walk Home    \n")

def main():
    print("Welcome to 'Just An Ordinary Walk Home'!\n")
    playing = True

    while playing:
        enter_name()
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

            alive = False

            playing = False

        # if not alive:
        #     try_again = dead_retry()





if __name__ == "__main__":
    main()
