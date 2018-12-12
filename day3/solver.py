import re

SIZE = 1000
claim_pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')


class Fabric:
    def __init__(self):
        self.area = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

    def claim(self, x, y, width, height):
        for i in range(width):
            for j in range(height):
                self.area[x+i][y+j] += 1
    
    def count_overlaps(self):
        res = 0
        for x in range(SIZE):
            for y in range(SIZE):
                if self.area[x][y] >= 2:
                    res += 1
        return res

    def check_overlap(self, x, y, width, height):
        for i in range(width):
            for j in range(height):
                if self.area[x+i][y+j] != 1:
                    return True
        return False


def get_first_star(data, fabric):
    for claim in data:
        res = claim_pattern.search(claim)
        id, x, y, width, size = map(int, res.groups())
        fabric.claim(x, y, width, size)
        
    print("First star:", fabric.count_overlaps())

def get_second_star(data, fabric):
    for claim in data:
        res = claim_pattern.search(claim)
        id, x, y, width, size = map(int, res.groups())
        if not fabric.check_overlap(x, y, width, size):
            print("Second star:", id)
            return

if __name__ == "__main__":
    with open('data.txt') as f:
        data = f.read().split('\n')

    fabric = Fabric()

    get_first_star(data, fabric)
    get_second_star(data, fabric)