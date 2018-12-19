def parse(data):
    children, metas, data = *data[:2], data[2:]
    child_meta = []
    values = []

    for _ in range(children):
        score, value, data = parse(data)
        child_meta.append(score)
        values.append(value)

    score, meta = sum(data[:metas]), data[metas:]

    if not children: return score, score, meta
    return score + sum(child_meta), sum(values[i - 1] for i in data[:metas] if 1 <= i <= len(values)), meta

def get_first_star(data):
    print('First star:', parse(data)[0])

def get_second_star(data):
    print('Second star:', parse(data)[1])

if __name__ == "__main__":
    with open('data.txt', 'r') as f:
        data = list(map(int, f.read().split()))

    get_first_star(data)
    get_second_star(data)