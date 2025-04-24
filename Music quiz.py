import random
import os

score = 0
admin_pass = 'Parola22!'
play_amount = 1
end_option = 0

def add_song():
    new_artist == input("Enter the artists name.")
    with open('artists.txt', 'a') as f:
        f.append(new_artist)

def end():
    end_option = int(input("What do you wish to do:\n1. Play again.\n2. Display the top 5 players. (Admin only)\n3. Add a new artist and songs."))
    return end_option

def top_five_scores():
    ("\nTop 5 Players:") #display top 5 players
    for i, (name, score) in enumerate(scores[:5]):
        print(f"{i + 1}. {name} - {score}")
        
def play_again():
    play_amount = 1

def login(play_amount):
    print("Log into your account!")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    try:
        with open('database.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() == f"{username}:{password}":
                    print("Logged in!\n")
                    return username
                
                    
    except FileNotFoundError:
        print("Account not found.")
        exit()

    print("Exiting...")
    exit()

def signup():
    print("Make a new account!")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    with open('database.txt', 'a') as f:
        f.write(f"{username}:{password}\n")
    
    print("Account created.\n")
    return login()

user_option = int(input("Choose an option:\n1. Sign up\n2. Sign in"))

if user_option == 1:
    username = signup()
elif user_option == 2:
    username = login()

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
while play_amount == 1: 
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
                parts = line.strip().split(': ')
                if len(parts) == 2 and parts[1].isdigit():
                    name, score_val = parts
                    scores.append((name, int(score_val)))

# append players score
    scores.append((username, score))

# Sort the scores in descending order
    scores.sort(key=lambda x: x[1], reverse=True)

# write scores to file
    with open('players_scores.txt', 'w') as f:
        for name, score in scores:
            f.write(f"{name}: {score}\n")

    end()
    
    if end_option == 1:
        play_amount = 1
    elif end_option == 2:
        admin_pass_input = input("Enter the Admin password:\n")
        if admin_pass_input != admin_pass:
            print("Access denied!")
            play_amount = 0
