class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                diff = price - min_price
                if diff > max_profit:
                    max_profit = diff
        return max_profit
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

                