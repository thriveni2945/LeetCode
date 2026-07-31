class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        max_to_eat = len(candyType) // 2
    
        unique_candies = len(set(candyType))
        return min(max_to_eat, unique_candies)