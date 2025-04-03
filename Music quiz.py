
#███╗░░░███╗░█████╗░██████╗░███████╗  ██████╗░██╗░░░██╗  ░██████╗██╗██╗░░░░░██╗░░░██╗██╗██╗░░░██╗
#████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚██╗░██╔╝  ██╔════╝██║██║░░░░░██║░░░██║██║██║░░░██║
#██╔████╔██║███████║██║░░██║█████╗░░  ██████╦╝░╚████╔╝░  ╚█████╗░██║██║░░░░░╚██╗░██╔╝██║██║░░░██║
#██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░  ██╔══██╗░░╚██╔╝░░  ░╚═══██╗██║██║░░░░░░╚████╔╝░██║██║░░░██║
#██║░╚═╝░██║██║░░██║██████╔╝███████╗  ██████╦╝░░░██║░░░  ██████╔╝██║███████╗░░╚██╔╝░░██║╚██████╔╝
#╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝╚══════╝░░░╚═╝░░░╚═╝░╚═════╝░

username = None
password = None

def auth():#check if user is allowed to play game
    username = input("enter username")
    password = input("enter password")

    if username == "Silviu":
        if password == "Password":
            return print("Welcome to the Music Quiz!")
    elif username == "Nyphro":
        if password == "Password":
            return print("Welcome to the Music Quiz!")
    else:
        print("Access denied!")

auth() #Authenticate that user can play game

## Part 1 ^^^^^^^^^

artist = open("artist.txt", "w")
artist.write(["","","","","",""])
