# Time Complexity: O(N)
# Space Complexity: O(1)
import sys

for line in sys.stdin:
    a, b = map(int, line.split())

    if a == 0 and b == 0:
        break

    print("Yes" if a > b else "No")
