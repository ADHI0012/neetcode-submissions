class CountSquares:

    def __init__(self):
        self.hashMap = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.hashMap[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        x,y = point
        res = 0

        for a,b in self.points:
            if abs(x - a) == abs(y - b) and a != x and b != y:
                res += self.hashMap[(x,b)] * self.hashMap[(a,y)]
        return res