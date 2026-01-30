# Time Complexity: O(N), where N is the number of test cases.
# Space Complexity: O(1)
t = int(input())

for _ in range(t):
    word = input()
    print(word[0] + word[-1])
