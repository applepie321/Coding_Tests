# Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/?envType=daily-question&envId=2024-02-13


def first_palindrome(words: list[str]) -> str:
    for word in words:
        if word == word[::-1]:
            return word
    return ""
