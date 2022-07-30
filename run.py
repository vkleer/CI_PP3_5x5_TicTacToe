board_marks = [' ', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']


def game_board(marks):
    """
    Prints the gameboard to the console
    """

    print('┌─────┬─────┬─────┐')
    print(f'│  {marks[0]}  │  {marks[1]}  │  {marks[2]}  │')
    print('├─────┼─────┼─────┤')
    print(f'│  {marks[3]}  │  {marks[4]}  │  {marks[5]}  │')
    print('├─────┼─────┼─────┤')
    print(f'│  {marks[6]}  │  {marks[7]}  │  {marks[8]}  │')
    print('└─────┴─────┴─────┘')


game_board(board_marks)