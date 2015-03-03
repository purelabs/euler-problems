from problem import concatenate_product, solution

def test_192_n_1():
    assert concatenate_product(192, 1) == (1, 192)

def test_192_n_3():
    assert concatenate_product(192, 3) == (3, 192384576)

def test_192_n_5():
    assert concatenate_product(9, 5) == (5, 918273645)

def test_192_n_2_length_3():
    assert concatenate_product(192, 2, 3) == (1, 192)

def test_solution_1():
    assert solution(1) == (1, 9)

def test_solution_2():
    assert solution(2) == (2, 99)
