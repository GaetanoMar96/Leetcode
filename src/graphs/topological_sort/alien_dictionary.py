from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        indegree = {}
        adj = defaultdict(list)
        #collect all keys
        chars = set(''.join(words))
        for c in chars:
            indegree[c] = 0
        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            #compare each char and see which comes first
            l1, l2 = 0, 0
            found_diff = False
            while l1 < len(word1) and l2 < len(word2):
                if word1[l1] != word2[l2]:
                    adj[word1[l1]].append(word2[l2])
                    indegree[word2[l2]] += 1
                    found_diff = True
                    break
                l1, l2 = l1 + 1, l2 + 1
            if not found_diff and len(word1) > len(word2):
            # Invalid case: a longer word comes before a shorter word
                return ""

        q = deque()
        for key in indegree:
            if indegree[key] == 0:
                q.append(key)
                
        order = ''
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                order += node
                if node in adj:
                    for char in adj[node]:
                        indegree[char] -= 1
                        if indegree[char] == 0:
                            q.append(char)
        if len(order) != len(indegree.keys()):
            return ''     
        return order