def concatenate_pandigital_product(x, y, length=None):
    value = ''
    contained_digits = set()
    result = (None, None)

    for n in range(1, y+1):
        p = str(x*n)
        if (length and len(value) + len(p) > length) or ('0' in p):
            n -= 1
            break
        value += p
        value_int = int(value)
        contained_digits.update(p)

        if len(contained_digits) == 9 and (not result[1] or value_int > result[1]):
            result = (n, value_int)

    return result


def solution():
    max_x, max_y, max_value = None, None, None

    for x in range(1, 10000):
        y, value = concatenate_pandigital_product(x, 9, 9)

        if y > 1 and value > max_value:
            max_x, max_y, max_value = x, y, value

    return (max_x, max_y, max_value)
