
def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.readlines()

def replace_spelling_with_numbers(input_string: str, reverse = False) -> str:
    spelling_to_number = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    if reverse:
        input_string = input_string[::-1]
        spelling_to_number = {key[::-1]: value for key,value in spelling_to_number.items()}
    for i in range(len(input_string)):
        for spell, number in spelling_to_number.items():
            if input_string[i:].startswith(spell) or input_string[i:].startswith(number):
                return number

def get_first_and_last_number(input_string: str) -> int:
    first_number = replace_spelling_with_numbers(input_string)
    second_number = replace_spelling_with_numbers(input_string, reverse=True)
    return int(f"{first_number}{second_number}")

def get_all_numbers(string_lines):
    return [get_first_and_last_number(line) for line in string_lines]


if __name__ == '__main__':
    input_data = get_input("input.txt")
    numbers_by_line = get_all_numbers(input_data)
    for line, number in zip(input_data, numbers_by_line):
        print(line.replace('\n', '') + f" - {number}")
    print(sum(numbers_by_line))
