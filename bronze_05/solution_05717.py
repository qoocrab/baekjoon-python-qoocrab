# Time Complexity: O(N), where N is the number of test cases
# Space Complexity: O(1)
while True:
    m, f = map(int, input().split())

    if m == 0 and f == 0:
        break

    print(m + f)
