#########################################################
#                Just An Ordinary Walk Home
#                  A Simple Text Adventure
#
#Author: John Michael Soza
#########################################################

from scenes_and_functions import enter_name, introduction, dead_retry, find_nickel

print("   Just An Ordinary Walk Home    \n")

def main():
    print("Welcome to 'Just An Ordinary Walk Home'!\n")
    playing = True
    scenes = 0
    while playing:
        enter_name()
        introduction()

        alive = True

        while(alive):
            # choices = get_scene(scenes)
            # scenes = get_choice(choices)
            alive = find_nickel()

        if not alive:
            try_again = dead_retry()





if __name__ == "__main__":
    main()
