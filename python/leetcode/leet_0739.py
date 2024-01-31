# Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/?envType=daily-question&envId=2024-01-31


def dailyTemperatures(self, temperatures):
    answer = []
    result = [0] * len(temperatures)
    for i in range(len(temperatures)):
        while answer and temperatures[i] > temperatures[answer[-1]]:
            prev_index = answer.pop()
            result[prev_index] = i - prev_index
        answer.append(i)
    return result
