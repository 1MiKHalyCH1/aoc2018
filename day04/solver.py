from time import strptime
from operator import itemgetter
from collections import defaultdict
import re


date_pattern = re.compile(r'\[(.+)\] (.+)')
id_pattern = re.compile(r'Guard #(\d+) begins shift')
date_format = '%Y-%m-%d %H:%M'

def get_first_star(schedule):
    max_guard_id = max((sum(v.values()), k) for k,v in schedule.items())[1]
    max_guard_minute = max((v, k) for k,v in schedule[max_guard_id].items())[1]
    print("First star:", max_guard_id * max_guard_minute)

def get_second_star(schedule):
    max_guard_id = max_guard_minute = max_minutes = 0

    for guard_id, guard_schedule in schedule.items():
        minutes, guard_minute = max((v, k) for k,v in guard_schedule.items())
        if minutes > max_minutes:
            max_guard_id = guard_id
            max_guard_minute = guard_minute
            max_minutes = minutes

    print("Second star:", max_guard_id * max_guard_minute)

def get_schedule(data):
    res = dict()
    for x in data:
        k, v = date_pattern.search(x).groups()
        res[strptime(k, date_format)] = v
    
    data = [(k, v) for k,v in sorted(res.items(), key=itemgetter(0))]

    schedule = defaultdict(dict)
    start = finish = None
    guard_id = None
    for k, v in data:
        if '#' in v:
            guard_id = int(id_pattern.search(v).group(1))
        elif v == 'falls asleep':
            start = k.tm_min
        elif v == 'wakes up':
            finish = k.tm_min
            guard_shedule = schedule[guard_id]
            for i in range(start, finish):
                guard_shedule[i] = guard_shedule.get(i, 0) + 1

    return schedule

if __name__ == "__main__":
    with open('data.txt') as f:
        data = f.read().split('\n')
    
    schedule = get_schedule(data)
    get_first_star(schedule)
    get_second_star(schedule)