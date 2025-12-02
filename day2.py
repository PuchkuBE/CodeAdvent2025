import pytest
import re

def get_invalid_ids_part1(start:int, end:int) -> list[int]:
    return [i for i in range(start, end + 1)
            if (s := str(i)) and len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]]

def get_invalid_ids_part2(start:int, end:int) -> list[int]:
    regexp = re.compile(r"^(\d+)\1+$")
    return [i for i in range(start, end + 1) if regexp.match(str(i))]
        
def main():
    # Read the file
    with open('input/input_day2.txt','r') as f:
        line = f.readline()
        ranges = line.split(",")
        invalid_ids_part1 = 0
        invalid_ids_part2 = 0
        for range in ranges:
            start, end = map(int, range.split("-"))
            invalid_ids_part1 += sum(get_invalid_ids_part1(start, end))
            invalid_ids_part2 += sum(get_invalid_ids_part2(start, end))
        print(f'The solution for day2/part1 = {invalid_ids_part1}')
        print(f'The solution for day2/part2 = {invalid_ids_part2}')

if __name__=="__main__":
    main()

@pytest.mark.parametrize(
    "start, end, expected_result",
    [
        (11, 22, 2),
        (95, 115, 1),
        (998, 1012, 1),
        (1188511880, 1188511890, 1),
        (222220, 222224, 1),
        (1698522, 1698528, 0),
        (446443, 446449, 1),
        (38593856, 38593862, 1),
        (565653,565659,0),
        (824824821,824824827,0),
        (2121212118,2121212124,0),
    ],
)
def test_invalid_part1(start, end, expected_result):
    assert len(get_invalid_ids_part1(start, end)) == expected_result

@pytest.mark.parametrize(
    "start, end, expected_result",
    [
        (11, 22, 2),
        (95, 115, 2),
        (998, 1012, 2),
        (1188511880, 1188511890, 1),
        (222220, 222224, 1),
        (1698522, 1698528, 0),
        (446443, 446449, 1),
        (38593856, 38593862, 1),
        (565653,565659,1),
        (824824821,824824827,1),
        (2121212118,2121212124,1),
    ],
)
def test_invalid_part2(start, end, expected_result):
    assert len(get_invalid_ids_part2(start, end)) == expected_result
