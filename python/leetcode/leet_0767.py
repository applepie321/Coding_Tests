# Reorganize string
# https://leetcode.com/problems/reorganize-string/



# Given a string s, rearrange the characters of s 
# so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.


# Not work
# class Solution:
#     def reorganizeString(self, s: str) -> str:
#         for n in range(len(s)-2):
#             if s[n] == s[n+1] and s[n+1] == s[n+2]:
#                 return ""
#             elif s[n] == s[n+1] and s[n+1] != s[n+2]:
#                 temp = s[n+1]
#                 s.replace(s[n+1], s[n+2])
#                 s.replace(s[n+2], temp)
#                 return s










from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        # 문자의 빈도수를 세고 내림차순으로 정렬합니다.
        counts = Counter(s)
        counts = sorted(counts.items(), key=lambda x: -x[1])
        # 가장 많이 나오는 문자의 개수가 (문자열 길이 + 1) // 2 보다 크면 불가능합니다.
        if counts[0][1] > (len(s) + 1) // 2:
            return ""
        # 결과를 저장할 리스트를 만듭니다.
        result = [""] * len(s)
        # 홀수 인덱스와 짝수 인덱스를 따로 관리합니다.
        odd = 0
        even = 1
        # 각 문자에 대해서
        for char, count in counts:
            # 홀수 인덱스에 먼저 넣습니다.
            for _ in range(count):
                result[odd] = char
                odd += 2
                # 홀수 인덱스가 범위를 벗어나면 짝수 인덱스로 돌아갑니다.
                if odd >= len(s):
                    odd = 1
        # 리스트를 문자열로 변환하여 리턴합니다.
        return "".join(result)