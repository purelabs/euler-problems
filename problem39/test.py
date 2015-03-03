from problem import concatenate_pandigital_product, solution

def test_192_n_2():
    assert concatenate_pandigital_product(192, 2) == (None, None)

def test_192_n_3():
    assert concatenate_pandigital_product(192, 3) == (3, 192384576)

def test_192_n_4():
    assert concatenate_pandigital_product(192, 4) == (4, 192384576768)

def test_192_n_2_length_9():
    assert concatenate_pandigital_product(192, 2, 9) == (None, None)

def test_192_n_3_length_9():
    assert concatenate_pandigital_product(192, 3, 9) == (3, 192384576)

def test_192_n_4_length_9():
    assert concatenate_pandigital_product(192, 4, 9) == (3, 192384576)

def test_192_n_4_length_12():
    assert concatenate_pandigital_product(192, 4, 12) == (4, 192384576768)

def test_987654321_n_1_length_9():
    assert concatenate_pandigital_product(987654321, 1, 9) == (1, 987654321)

def test_solution():
    assert solution() == (9327, 2, 932718654)
