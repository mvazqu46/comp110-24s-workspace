"""Ex03 Functional Battleship."""
import random
__author__ = "730718822"


""""""


def input_guess(grid_size: int, type_: str) -> int:
    assert type_ == "row" or type_ == "column", f"Invalid guess_type: {type_}"
    while True:
        guess = input(f"Guess a {type_}: ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= grid_size:
                return guess
            else:
                print(f"The grid is only {grid_size} by {grid_size}. Try again:", end=" ")


""""""


if __name__ == "__main__":
    grid_size = 4
    print(input_guess(grid_size, "row"))


""""""


def print_grid(grid_size: int, row_guess: int, col_guess: int, correct: bool) -> None:
    emoji_correct = "\U0001F7E5"
    emoji_incorrect = "\U0001F7E6"
    for row in range(1, grid_size + 1):
        for col in range(1, grid_size + 1):
            if row == row_guess and col == col_guess:
                print(emoji_correct if correct else emoji_incorrect, end="")
            else:
                print(emoji_incorrect, end="")
        print()


""""""
# Testing print_grid function
if __name__ == "__main__":
    grid_size = 4
    row_guess, col_guess = 3, 2
    print_grid(grid_size, row_guess, col_guess, True)


""""""


def correct_guess(secret_row: int, secret_col: int, guess_row: int, guess_col: int) -> bool:
    return secret_row == guess_row and secret_col == guess_col


""""""


if __name__ == "__main__":
    print(correct_guess(4, 4, 3, 1))


""""""


def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    turns = 5
    for turn in range(1, turns + 1):
        print(f"=== Turn {turn}/{turns} ===")
        guess_row = input_guess(grid_size, "row")
        guess_col = input_guess(grid_size, "column")
        if correct_guess(secret_row, secret_col, guess_row, guess_col):
            print_grid(grid_size, guess_row, guess_col, True)
            print("Hit!")
            print(f"You won in {turn}/{turns} turns!")
            return
        else:
            print_grid(grid_size, guess_row, guess_col, False)
            print("Miss!")
    print(f"X/{turns} - Better luck next time!")


if __name__ == "__main__":
    grid_size = random.randint(3, 5)
    secret_row = random.randint(1, grid_size)
    secret_col = random.randint(1, grid_size)
    main(grid_size, secret_row, secret_col)