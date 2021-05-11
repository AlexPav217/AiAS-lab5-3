import math
import sys


def alg_complement(matrix, row_index, col_index):
    rang = len(matrix)
    new_matrix = []
    counter = -1
    for i in range(rang):
        if i != row_index:
            new_matrix.append([])
            counter += 1
        for j in range(rang):
            if i != row_index and j != col_index:
                new_matrix[counter].append(matrix[i][j])
    return new_matrix


def determinant(matrix):
    det = 0
    for i in range(len(matrix)):
        complement = alg_complement(matrix, 0, i)
        if len(complement) == 1:
            det = (det * (-1) + matrix[0][i] * complement[0][0])
        elif len(complement) == 0:
            det = -matrix[0][0]
        else:
            det = det + matrix[0][i] * determinant(complement) * math.pow(-1, i + 1)
    return det * (-1)


def get_transposed_matrix(matrix):
    transposed_matrix = []
    for i in range(len(matrix)):
        transposed_matrix.append([])
        for j in range(len(matrix[i])):
            transposed_matrix[i].append(matrix[j][i])
    return transposed_matrix


def get_inverse_matrix(matrix):
    inverse_matrix = []
    det = determinant(matrix)
    if det == 0:
        print("Решений нет или их бесконечно много")
        sys.exit()
    for i in range(len(matrix)):
        inverse_matrix.append([])
        for j in range(len(matrix[i])):
            inverse_matrix[i].append(
                (1 / det) * determinant(alg_complement(matrix, i, j)) * math.pow((-1), (j + i)))
    return get_transposed_matrix(inverse_matrix)


def multiply_by_vector(matrix, vector):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(0)
        for j in range(len(matrix[i])):
            new_matrix[i] += matrix[i][j] * vector[j]
    return new_matrix


def get_unknown_members(matrix, answer_vector):
    det = determinant(matrix)
    if det == 0:
        print("Решений нет или их бесконечно много")
        sys.exit()
    inverse_matrix = get_inverse_matrix(matrix)
    unknown_vector = multiply_by_vector(inverse_matrix, answer_vector)
    return unknown_vector


if __name__ == '__main__':
    matrix_str = input("Введите матрицу в строку, разделение между числами-пробел\n")
    matrix_str = matrix_str.split()
    rang = math.sqrt(len(matrix_str))
    if not rang.is_integer():
        raise IOError("Матрица должна быть квадратная")
    matrix = []
    counter = 0
    for i in range(int(rang)):
        matrix.append([])
        for j in range(int(rang)):
            matrix[i].append(int(matrix_str[counter]))
            counter += 1
    answer_vector = [int(x) for x in input
        ("Введите свободные члены уравнения\n").split()]
    if len(answer_vector) != len(matrix):
        raise IOError("Ранг матрицы должен совпадать с количеством свободных членов")
    print(get_unknown_members(matrix, answer_vector))
