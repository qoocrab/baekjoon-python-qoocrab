# Time Complexity: O(1)
# Space Complexity: O(1)
expected = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))
print(" ".join(str(e - f) for e, f in zip(expected, found)))
