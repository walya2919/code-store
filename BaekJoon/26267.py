import sys

diction = dict()
N = int(sys.stdin.readline())
for _ in range(N):
    X, T, C = map(int, sys.stdin.readline().split())
    try:
        diction[T-X] += C
    except:
        diction[T-X] = C

print(max(diction.values()))