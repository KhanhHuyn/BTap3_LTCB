
def perm_with_repetition(s, r):
    result = []

    def backtrack(path):
        if len(path) == r:
            result.append(''.join(path))
            return
        for c in s:
            path.append(c)
            backtrack(path)
            path.pop()

    backtrack([])
    return result


s = input("Enter the string: ")
r = int(input("Enter the repetition number: "))

res = perm_with_repetition(s, r)
print(res)
