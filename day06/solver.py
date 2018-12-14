from string import ascii_uppercase
from itertools import product

def manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def get_all_distances(p, points):
    return {name:manhattan_distance(p, point) for name, point in points.items()}

def get_nearest(p, points):
    first, second = sorted(((v,k) for k,v in get_all_distances(p, points).items()))[:2]
    if first[0] < second[0]:
        return first[1]

class Grid:
    def __init__(self, points):
        self.points = dict(zip(map(''.join, product(ascii_uppercase, repeat=2)), points))
        self.height = max(y for x,y in points)
        self.width = max(x for x,y in points)
        self.count = {k:1 for k in self.points}
        
        
        self.grid = [['.' for _ in range(self.width+1)] for _ in range(self.height+1)]
        for k, (x, y) in self.points.items():
            self.grid[y][x] = k

    def draw_grid(self):
        self.infinity_points = set()

        for x in range(self.width+1):
            for y in range(self.height+1):
                if self.grid[y][x] == '.':
                    nearest = get_nearest((x,y), self.points)
                    if nearest:
                        self.count[nearest] += 1
                        if x in (0, self.width) or y in (0, self.height):
                            self.infinity_points.add(nearest)
                        self.grid[y][x] = nearest

    def count_region(self):
        res = 0
        for x in range(self.width+1):
            for y in range(self.height+1):
                distances = get_all_distances((x,y), self.points)
                if sum(distances.values()) < 10000:
                    res += 1
        return res

    def get_counts(self):
        return {k:v for k,v in self.count.items() if k not in self.infinity_points}
    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)

def get_first_star(grid):
    res = sorted(((v, k) for k,v in grid.get_counts().items()), reverse=True)[0][0]
    print("First star:", res)

def get_second_star(grid):
    res = grid.count_region()
    print("Second star:", res)

if __name__ == "__main__":
    with open('data.txt') as f:
        points = [tuple(map(int, x.split(', '))) for x in f.read().split('\n')]

    grid = Grid(points)
    grid.draw_grid()
    # print(grid)
    get_first_star(grid)
    get_second_star(grid)