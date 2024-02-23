"""EX04 List Utility Functions."""
__author__ = "730718822"


def all(numbers: list[int], target: int) -> bool:
    """Importing all numbers."""
    if not numbers:
        return False
    for num in numbers:
        if num != target:
            return False
    return True


def max(input: list[int]) -> int:
    """Importing max numbers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_val = input[0]
    for num in input[1:]:
        if num > max_val:
            max_val = num
    return max_val

                
def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Importing is_equal for numbers."""
    if len(list1) != len(list2):
        return False 
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
 

def extend(list1: list[int], list2: list[int]) -> None:
    """Importing extend for numbers."""
    list1.extend(list2)