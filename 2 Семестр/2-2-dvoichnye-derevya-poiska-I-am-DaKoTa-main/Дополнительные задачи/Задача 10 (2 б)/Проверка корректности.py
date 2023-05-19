from time import perf_counter
import tracemalloc

t_start = perf_counter()
tracemalloc.start()


# Проверка, является ли данное дерево двоичным деревом поиска
def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    # Если узел не существует, значит дерево пустое и является двоичным деревом поиска
    if node is None:
        return True
    # Если значение узла находится вне заданных пределов, значит дерево не является двоичным деревом поиска
    if node.value < min_val or node.value > max_val:
        return False
    # Рекурсивно проверяем левое и правое поддеревья на то, являются ли они двоичными деревьями поиска
    # Для левого поддерева значение верхней границы изменяется на (node.value - 1),
    # а для правого поддерева - на (node.value + 1)
    return is_bst(node.left, min_val, node.value - 1) and is_bst(node.right, node.value + 1, max_val)


# Класс узла двоичного дерева
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value  # Значение узла
        self.left = left  # Левый потомок
        self.right = right  # Правый потомок


with open("input.txt", "r") as f_in:
    n = int(f_in.readline())
    # Список узлов
    nodes = [Node() for i in range(n)]
    for i in range(n):
        value, left, right = map(int, f_in.readline().split())
        nodes[i].value = value
        if left != 0:
            nodes[i].left = nodes[left - 1]
        if right != 0:
            nodes[i].right = nodes[right - 1]
with open("output.txt", "w+") as f_out:
    # Если дерево пустое, то оно является двоичным деревом поиска
    if n == 0:
        f_out.write('YES')
    # Если дерево не пустое, проверяем, является ли оно двоичным деревом поиска
    else:
        if is_bst(nodes[0]):
            f_out.write('YES')
        else:
            f_out.write('NO')
print("Время работы: %s секунд" % (perf_counter() - t_start))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
