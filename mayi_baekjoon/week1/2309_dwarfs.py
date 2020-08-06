if __name__ == "__main__":
    height_list = list()
    for _ in range(9):
        height_list.append(int(input()))
    height_list = sorted(height_list)

    surplus = sum(height_list) - 100
    for idx_first, height_first in enumerate(height_list):
        remainder = surplus - height_first
        for idx_second, height_second in enumerate(reversed(height_list)):
            if height_second < remainder:
                break
            elif height_second == remainder:
                height_list.pop(idx_first)
                height_list.pop(7 - idx_second)
                [print(height) for height in height_list]
                exit()
