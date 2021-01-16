class Solution:
    def numWaterBottles(self, bottles: int, exchange: int) -> int:
        res = bottles # always drink the bottles
        while bottles >= exchange: # while we have enough bottles to exchange
            drank, new_bottles = divmod(bottles, exchange)
            res += drank
            bottles = new_bottles + drank
        return res
​
