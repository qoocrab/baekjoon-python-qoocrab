# Time Complexity: O(N)
# Space Complexity: O(1)
import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())

for i in range(1, n + 1):
    write(f"{i}\n")
