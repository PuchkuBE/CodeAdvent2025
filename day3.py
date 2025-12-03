import pytest

def largestJoltage(pack: str, size:int) -> str:
    if size == 1:
        return max(pack)
    else:
        j = pack.find(max(pack[:-size+1]))
        return pack[j] + largestJoltage(pack[j+1:], size - 1)

def main():
    lines = open('input/input_day3.txt','r').read().split()
    
    solution1 = solution2 = 0
    for pack in lines:
        solution1 += int(largestJoltage(pack[:-1], 2))
        solution2 += int(largestJoltage(pack[:-1], 12))

    print(f'The solution for day3/part1 = { solution1}')    
    print(f'The solution for day3/part2 = { solution2}')
 
if __name__=="__main__":
    main()


## TESTS ############################################

@pytest.mark.parametrize(
    "pack, expected_result",
    [
        ("987654321111111", "98"),
        ("811111111111119", "89"),
        ("234234234234278","78"),
        ("818181911112111","92"),
        ("1564299121512","99"),
        ("135165131389","89"),
        ("135165131398","98"),
    ],
)
def test_largestJoltage2(pack, expected_result):
    assert largestJoltage(pack,2) == expected_result

@pytest.mark.parametrize(
    "pack, expected_result",
    [
        ("987654321111111", "987654321111"),
        ("811111111111119", "811111111119"),
        ("234234234234278","434234234278"),
        ("818181911112111","888911112111"),
    ],
)
def test_largerLargestJoltage12(pack, expected_result):
    assert largestJoltage(pack,12) == expected_result