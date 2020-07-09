from random import randint


def get_random_valid_phone_number():
    return '8085' + str(randint(100000, 900000))


def get_rand_number_between_zero_to_max_number(max_number, min_number=0):
    return randint(min_number, max_number)
