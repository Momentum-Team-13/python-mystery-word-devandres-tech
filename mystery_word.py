from tkinter import W
import random


def render_board(board):
    board_list = []
    for item in board:
        if not item[1]:
            board_list.append('_')
        else:
            board_list.append(item[0])
    print(' '.join(blank for blank in board_list))
    print('\n')
    return board_list


def validate_user_input(guesses_left):
    user_input = input(f'Make your guess (choose a letter). You have {guesses_left} guesses left:\n')
    while len(user_input) > 1:
        user_input = input('Please enter a single letter:\n')
    else:

        return user_input.lower()


def build_board(word):
    board = []
    for letter in word:
        board.append([letter, False])
    return board 


def validate_board(user_guess, board):
    letters = []
    invalid_guess = False
    for item in board:
        if item[0] == user_guess:
            item[1] = True

    for item in board:
        letters.append(item[0])

    if user_guess not in letters:
        invalid_guess = True
    return invalid_guess


def play_game():
    with open('./words.txt') as open_file:
        read_file = open_file.readlines()
        random_word = read_file[random.randint(0, len(read_file))]
        print(random_word)
        board = build_board(random_word.strip().lower())
        guesses_left = 8

        print(f'The magic word contains {len(random_word)} letters!')
        render_board(board)

        user_guess = validate_user_input(guesses_left)
        invalid_guess = validate_board(user_guess, board)
        if invalid_guess:
            print('Wrong guess')
            guesses_left = guesses_left - 1

        while guesses_left > 0:
            board_list = render_board(board)
            if '_' not in board_list:
                print('Congrats you won!')
                return
            user_guess = validate_user_input(guesses_left)
            invalid_guess = validate_board(user_guess, board)
            if invalid_guess:
                print('Wrong guess')
                guesses_left = guesses_left - 1 
        print(f'You lost, you ran out of guesses! correct word was: {random_word}')

if __name__ == "__main__":
    play_game()

