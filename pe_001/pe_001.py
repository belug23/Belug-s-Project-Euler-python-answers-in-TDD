# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_multiple_of_3_and_5_under(limit: int) -> int:
    if limit < 0:
        raise ValueError("Minimum number must be 0")
    multiples = get_multiples_of_3_and_5_under(limit)
    return sum(multiples)


def get_multiples_of_3_and_5_under(limit: int):
    multiples = []
    for num in range(limit):
        if is_multiple_of_3_or_5(num):
            multiples.append(num)
    return multiples


def is_multiple_of_3_or_5(value: int) -> bool:
    return is_multiple_of_3(value) or is_multiple_of_5(value)


def is_multiple_of_3(value: int) -> bool:
    return value % 3 == 0


def is_multiple_of_5(value: int) -> bool:
    return value % 5 == 0


if __name__ == "__main__":
    print(sum_of_multiple_of_3_and_5_under(1000))
