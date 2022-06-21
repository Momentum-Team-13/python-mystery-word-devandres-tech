def render_board(word):
    board = ['_' for letter in word]
    print(' '.join(blank for blank in board))
    print('\n')


def validate_user_input():
    user_input = input('Make your guess:\n')
    while len(user_input) > 1:
        user_input = input('Please enter a single letter:\n')
    else:
        return user_input


def play_game():
    with open('./test-word.txt') as open_file:
        read_file = open_file.read()
        guess_word = read_file
        print(f'The magic word contains {len(guess_word)} letters!')
        render_board(guess_word)

        user_guess = validate_user_input()
        while user_guess != 'y':
            render_board(guess_word)
            user_guess = validate_user_input()


if __name__ == "__main__":
    play_game()

