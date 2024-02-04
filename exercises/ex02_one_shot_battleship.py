"""One shot Battleship!"""
__author__= "730718822"

#Start of the variables:
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
sz_grid: int = 4
secret_row: int = 3
secret_column: int = 2
message_hit: str = "Hit!"
message_miss: str = "Miss!"

#Start of the code:
while True:
    guess_row: str = input("Guess a row: ")
    guess_row2: int = int(guess_row)
    guess_column: str = input("Guess a column: ")
    guess_column2: int = int(guess_column)
    counter_row: int = 1
    counter_column: int = 1
    emoji_row: str = ""
    guess_correct = (guess_row2 == secret_row) and (guess_column2 == secret_column)
    result_box = RED_BOX if guess_correct else WHITE_BOX

    if 0 <= guess_row2 < sz_grid and 0 <= guess_column2 < sz_grid:
        pass
    else:
        print(f"The grid is only {sz_grid} by {sz_grid}. Try again:")
    while counter_row <= sz_grid:
        emoji_row = ""
        counter_column = 1
        if guess_row2 == counter_row:
            while counter_column <= sz_grid:
                if guess_column2 == counter_column:
                    emoji_row += result_box
                else:
                    emoji_row += BLUE_BOX
                counter_column += 1
        else:
            while counter_column <= sz_grid:
                emoji_row += BLUE_BOX
                counter_column += 1
        print(emoji_row)
        counter_row += 1
    if guess_correct:
        print(message_hit)
    else:
        print(message_miss) 
