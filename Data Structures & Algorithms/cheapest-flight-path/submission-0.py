import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf') for _ in range(n)]
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices.copy()
            for s,d,cost in flights:
                if prices[s] == float('inf'): continue
                newprice = cost + prices[s]
                print(cost, prices[s])
                if newprice < temp[d]:
                    temp[d] = newprice
            prices = temp
        
        print(prices)
        
        return prices[dst] if prices[dst] != float('inf') else -1