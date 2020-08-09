"""
Source: https://www.acmicpc.net/problem/1182
Time: 536ms
Rank: .
"""

if __name__ == "__main__":
    n, s = input().split(" ")
    n, s = int(n), int(s)
    sequence = [int(i) for i in input().split(" ")]
    count = 0

    def find_subseq(seq, s):
        global count
        for idx, el in enumerate(seq):
            if s == el:
                count += 1
            if len(seq) > 1:
                find_subseq(seq[idx + 1:], s - el)
    
    find_subseq(sequence, s)
    
    print(count)
