import random
from wordlist import word_list
from hangman_art import logo
from hangman_art import stages
print(logo)
# con = input("Welcome to the game! Press F to continue: ")
# if(con == "f" or con == "F")

choice =  random.choice(word_list)
wordlen = len(choice)

end_of_game = False;
lives = 6

display = [];
for _ in range(wordlen):
    display += "_"

while not end_of_game:
    guess= input("Enter a letter: ")

    if guess in display:
        print(f"You have already guessed {guess}: ")

    for position in range(wordlen):
        letter = choice[position]

        if(letter == guess):
            display[position] = letter

    if guess not in choice:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -=1 ;
        if(lives==0):
            end_of_game = True;
            print("Game Over\n" + "You Lose Motherfucker")
            print(f"The correct word was {choice}")


    print(f"{' '.join(display) }")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages
    print(stages[lives])