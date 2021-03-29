import time
import random


def merge(li_1, li_2):
    """Merge two sorted arrays into a sorted one."""
    i = 0
    j = 0
    merged_list = list()
    for _ in range(len(li_1) + len(li_2)):
        if li_1[i] <= li_2[j]:
            merged_list.append(li_1[i])
            i += 1
        else:
            merged_list.append(li_2[j])
            j += 1
        
        if i == len(li_1):
            merged_list.extend(li_2[j:])
            break
        if j == len(li_2):
            merged_list.extend(li_1[i:])
            break
    return merged_list


def divide(li):
    """Divide an array into two half-lengthed arrays."""
    length = len(li)
    half_length = length // 2
    return li[:half_length], li[half_length:]


def merge_sort(li):
    """Sort an array."""
    if len(li) > 1:
        li_1, li_2 = divide(li)
        li_1_sorted = merge_sort(li_1)
        li_2_sorted = merge_sort(li_2)
        li_merged = merge(li_1_sorted, li_2_sorted)
        return li_merged
    else:
        return li


def benchmark(list_length):
    start_time = time.time()
    merge_sort([random.randint(1, list_length) for _ in range(list_length)])
    time_elapsed = time.time() - start_time
    print(f"List length: {list_length}, Time: {time_elapsed:.4f} secs.")


def test(li):
    sorted_li = merge_sort(li)
    prev_item = 0
    for item in sorted_li:
        if item < prev_item:
            return False
    return True


if __name__ == "__main__":

    for i in range(100):
        test_length = random.randint(1, 10000)
        test_list = [random.randint(1, 10000) for _ in range(test_length)]
        passed = test(test_list)
        if not passed:
            raise RuntimeError
    print("Passed test! Start benchmarking...\n")

    for i in range(20):
        benchmark(2**i)
