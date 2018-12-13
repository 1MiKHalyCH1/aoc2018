from collections import Counter

class TaskStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            return
        
        last_elem = self.stack[-1]
        if last_elem.lower() == x.lower() and x.islower() ^ last_elem.islower():
            self.stack.pop()
        else:
            self.stack.append(x)

    def react(self, s):
        for x in s:
            self.push(x)

    def __str__(self):
        return ''.join(self.stack)

    def __len__(self):
        return len(self.stack)

def get_first_star(data):
    stack = TaskStack()
    stack.react(data)
    print("First star:", len(stack))


def get_second_star(data):
    min_len = len(data)

    for c in set(data.lower()):
        stack = TaskStack()
        stack.react(data[:].replace(c, '').replace(c.upper(), ''))
        if len(stack) < min_len:
            min_len = len(stack)

    print("Second star:", min_len)

if __name__ == "__main__":
    with open('data.txt') as f:
        data = f.read()

    get_first_star(data)
    get_second_star(data)