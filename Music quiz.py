import random
import os

admin_pass = 'Parola22!'
play_amount = 1
end_option = 0


def add_song():
    new_artist = input("Enter the artist's name: ").strip()
    
    # Check if the artist already exists
    with open('artist.txt', 'r') as f:
        existing_artists = [line.strip() for line in f]
    
    if new_artist in existing_artists:
        print(f"Artist {new_artist} already exists.")
        return
    
    with open('artist.txt', 'a') as f:
        f.write(new_artist + '\n')
    
    try:
        num_songs = int(input("How many songs do you want to add?"))
    except ValueError:
        print("Enter a valid number")
        return
    
    songs = []
    for i in range(num_songs):
        song = input(f"Enter song {i + 1}: ").strip()
        songs.append(song)
    
    filename = f"{new_artist.lower().replace(' ', '')}.txt"
    with open(filename, 'w') as f:
        for song in songs:
            f.write(song + '\n')

    print(f"{new_artist} and their songs have successfully been added to the database.")

def end():
    while True:
        try:
            choice = int(input("Choose one of the following:\n1. Play again\n2. Display the top 5 players (Admin only)\n3. Add a new artist (Admin only)\n4. Quit"))
            if choice in [1,2,3,4]:
                return choice
            else:
                print("Choose a valid choice")
        except ValueError:
            print("Please enter a number")
                

def top_five_scores(scores):
    print("\nTop 5 Players:") #display top 5 players
    for i, (name, score) in enumerate(scores[:5]):
        print(f"{i + 1}. {name} - {score}")
        
def login():
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

deftones_songs = ['Change', 'Rosemary', 'Mascara']
suicideboys_songs = ['Antarctica', 'Paris', 'Coma']
BONES_songs = ['HDMI', 'Sodium', 'Rocks']

if not os.path.exists('artist.txt'):
    artists = ['Deftones', '$uicideboy$', 'BONES']
    with open('artist.txt', 'w') as f:
        for item in artists:
            f.write(f"{item}\n")
    
    song_data = {
        'deftones.txt': ['Change', 'Rosemary', 'Mascara'],
        'suicideboys.txt': ['Antarctica', 'Paris', 'Coma'],
        'bones.txt': ['HDMI', 'Sodium', 'Rocks']
    }
    for filename, songs in song_data.items():
        with open(filename, 'w') as f:
            for song in songs:
                f.write(f"{song}\n")

# Reading the list of artists
while play_amount == 1:
    score = 0
    with open("artist.txt", "r") as f:
        artist_list = [line.strip() for line in f if line.strip()]

    artist_random = random.choice(artist_list) # pick an artist

    filename = f"{artist_random.lower().replace(' ', '')}.txt"
            
    if os.path.exists(filename):
        with open(filename, "r") as f:
            song_list = [line.strip() for line in f if line.strip()]
            song_guess = random.choice(song_list)
    else:
        print(f"No song file found for {artist_random}. Skipping...")
        continue

    song_first_letter = song_guess[0]

#guess song
    guess = input(f"Guess the song from {artist_random} - {song_first_letter}: ")

# Check the first guess 
    if guess.strip().lower() == song_guess.lower():
        score += 2
        print(f"Correct!")
    else:
        guess = input("Try again!\n")
        if guess.strip().lower() == song_guess.lower():
            score += 1
            print(f"Correct!")
        else:
            print(f"The correct answer was {artist_random} - {song_guess}.")

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
        for name, score_val in scores:
            f.write(f"{name}: {score_val}\n")

    end_option = end()

    if end_option == 1:
        continue
    elif end_option == 2:
        admin_pass_input = input("Enter the Admin password:\n")
        if admin_pass_input != admin_pass:
            print("Access denied!")
        else:
            top_five_scores(scores)
            exit()
    elif end_option == 3:
        admin_pass_input = input("Enter the Admin password:\n")
        if admin_pass_input != admin_pass:
            print("Access denied!")
        elif admin_pass_input == admin_pass:
            add_song()
            exit()
        else:
            exit()
    elif end_option == 4:
        print("Exiting...")
        exit()
