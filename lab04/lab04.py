import random

wordlist = [
    "hangman",
    "llama",
    "python",
]

word = wordlist[random.randint(0, len(wordlist) - 1)]
board = list('_' * len(word))
bad_guesses = []
max_wrong = 6

while len(bad_guesses) < max_wrong and '_' in board:
    print(f"\nWelcome to HANGMAN!")
    print(board)
    print(f"\nBad Guesses: {bad_guesses}")
    
    if len(bad_guesses) == 1:
        print(f"""
        
+---+
|    
|    
|    
|
=======
""")   

    if len(bad_guesses) == 2:
        print(f"""
+---+
|   | 
|    
|    
|
=======
""")

    if len(bad_guesses) == 3:
        print(f"""
+---+
|   | 
|   O 
|    
|
=======
""")
        
    if len(bad_guesses) == 4:
        print(f"""
+---+
|   | 
|   O 
|   | 
|
=======
""")

    if len(bad_guesses) == 5:
        print(f"""
+---+
|   | 
|   O 
|  /|\\ 
|
=======
""")
        
    guess = input(f"\nGuess a letter: ")

    if len(guess) != 1 or not guess.isalpha():
        print(f"Please enter a single letter.")
        input(f"Press Enter to continue...")
        continue

    if guess in bad_guesses or guess in board:
        print(f"\nYou already guessed that letter.")
        input(f"Press Enter to continue...")
        continue

    is_found = False

    for i, letter in enumerate(word):
        if letter == guess:
            board[i] = letter
            is_found = True

    if not is_found:
        bad_guesses.append(guess)
        print(f"\n{guess} is not in the word.")

        if len(bad_guesses) == 6:
            print(f"""
+---+
|   | 
|   O 
|  /|\\ 
|  / \\
=======
""")
    else:
        print(f"\n{guess} is in the word!")
    input(f"Press Enter to continue...")

if '_' not in board:
    print(f"\nYOU WON! The word was: {word}")
else:
    print(f"\nYOU LOST! The word was: {word}")

print(f"Thanks for playing")