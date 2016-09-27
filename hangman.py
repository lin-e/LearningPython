def get_match(str_guess):
    global word
    match_index = list()
    for i in range(0, len(word)):
        if word[i] == str_guess.upper():
            match_index.append(i)
    return match_index

word = input("Enter a word: ").upper()
lives = 5
guess = ""
for i in range(0, len(word)):
    guess += "*"
game_complete = False
guessed_chars = list()
while (not game_complete) and (lives > 0):
    print("So far, you have guessed: " + "".join(guess))
    print("You have " + str(lives) + " live(s) remaining.")
    keep_asking = True
    while keep_asking:
        player_guess = input("Guess a letter: ")
        if len(player_guess) == 1:
            keep_asking = False
        else:
            print("Your guess must be a single character!")
    if player_guess.upper() in guessed_chars:
        print("You have already guessed this character!")
    else:
        guessed_chars.append(player_guess.upper())
        guessed_correct = get_match(player_guess)
        temp = list(guess)
        if len(guessed_correct) > 0:
            for c in guessed_correct:
                temp[c] = player_guess.upper()
            guess = "".join(temp)
        else:
            lives -= 1
    if ("".join(guess).upper() == word):
        game_complete = True
if game_complete:
    print("You win!")
else:
    print("You lose!")
print("The word was: " + word)
