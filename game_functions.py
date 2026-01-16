import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = poss_values[len(poss_values)//2]
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if user_input == "h" and (current_val < next_val):
        return True
    elif user_input == "l" and (current_val > next_val):
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    word_list = list(word)
    in_word = False
    for i in range(len(word_list)):
        if letter == word_list[i]:
            board[i] = letter
            in_word = True
    if in_word:
        print(f"Well done {letter} is in the word")
        return True
    else:
        print(f"Sorry, {letter} is not in the word")
        return False
