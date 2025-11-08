# # recursive

# refer: https://leetcode.com/problems/predict-the-winner/solutions/3826359/concise-min-max-algorithm-with-memoization-in-python-faster-than-95/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def play(l, r, turn):
            if l > r:
                return 0
            if turn == 0:
                return max(play(l+1, r, 1-turn) + nums[l], play(l, r-1, 1-turn) + nums[r])
            else:
                return min(play(l+1, r, 1-turn) - nums[l], play(l, r-1, 1-turn) - nums[r])
        return play(0, len(nums)-1, 0) >= 0


# update: top down dp with cache
# at each round, the goal is to maximize the score of the current player
# the maximize score equals to the score we can get from the current round plus what is remaining for us after next round
# since the total number of stones is fixed, what is remaining for us after next round equals to total number of stones minus the maximize the score the other player can get at next round
# add prefix sum to tackle negative number of stones

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        prefix = [0]
        tmp = 0
        for i in nums:
            tmp += i
            prefix.append(tmp)
        
        @cache
        def score(i, j):
            if i == j:
                return prefix[i+1] - prefix[i]
            next_overall_score_1 = prefix[j+1] - prefix[i+1]
            next_best_score_1 = score(i+1, j)
            score_from_next_round_1 = next_overall_score_1 - next_best_score_1
            next_overall_score_2 = prefix[j] - prefix[i]
            next_best_score_2 = score(i, j-1)
            score_from_next_round_2 = next_overall_score_2 - next_best_score_2
            return max(nums[i] + score_from_next_round_1, nums[j] + score_from_next_round_2)
        max_score = score(0, len(nums)-1)
        if max_score*2 >= prefix[-1]:
            return True
        else:
            return False