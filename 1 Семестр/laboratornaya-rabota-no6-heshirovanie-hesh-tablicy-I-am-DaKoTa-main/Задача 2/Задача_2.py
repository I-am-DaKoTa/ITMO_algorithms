def add(number, name):
    book[number] = name


def delete(number):
    try:
        return book.pop(number)

    except KeyError:
        return None


def find(number):
    if book.get(number) is not None:
        return book.get(number)
    else:
        return "not found"


with open('input.txt', 'r') as f:
    n = int(f.readline())
    commands = f.read().splitlines()
    book = {}
if 1 <= n <= 10 ** 5:
    for command in commands:
        cmd = command.split(' ')[0]
        number = int(command.split(' ')[1])
        if cmd == "add":
            name = command.split(' ')[2]
            add(number, name)

        elif cmd == "del":
            delete(number)

        else:
            with open('output.txt', 'a') as f:
                f.write(find(number) + '\n')
