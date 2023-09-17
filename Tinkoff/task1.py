# n = int(input())
# s = int(input())


n, s = map(int, input().split())
max = 0

rev = []
for i in input().split():
    rev.append(int(i))

for i in range(n):
    if rev[i] <= s:
        if rev[i] > max:
            max = rev[i]

print(max)
