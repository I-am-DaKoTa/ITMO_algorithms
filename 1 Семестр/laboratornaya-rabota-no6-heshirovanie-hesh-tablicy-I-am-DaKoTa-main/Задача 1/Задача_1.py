def add(num):
    if not (num in set):
        set.append(num)
    else:
        pass


def remove(num):
    if num in set:
        set.remove(num)
    else:
        pass


def contains(num):
    if num in set:
        with open('output.txt', 'a') as f:
            f.write("Y" + "\n")
    else:
        with open('output.txt', 'a') as f:
            f.write("N" + "\n")


with open('input.txt', 'r') as f:
    n = int(f.readline())
    commands = f.read().splitlines()
    set = []
    if 1 <= n <= 5 * 10 ** 5:
        for command in commands:
            cmd = command.split(' ')[0]
            num = int(command.split(' ')[1])
            if abs(num) <= 10 ** 18:
                if cmd == "A":
                    add(num)

                elif cmd == "D":
                    remove(num)

                else:
                    contains(num)
            else:
                with open('output.txt', 'w') as f:
                    f.write("ERROR")
                break
