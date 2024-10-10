
def get_input(filepath: str):
    with open(filepath, "r") as f:
        return f.readlines()

def get_first_and_last_number(input_string: str) -> int:
    only_digits = [c for c in input_string if c.isnumeric()]
    if len(only_digits) < 2:
        only_digits.append(only_digits[0])
    return int(f"{only_digits[0]}{only_digits[-1]}")

def get_all_numbers(string_lines):
    return (get_first_and_last_number(line) for line in string_lines)


if __name__ == '__main__':
    input_data = get_input("part-1-input.txt")
    print(sum(get_all_numbers(input_data)))
