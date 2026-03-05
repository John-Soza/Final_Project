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
    print("You had an arduous but strangely rewarding day at work, and on your way \nhome you made a stop at your favorite department store to buy some new \nclothes to reward yourself.\n")
    print("The weight and feel of the store's designer bag adds a small boost to \nyour confidence.")

#introduction()
