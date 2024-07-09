# 1701. Average Waiting Time
# https://leetcode.com/problems/average-waiting-time/?envType=daily-question&envId=2024-07-09

# Source
# Leetcode Editorial

def average_waiting_time(customers: list[list[int]]) -> float:
    next_wait_time = 0
    total_wait_time = 0

    for customer in customers:
        next_wait_time = max(customer[0], next_wait_time) + customer[1]
        total_wait_time += next_wait_time - customer[0]

    average_waiting_time = total_wait_time / len(customer)
    return average_waiting_time