# Bag of Tokens
# https://leetcode.com/problems/bag-of-tokens/description/?envType=daily-question&envId=2024-03-04

def bag_of_token_score(tokens: list[int], power: int) -> int:
    low = 0
    high = len(tokens) - 1
    score = 0

    tokens = sorted(tokens)

    while low <= high:
        if power >= tokens[low]:
            score += 1
            power -= tokens[low]
            low += 1

        elif low < high and score > 0:
            score -= 1
            power += tokens[high]
            high -= 1

        else:
            return score

    return score
