"""
Source: https://www.acmicpc.net/problem/1018
Time: 64ms
Rank: 9th
"""

# def make_chess_board(m, n):
#     chess_board = list()
#     for i in range(m):
#         temp_row = list()
#         for j in range(n):
#             temp_row.append((i + j) % 2)
#         chess_board.append(temp_row)
#     return chess_board

# def parse_input(input_list, m, n):
#     input_board = list()
#     for i, row in enumerate(input_list):
#         temp_row = list()
#         for j, col in enumerate(row):
#             temp_row.append((1 if col == "B" else 0))
#         input_board.append(temp_row)
#     return input_board

# def cumsum(ndarray, axis):
#     new_ndarray = list()
#     if axis == 1:
#         for row in ndarray:
#             new_row = list()
#             cum = 0
#             for r in row:
#                 cum += r
#                 new_row.append(cum)
#             new_ndarray.append(new_row)
#         return new_ndarray
#     elif axis == 0:
#         ndarray = list(zip(*ndarray))
#         return list(zip(*cumsum(ndarray, axis=1)))

# def pad(ndarray):
#     new_mat = list()
#     new_mat.append([0 for _ in range(len(ndarray[0]) + 1)])
#     for row in ndarray:
#         new_mat.append([0] + list(row))
#     return new_mat

# def make_integral_img(board):
#     return pad(cumsum(cumsum(board, axis=1), axis=0))

# def mat_sub_abs(mat1, mat2):
#     new_mat = list()
#     for mat1_row, mat2_row in zip(mat1, mat2):
#         new_mat.append([abs(m1 - m2) for m1, m2 in zip(mat1_row, mat2_row)])
#     return new_mat

def get_min_error(input_list, n):
    integral_img = [[0]*(n + 1)]
    min_error = 64
    b_or_w = ["B", "W"]
    for i, row in enumerate(input_list):
        tmp = 0
        integral = [0]
        for j, col in enumerate(row):
            v = (col == b_or_w[(i + j) % 2])
            tmp += integral_img[i][j + 1] + v - integral_img[i][j]
            integral.append(tmp)
            if i < 7 or j < 7:
                pass
            else:
                error = (tmp +
                        integral_img[i - 7][j - 7] -
                        integral[j - 7] -
                        integral_img[i - 7][j + 1])
                min_error = min(error, 64 - error, min_error)
        integral_img.append(integral)
    return min_error


if __name__ == "__main__":
    m, n = input().split(" ")
    m, n = int(m), int(n)

    input_list = list()
    for _ in range(m):
        input_list.append(input())

    # input_board = parse_input(input_str, m, n)
    # chess_board = make_chess_board(m, n)
    # integral_img = make_integral_img(mat_sub_abs(chess_board, input_board))

    # error_list = list()
    # for i in range(m - 7):
    #     for j in range(n - 7):
    #         error = (integral_img[i + 8][j + 8] + 
    #                 integral_img[i][j] -
    #                 integral_img[i + 8][j] -
    #                 integral_img[i][j + 8])
    #         error_list.append(int(min(error, 64 - error)))

    min_error = get_min_error(input_list, n)

    print(min_error)
