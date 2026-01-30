# Time Complexity: O(N), where N is the number of test cases.
# Space Complexity: O(1)
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    print(x + y)
