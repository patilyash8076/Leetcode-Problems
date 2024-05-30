class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')  # Initialize min_price to infinity
        max_profit = 0  # Initialize max_profit to zero

        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price encountered
            else:
                profit = price - min_price  # Calculate profit if sold today
                if profit > max_profit:
                    max_profit = profit  # Update the max_profit if the current profit is higher

        return max_profit

                