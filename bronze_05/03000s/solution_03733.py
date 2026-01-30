# Time Complexity: O(L), where L is the number of input lines
# Space Complexity: O(1)
import sys

for line in sys.stdin:
    n, s = map(int, line.split())
    print(s // (n + 1))
