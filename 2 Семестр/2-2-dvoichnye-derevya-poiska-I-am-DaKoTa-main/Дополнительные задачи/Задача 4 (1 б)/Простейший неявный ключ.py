from time import perf_counter
import tracemalloc

t_start = perf_counter()
tracemalloc.start()


# Класс узла дерева
class Node:
    def __init__(self, key):
        # Инициализируем поля узла
        self.key = key  # Значение узла
        self.size = 1  # Размер поддерева
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок


# Класс неявного двоичного дерева поиска
class ImplicitBST:
    def __init__(self):
        # Инициализируем пустым корнем
        self.root = None

    # Размер поддерева
    def size(self, node):
        if node is None:
            return 0
        return node.size

    # Обновление размера поддерева
    def update_size(self, node):
        node.size = self.size(node.left) + self.size(node.right) + 1

    # Вставка нового узла в дерево
    def insert(self, key):
        def _insert(node, key):
            # Если дерево пустое, то создать узел с заданным ключом
            if node is None:
                return Node(key)

            # Если узел с заданным ключом уже существует, то ничего не делать
            if key == node.key:
                return node

            # Если ключ меньше, то добавить в левое поддерево
            if key < node.key:
                node.left = _insert(node.left, key)

            # Если ключ больше, то добавить в правое поддерево
            else:
                node.right = _insert(node.right, key)

            # Обновление размера поддерева
            self.update_size(node)
            return node

        self.root = _insert(self.root, key)

    # Получение k-го элемента по возрастанию в дереве
    def kth_smallest(self, k):
        def _kth_smallest(node, k):
            # Если дерево пустое, то вернуть None
            if node is None:
                return None
            left_size = self.size(node.left)

            # Если размер левого поддерева равен k-1, то вернуть ключ текущего узла
            if left_size == k - 1:
                return node.key

            # Если размер левого поддерева больше или равен k, то искать k-й элемент в левом поддереве
            if left_size >= k:
                return _kth_smallest(node.left, k)

            # Иначе искать (k-left_size-1)-й элемент в правом поддереве
            else:
                return _kth_smallest(node.right, k - left_size - 1)

        return _kth_smallest(self.root, k)


# Создание экземпляра неявного двоичного дерева поиска
bst = ImplicitBST()
with open('input.txt') as f_in, open('output.txt', 'w') as f_out:
    for line in f_in:
        op, val = line.split()  # Запрос
        if op == '+':
            bst.insert(int(val))
        elif op == '?':
            k = int(val)
            f_out.write(str(bst.kth_smallest(k)) + '\n')
print("Время работы: %s секунд" % (perf_counter() - t_start))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
