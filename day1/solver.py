from itertools import cycle

def get_first_star(data):
    res = eval('0' + ''.join(data))
    print("First star:", res)

def get_second_star(data):
    results = {0}
    res = 0

    for x in cycle(data):
        res = eval(str(res) + x)
        if res in results:
            print("Second star:", res)
            return
        else:
            results.add(res)

if __name__ == "__main__":
    with open('data.txt') as f:
        data = f.read().split()
    
    get_first_star(data)
    get_second_star(data)