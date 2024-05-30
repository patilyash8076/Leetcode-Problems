class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # O(n) solution 
        min_price = prices[0]   # assign any number I can also assign infiniy here
        max_profit = 0
        for price in prices:
            if price < min_price:   # checks if price is less than min_price
                min_price = price   # if it is then assigning min_price with current_price
            else:
                diff = price - min_price    # if not then difference is calculates between current_price and min_price 
                if diff > max_profit:       # if diff is greater than max_profit then diff is assign to max_profit
                    max_profit = diff
        return max_profit

        # O(n**2) Solution

        # max_profit = 0
        # for i in range(len(prices)-1):          #[7 1 5 3 6]
        #     for j in range(i+1, len(prices)):   #[1 5 3 6 4]
        #         if prices[i] > prices[j]:
        #             break
        #         else:
        #           diff = abs(prices[i] - prices[j])
        #           if diff > max_profit:
        #             max_profit = diff
        # return max_profit

                