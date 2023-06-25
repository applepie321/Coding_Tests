# 1575. Count All Possible Routes
# https://leetcode.com/problems/count-all-possible-routes/description/

class Solution:
    MOD = 1000000007

    def helper(self, locations, city, finish, remainFuel, memo):
        if remainFuel < 0:
            return 0
        
        if memo[city][remainFuel] is not None:
            return memo[city][remainFuel]
        
        total = 1 if city == finish else 0
        
        for nextCity in range(len(locations)):
            if nextCity != city and remainFuel >= abs(locations[nextCity] - locations[city]):
                total = (total + self.helper(locations, nextCity, finish, remainFuel - abs(locations[nextCity] - locations[city]), memo)) % self.MOD
        
        memo[city][remainFuel] = total
        return total

    def countRoutes(self, locations, start, finish, fuel):
        n = len(locations)
        memo = [[None] * (fuel + 1) for _ in range(n)]
        return self.helper(locations, start, finish, fuel, memo)
    




# Source
# https://leetcode.com/problems/count-all-possible-routes/solutions/3678974/beats-100-memo-tabulation-c-java-python-beginner-friendly/

# The helper function is a recursive function that performs the main computation for counting all possible routes. It takes the following parameters: locations (vector of city locations), city (current city index), finish (index of the finish city), remainFuel (remaining fuel), and memo (memoization table).
# The function begins by checking if the remaining fuel (remainFuel) is negative. If so, it means that the current path is not feasible due to insufficient fuel, and the function returns 0.
# Next, the function checks if the result for the current city and remainFuel combination is already present in the memo table. If so, it retrieves and returns the stored result, avoiding redundant computations.
# If the result is not available in the memo table, the function proceeds to compute it.
# The function initializes the total variable as 1 if the current city is the same as the finish city, indicating that a valid route has been found. Otherwise, total is initialized as 0.
# The function then iterates over all possible nextCity indices, representing the cities that can be visited from the current city. It skips the current city itself.
# For each nextCity, the function checks if there is enough fuel (remainFuel) to travel from the current city to the nextCity. If so, it recursively calls the helper function for the nextCity with the updated remainFuel (subtracting the fuel consumed for the current move) and adds the returned result to the total value.
# Before adding the result to total, the function takes modulo MOD to keep the result within the specified range (1000000007).
# Once all possible nextCity options have been explored, the function stores the computed total result in the memo table for the current city and remainFuel combination. This is done to avoid redundant computations in future recursive calls.
# Finally, the function returns the computed total result.