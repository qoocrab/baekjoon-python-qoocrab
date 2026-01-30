# Time Complexity: O(N)
# Space Complexity: O(N)
import sys

data = sys.stdin.read().split()

for i in range(0, len(data), 2):
    a = int(data[i])
    b = int(data[i+1])
    print(a + b)
