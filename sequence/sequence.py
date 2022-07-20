def get_steps_starting_value(number: int) -> int:
    """Function that returns starting step value needed in sequence function"""
    return 1 if number > 0 else 0


def sequence(number: int) -> int:
    """Function for calculating the number of steps needed for calculation of the problem"""
    steps = get_steps_starting_value(number)

    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1

        steps += 1

    return steps


def longest_sequence(number: int) -> int:
    """Function that checks which one of the sequences has the longest number of steps"""
    longest = 0

    for i in range(number):
        if (current := sequence(i)) > longest:
            longest = current

    return longest
