n = 5

test_matrix = [[i + j for i in range(1, n + 1)] for j in range(0, n * n, n)]

for line in test_matrix:
    print(line)

print('-' * 100)


def traverse_matrix(matrix: list[list[int]], output: object = None) -> list[int]:
    """
    Function to traverse matrix in the revert clockwise order
    Args:
        matrix (list[list[int]]): matrix object to traverse
        output (list[int]): help variable for recursive runs.
                            You don't need to provide for initial run
    Returns:
        (list[int]): traversed matrix
    """
    if output is None:
        output = []

    if not len(matrix):
        return output

    matrix = list(zip(*matrix[::-1]))
    output.extend(matrix[0][::-1])
    return traverse_matrix(matrix[1:], output)


if len(test_matrix):
    new_list = traverse_matrix(test_matrix)
    print(new_list)
    print(len(new_list))
else:
    print('The matrix is empty!')