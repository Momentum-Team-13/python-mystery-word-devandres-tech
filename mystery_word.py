def render_board(board):
    board_list = []
    print(board)
    for item in board:
        if not item[1]:
            board_list.append('_')
        else:
            board_list.append(item[0])
    print(' '.join(blank for blank in board_list))
    print('\n')


def validate_user_input(guesses_left):
    user_input = input(f'Make your guess (choose a letter). You have {guesses_left} guesses left:\n')
    while len(user_input) > 1:
        user_input = input('Please enter a single letter:\n')
    else:
        return user_input


def build_board(word):
    board = []
    for letter in word:
        board.append([letter, False])
    return board 


def validate_board(user_guess, board):
    for item in board:
        if item[0] == user_guess:
            item[1] = True


def play_game():
    with open('./test-word.txt') as open_file:
        read_file = open_file.read()
        guess_word = read_file.strip()
        board = build_board(guess_word)
        guesses_left = 8

        print(f'The magic word contains {len(guess_word)} letters!')
        render_board(board)

        user_guess = validate_user_input(guesses_left)
        validate_board(user_guess, board)
        while user_guess != 'y':
            render_board(board)
            user_guess = validate_user_input(guesses_left)
            validate_board(user_guess, board)


if __name__ == "__main__":
    play_game()

