import random
import ast

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

artists = ['Deftones', '$uicideboy$','BONES']
deftones_songs = ['Change', 'Rosemary', 'Mascara']
suicideboys_songs = ['Antarctica', 'Paris', 'Coma']
BONES_songs = ['HDMI', 'Sodium', 'Rocks']

with open('deftones.txt', "w") as f: #write to file
    for item in deftones_songs:
        f.write(f"{item}\n")

with open('suicideboys.txt', "w") as f: #write to file
    for item in suicideboys_songs:
        f.write(f"{item}\n")

with open('BONES.txt', 'w') as f: #write to file
    for item in BONES_songs:
        f.write(f"{item} \n")

with open("artist.txt", "w") as f: #write to file
    for item in artists:
        f.write(f"{item}\n")

with open("artists.txt", "r") as f: #reads the list of artists
    data = f.read()

artist_list = ast.literal_eval(data) #re arranges back into a list
artist_random_guess = random.choice(artist_list) #pick one of the 3 artists

if artist_random_guess == "Deftones":
    with open('deftones.txt', "r") as f:
        song_list = [line.strip() for line in f if line.strip()]
        song_guess = random.choice(song_list)

elif artist_random_guess == "$uicideboy$":
    with open('suicideboys.txt', "r") as f:
        song_list = [line.strip() for line in f if line.strip()]
        song_guess = random.choice(song_list)

elif artist_random_guess == "BONES":
    with open('BONES.txt', "r") as f:
        song_list = [line.strip() for line in f if line.strip()]
        song_guess = random.choice(song_list)

print(artist_random_guess)
print(song_guess)