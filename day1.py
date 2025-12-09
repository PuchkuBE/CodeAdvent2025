from collections import namedtuple
from re import L

Move = namedtuple('Move',['direct','steps'])

def make_move_b(start:int, move:Move) -> tuple[int,int]:    
    """Make a move, starting from start, used for part b

    Args:
        start (int): the starting position
        move (Move): a tuple, indicating the direction and number of steps

    Returns:
        tuple[int, int]: (the end position after making the move, nr of times zero was passed)
    """    
    #print(f'Currently at {start} and moving {move.steps} to {move.direct}')
    new_pos = start
    match move.direct:
        case 'R':
            new_pos += move.steps
        case 'L':
            new_pos -= move.steps
        case _:
            print("Invalid move")
    zero_passes, corrected_pos = divmod(new_pos, 100)
    #print(f'Result of divmod: {zero_passes, corrected_pos}')
    zero_passes = abs(zero_passes)
    #print(f'Starting from position {start} and turning {move.steps} in the {move.direct} direction passes zero {zero_passes} times')
    return (corrected_pos,abs(zero_passes))

def make_move(start:int, move:Move) -> int:    
    """Make a move, starting from start, used for part 1

    Args:
        start (int): the starting position
        move (Move): a tuple, indicating the direction and number of steps

    Returns:
        int: the end position after making the move
    """    
    end, _ = make_move_b(start, move)
    return end

def ex1(lines: str, starting_pos: int) -> int:
    """Day1 - part 1 of the advent of code

    Args:
        lines (str): the input lines (movements in format R12)
        starting_pos (int): the starting position of the exercise

    Returns:
        int: the number of times that the move ended on the zero position
    """   
    # Read in each line as a move
    new_pos = starting_pos
    ends_on_zero = 0

    for line in lines:
        move = Move(line[0], int(line[1:-1])) 
        new_pos = make_move(new_pos, move)
        if new_pos == 0:
            ends_on_zero += 1
    return ends_on_zero

def ex1_b(lines: str, starting_pos: int) -> int:
    """Day1 - part 1 of the advent of code

    Args:
        lines (str): the input lines (movements in format R12)
        starting_pos (int): the starting position of the exercise

    Returns:
        int: the number of times that the move passed or ended on the zero position
    """   
    # Read in each line as a move
    new_pos = starting_pos
    zero_passes = 0

    for line in lines:
        move = Move(line[0], int(line[1:-1])) 
        new_pos, nr_passes = make_move_b(new_pos, move)
        zero_passes += nr_passes

    return zero_passes

def main():
    # Read the file
    with open('input/day1.txt','r') as f:
        lines = f.readlines()
    
    solution1 = ex1(lines,50)
    solution2 = ex1_b(lines, 50)
    print(f'The solution for day1/part1 = { solution1}')
    print(f'The solution for day1/part2 = { solution2}')

    
if __name__=="__main__":
    main()