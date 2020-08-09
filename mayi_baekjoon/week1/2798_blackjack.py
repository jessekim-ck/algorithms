"""
Source: https://www.acmicpc.net/problem/2798
Time: 72ms
Rank: 25th
"""

if __name__ == "__main__":

    n, m = input().split(" ")
    n, m = int(n), int(m)

    first_cards = sorted([int(i) for i in input().split(" ")])

    max_value = int()
    for idx, first in enumerate(first_cards):
        if first <= (m / 3):
            second_cards = first_cards[:idx] + first_cards[idx + 1:]

            for idx, second in enumerate(second_cards):
                if second <= (m - first / 2):
                    third_cards = second_cards[:idx] + second_cards[idx + 1:]

                    for third in reversed(third_cards):
                        if third <= m - first - second:
                            max_value = max(max_value, first + second + third)
                            print(first + second + third)
                            break

                else:
                    break
        else:
            break

    print(max_value)
