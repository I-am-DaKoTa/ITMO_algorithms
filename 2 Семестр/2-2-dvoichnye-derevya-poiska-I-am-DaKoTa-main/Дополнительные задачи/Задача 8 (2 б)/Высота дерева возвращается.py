from time import perf_counter
import tracemalloc

t_start = perf_counter()
tracemalloc.start()


# Класс узла дерева
class Node:
    def __init__(self, key):
        # Инициализируем поля узла
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок
        self.key = key  # Значение узла


# Вставка узла в дерево
def insert(root, key):
    # Если дерево пустое, создаем новый узел
    if root is None:
        return Node(key)
    else:
        # Если значение ключа больше значения текущего узла, переходим в правое поддерево
        if root.key < key:
            root.right = insert(root.right, key)
        # Если значение ключа меньше или равно значению текущего узла, переходим в левое поддерево
        else:
            root.left = insert(root.left, key)
    return root


# Нахождение высоты дерева
def height(root):
    # Если дерево пустое, высота равна 0
    if root is None:
        return 0
    else:
        # Рекурсивно находим высоту левого и правого поддеревьев
        left_height = height(root.left)
        right_height = height(root.right)
        # Возвращаем максимальное значение высоты и прибавляем 1, чтобы учесть текущий узел
        return max(left_height, right_height) + 1


root = None
with open("input.txt", "r") as f_in:
    n = int(f_in.readline())
    for i in range(n):
        key, left, right = map(int, f_in.readline().split())
        if i == 0:
            root = Node(key)
        else:
            insert(root, key)
with open("output.txt", "w+") as f_out:
    f_out.write(str(height(root)))
print("Время работы: %s секунд" % (perf_counter() - t_start))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
