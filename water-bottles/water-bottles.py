class Solution:
    def numWaterBottles(self, bottles: int, exchange: int) -> int:
        res = bottles
        while bottles >= exchange: # While there is more bottles or enough bottles to exchange
            newbottles, empty = bottles = bottles // exchange, bottles - (exchange * (bottles // exchange)) # Divmod
            res += newbottles # Add the bottles we drank
            bottles = newbottles + empty # Do it again for the new amount of bottles.
        return res
​
