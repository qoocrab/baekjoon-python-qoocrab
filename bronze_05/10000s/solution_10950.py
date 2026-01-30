# Time Complexity: O(N)
# Space Complexity: O(N)
import sys

data = sys.stdin.read().split()
t = int(data[0])
index = 1

for _ in range(t):
    a = int(data[index])
    b = int(data[index + 1])
    print(a + b)
    index += 2
