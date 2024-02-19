import random
#greeting
print("Welcome to Hangman! The objective of this game is to guess letters in the word. \n You have 10 guesses good luck!")

#list of words to use in hangman
word_list = ['number', 'coffee', 'python', 'bird', 'cisco']

#empty list of guessed letters, it will take the random word from word list and fill it up with "_"
guessed_letters = []

#this selects a random word from the list
words = random.choice(word_list)


#fills up selected word with "_"
for letter in words:
    guessed_letters += '_'

#function to get player difficulty, it will loop until a proper input is selected
def user_difficulty():
    correct_input = False
    while not correct_input:
        difficulty = input("Please select difficulty, press 1 for easy, 2 for medium, 3 for hard: ")
    
        if difficulty == '1':
            attempts = 12
            correct_input = True
        
        elif difficulty == '2':
            attempts = 9
            correct_input = True
        
        elif difficulty == '3':
            attempts = 7
            correct_input = True
        
        else:
            print("Invalid selection, please enter 1, 2, or 3: ")
    return attempts 

        

        
            

attempts = user_difficulty()
print(f"You have {attempts} attempts, good luck!")
game_over = False
#hangman game, in a while loop. it calls the number of attempts from difficulty with a pre-defined boolean to continuously run the game until attempts == 0
while not game_over and attempts > 0:
    guess = input("Guess a letter: ").lower()
    attempts -= 1
    for position in range(len(words)):
        letter = words[position]
        
        if letter == guess:
            guessed_letters[position] = letter
            print(guessed_letters)
            
        if '_' not in guessed_letters:
            print("You win!")
            game_over = True
        
    if letter != guess:
        print(f"Incorrect! You have {attempts} attempts left!")
        print(guessed_letters)
        
if game_over is False and attempts == 0:
    print("Sorry you lost :( ")
    print(f"The correct word was {words}!")

