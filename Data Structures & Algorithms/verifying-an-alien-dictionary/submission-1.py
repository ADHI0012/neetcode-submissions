class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashMap = {}
        for i in range(len(order)):
            hashMap[order[i]] = i
        
        word_index = 0

        while word_index + 1 <= len(words) - 1:
            m = len(words[word_index])
            n = len(words[word_index + 1])
            index_big = word_index
            index_small = word_index + 1

            if m < n:
                m,n = n,m
                index_big, index_small = index_small, index_big
            i = 0

            while True:
                if i > n - 1 and index_small > index_big:
                    return False
                if i > n - 1:
                    break

                r1 = hashMap[words[word_index][i]]
                r2 = hashMap[words[word_index + 1][i]]

                if r1 == r2:
                    i += 1
                    continue
                if r1 > r2:
                    return False
                break

            
            word_index += 1
            
        return True


