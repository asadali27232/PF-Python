def is_palindrome(alist):
    palin = alist[::-1]

    for i in range(len(alist)):
        if alist[i] != palin[i]:
            return False

    return True


print(is_palindrome([1, 2, 3, 2, 1]))
print(is_palindrome([1, 2, 3, 2, 3]))
