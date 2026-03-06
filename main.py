#########################################################
#                Just An Ordinary Walk Home
#                  A Simple Text Adventure
#
#Author: John Michael Soza
#########################################################

from scenes_and_functions import enter_name, introduction, find_nickel, alley_guy, offer

print("   Just An Ordinary Walk Home    \n")

def main():
    print("Welcome to 'Just An Ordinary Walk Home'!\n")
    playing = True

    while playing:
        enter_name()
        introduction()

        alive = True

        while alive:
            # choices = get_scene(scenes)
            # scenes = get_choice(choices)
            alive = find_nickel()
            alive = alley_guy()
            offer()

            playing = False

        # if not alive:
        #     try_again = dead_retry()





if __name__ == "__main__":
    main()
