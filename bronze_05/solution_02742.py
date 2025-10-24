# Time Complexity: O(N)
# Space Complexity: O(N)
import sys

n = int(sys.stdin.readline())

sys.stdout.write("\n".join(map(str, range(n, 0, -1))) + "\n")
