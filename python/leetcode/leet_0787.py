# Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/?envType=daily-question&envId=2024-02-23
import math


def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    distances = [math.inf] * n
    distances[src] = 0
    for _ in range(k + 1):
        temp = list(distances)
        for flight in flights:
            u, v, price = flight
            if distances[u] != math.inf and temp[v] > distances[u] + price:
                temp[v] = distances[u] + price
        distances = temp
    return distances[dst] if distances[dst] != math.inf else -1
