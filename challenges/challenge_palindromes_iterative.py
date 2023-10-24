def is_palindrome_iterative(word):
    if not word:
        return False

    n = len(word)

    for index in range(n):
        if word[index] != word[n - index - 1]:
            return False

    return True
