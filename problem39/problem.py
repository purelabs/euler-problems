def concatenate_product(x, y, length=None):
    result = ''
    for n in range(1, y + 1):
        p = str(x*n)
        if length and len(result) + len(p) > length:
            n -= 1
            break
        result += p

    return (n, int(result))


def solution(length):
    max_y = 0
    max_value = 0

    for i in range(1, 10**length):
        y, value = concatenate_product(i, length, length)

        if value > max_value:
            max_value = value
            max_y = y

    return (max_y, max_value)
