# Maximize Happiness of Selected Children
# https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2024-05-09

def maximum_happiness_sum(happiness: list[int], k: int) -> int:
    happiness.sort(reversed=True)
    total_score, turns = 0, 0

    for i in range(k):
        total_score += max(happiness[i] - turns, 0)
        turns += 1
    
    return total_score