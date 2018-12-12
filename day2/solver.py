from collections import Counter
from Levenshtein import distance

def get_first_star(data):
    count_2 = count_3 = 0

    for s in data:
        c = Counter(s)
        if len({k for k,v in c.items() if v == 2}):
            count_2 += 1
        if len({k for k,v in c.items() if v == 3}):
            count_3 += 1
    print("First star:", count_2*count_3)
    return

def get_second_star(data):
    for x in data:
        for y in data:
            if distance(x,y) == 1:
                print("Second star:", "".join(a for a,b in zip(x,y) if a == b))
                return


if __name__ == "__main__":
    with open('data.txt') as f:
        data = f.read().split()

    get_first_star(data)
    get_second_star(data)