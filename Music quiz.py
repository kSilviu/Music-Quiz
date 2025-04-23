import random
import os

score = 0
Name = None
Password = None

def login():
    Name = input("Enter username")
    Password = input("Enter Password")
    auth = 0
    
    try:
        with open('database.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() = f"{Name}:{Password}:
                    auth = 1
                    break
        except FileNotFoundError:
            print("Account not found")
            return False
            
        if auth:
            return True
        else:
            return False 
            
def signup():
    Name = input("Enter username")
    Password = input("Enter password")
    with open('database.txt', 'a') as f:
        f.weite(f"{Name}:{Password}\n")
    login()


user_option = int(input("Choose an option:\n1. Sign up\n2. Sign in"))

artists = ['Deftones', '$uicideboy$', 'BONES']
deftones_songs = ['Change', 'Rosemary', 'Mascara']
suicideboys_songs = ['Antarctica', 'Paris', 'Coma']
BONES_songs = ['HDMI', 'Sodium', 'Rocks']

# Writing song lists to files
with open('deftones.txt', 'w') as f:
    for item in deftones_songs:
        f.write(f"{item}\n")

with open('suicideboys.txt', 'w') as f:
    for item in suicideboys_songs:
        f.write(f"{item}\n")

with open('BONES.txt', 'w') as f:
    for item in BONES_songs:
        f.write(f"{item}\n")

with open('artist.txt', 'w') as f:
    for item in artists:
        f.write(f"{item}\n")

# Reading the list of artists
with open("artist.txt", "r") as f:
    artist_list = [line.strip() for line in f if line.strip()]

artist_random = random.choice(artist_list) # pick an artist

if artist_random == "Deftones":
    with open('deftones.txt', "r") as f:
        song_list = [line.strip() for line in f if line.strip()]
        song_guess = random.choice(song_list)
elif artist_random == "$uicideboy$":
    with open('suicideboys.txt', "r") as f:
        song_list = [line.strip() for line in f if line.strip()]
        song_guess = random.choice(song_list)
elif artist_random == "BONES":
    with open('BONES.txt', "r") as f:
        song_list = [line.strip() for line in f if line.strip()]
        song_guess = random.choice(song_list)

song_first_letter = song_guess[0]

#guess song
guess = input(f"Guess thesong from {artist_random} - {song_first_letter}: ")

# Check the first guess 
if guess == song_guess:
    score += 2
    print(f"Correct!")
else:
    guess = input(f"Try again!\n")
    if guess == song_guess:
        score += 1
        print(f"Correct!")
    else:
        print(f"The correct answer was {artist_random} - {song_guess}.")
        exit()

print(f"Your final score is: {score}") #output score

scores = []
if os.path.exists('players_scores.txt'):
    with open('players_scores.txt', 'r') as f:
        for line in f:
            name, score = line.strip().split(': ')
            scores.append((name, int(score)))

# append players score
scores.append((username, score))

# Sort the scores in descending order
scores.sort(key=lambda x: x[1], reverse=True)

# write scores to file
with open('players_scores.txt', 'w') as f:
    for name, score in scores:
        f.write(f"{name}: {score}\n")

print("\nTop 5 Players:") #display top 5 players
for i, (name, score) in enumerate(scores[:5]):
    print(f"{i + 1}. {name} - {score}")
