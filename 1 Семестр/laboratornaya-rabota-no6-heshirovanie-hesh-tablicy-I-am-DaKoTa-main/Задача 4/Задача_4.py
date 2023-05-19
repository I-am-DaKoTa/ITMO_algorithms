def put(key, data):
    a[key] = data


def get(key):
    if a.get(key) is not None:
        return a.get(key)
    else:
        return "<none>"


def delete(number):
    try:
        return a.pop(number)
    except KeyError:
        return None


def prev(key):
    keys = list(a.keys())
    for k in keys:
        if k == key:
            if keys.index(k) != 0:
                prev = keys[keys.index(k) - 1]
                return a.get(prev)
            else:
                return "<none>"


def next(key):
    keys = list(a.keys())
    for k in keys:
        if k == key:
            if keys.index(k) != (len(keys) - 1):
                next = keys[keys.index(k) + 1]
                return a.get(next)
            else:
                return "<none>"


with open('input.txt', 'r') as f:
    n = int(f.readline())
    commands = f.read().splitlines()
    a = {}
for command in commands:
    cmd = command.split(' ')[0]
    key = command.split(' ')[1]
    if cmd == "put":
        data = command.split(' ')[2]
        put(key, data)

    elif cmd == "delete":
        delete(key)

    elif cmd == "get":
        with open('output.txt', 'a') as f:
            f.write(get(key) + '\n')

    elif cmd == "prev":
        with open('output.txt', 'a') as f:
            f.write(prev(key) + '\n')

    else:
        with open('output.txt', 'a') as f:
            f.write(next(key) + '\n')
