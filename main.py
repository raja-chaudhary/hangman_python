''' The famous hangman game that lets you guess the word letter by letter. If you guess correct the blanks in will get replaced with the correct alphabet but if your guess is incorrect you will lose a limb. You only stay alive till you lose all your limbs hence you only get 7 lives (you will lose after 7th incorrect guess)'''


# importing methods and lists from other modules
import random
from hangman_art import logo, stages
from hangman_words import letter_list, word_list

# printing the hangman logo upon start
print(logo)

# assigning the total number of lives
lives = 7

# randomly choosing a word from a list of 200+ words
chosen_word = random.choice(word_list)

# saving the length of the chosen word in a seperate variable
word_length = len(chosen_word)

# creating blanks in place of alphates of the word
display = []
for _ in range(word_length):
    display += "_"

# adding a while loop to run the game till the condition is true
game_active = True
while game_active:

    # taking input from the user
    guess = input("\nGuess a letter: ").lower()


# checking guessed letter
    if guess in letter_list:
        # remove the guessed letter from the list
        letter_list.remove(guess)
        # checking the guessed letter at every position of the word
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                # replacing '_' with the guessed letter
                display[position] = letter
        if guess not in chosen_word:
            print(
                f'The letter {guess} is not in the word. You lose a life!')
            lives -= 1                      # reduce life by 1 if guess is incorrect
            print(stages[lives])            # printing the hanged man
        if lives == 0:
            print('You Lost')
            print(f'Pssst, the solution is {chosen_word}.')
            game_active = False             # ending the loop once the player loses
        if '_' not in display:
            print('You Won.....')
            game_active = False
        print(' '.join(display))
    else:
        print(f'You have already guessed this letter {guess}')
        print(' '.join(display))
