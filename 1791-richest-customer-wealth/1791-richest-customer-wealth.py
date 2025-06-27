class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum = 0
        wealth = []
        # iterate through accounts
        for array in accounts:
            for item in array:
                sum = sum + item
            # store sum into new array, and reset sum for next array
            wealth.append(sum)
            sum = 0
        # iterate though wealth and return the largest number
        max = 0
        for number in wealth:
            if max < number:
                max = number
        return max