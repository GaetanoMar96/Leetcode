class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        user = {}
        user['alice'] = 0
        user['bob'] = 0
        def dp(i, curruser, stones):
            if stones == len(piles): # end stones
                return user['alice'] > user['bob']
            
            user[curruser] += piles[i]
            if curruser == 'alice':
                curruser = 'bob'
            else:
                curruser = 'alice'
            
            return dp(i+1, curruser, stones + 1) or dp(i - 1, curruser, stones + 1)
            
        return dp(0, 'alice', 1) or dp(len(piles) - 1, 'alice', 1)