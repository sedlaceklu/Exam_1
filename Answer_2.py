import random


def get_random(number=3):
    if number < 1 or number > 100:
        raise Exception("Invalid Data!")

    result = []

    while len(result) < number:
        num = random.randint(1, 100)

        if num in result:
            pass
        else:
            result.append(num)

    result.sort()
    return result


print(get_random(5))
print(get_random())
print(get_random())