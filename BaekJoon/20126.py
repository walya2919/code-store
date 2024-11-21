import sys

# N: 시험의 갯수
# M: 시험 시간
# S: 강의실 이용가능 시간
N, M, S = map(int, sys.stdin.readline().split())
time_li = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    time_li.append([x,y])

time_li.sort(key=lambda x : x[0])

if M <= time_li[0][0]:
    print("0")
    exit(0)

for index in range(N-1):
    if M <= time_li[index+1][0] - sum(time_li[index]):
        print(sum(time_li[index]))
        exit(0)

if M <= S - sum(time_li[-1]):
    print(sum(time_li[-1]))
    exit(0)

print("-1")