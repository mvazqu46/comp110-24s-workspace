"""One shot battleship."""
__author__ = "730718822"

'#Start of the variables:'
blue_box: str = "\U0001F7E6"
red_box: str = "\U0001F7E5"
white_box: str = "\U00002B1C"
sz_grid: int = 4
secret_row: int = 3
secret_column: int = 2
message_hit: str = "Hit!"
message_miss: str = "Miss!"
'# Guess a row'
while True:
    guess_row = int(input("Guess a row: "))
    if 1 <= guess_row <= sz_grid:
        break
    else:
        print(f"The grid is only {sz_grid} by {sz_grid}. Try again: ")
'# Guess a column'
while True:
    guess_column = int(input("Guess a column: "))
    if 1 <= guess_column <= sz_grid:
        break
    else:
        print(f"The grid is only {sz_grid} by {sz_grid}. Try again: ")
'# Code for grid printing'
grid_row = 1
while grid_row <= sz_grid:
    emoji_row = ""
    grid_column = 1
    while grid_column <= sz_grid:
        if guess_row == grid_row and guess_column == grid_column:
            if guess_row == secret_row and guess_column == secret_column:
                emoji_row += red_box 
            else:
                emoji_row += white_box  
        else:
            emoji_row += blue_box  
        grid_column += 1
    print(emoji_row)
    grid_row += 1
'# Hit, Miss, or Hint'
if guess_row == secret_row and guess_column == secret_column:
    print(message_hit)
elif guess_row == secret_row or guess_column == secret_column:

    print("Close! Correct row, wrong column." if guess_row == secret_row else "Close! Correct column, wrong row.")
else:
    print(message_miss)