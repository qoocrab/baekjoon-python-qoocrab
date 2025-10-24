# Time Complexity: O(N)
# Space Complexity: O(N)
import sys

n = int(sys.stdin.readline())

sys.stdout.write("\n".join(f"Hello World, Judge {i}!" for i in range(1, n + 1)) + "\n")