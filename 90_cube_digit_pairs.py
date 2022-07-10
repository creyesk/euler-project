from itertools import product, combinations
from math import comb

squares = [
    '01', '04', '06', '16', '25', '36', '46', '64', '81'
]  # substitute 9's for 6's


def replace_9_in_die(die):
    return tuple(
        x if x != '9' else '6' for x in die
    )


def can_form_squares(die_1, die_2):
    corrected_die_1 = replace_9_in_die(die_1)
    corrected_die_2 = replace_9_in_die(die_2)

    return all(
        (first_digit in corrected_die_1 and second_digit in corrected_die_2) or
        (second_digit in corrected_die_1 and first_digit in corrected_die_2)
        for first_digit, second_digit in squares
    )


def get_dice_combinations():
    eligible_numbers = '0123456789'
    die_combinations = set(combinations(eligible_numbers, 6))

    return set(product(die_combinations, die_combinations))


dice_combinations = get_dice_combinations()

valid_die_combinations = set(
    (die_1, die_2) for die_1, die_2 in dice_combinations
    if can_form_squares(die_1, die_2) and (die_1 <= die_2)
)

print(len(valid_die_combinations))
