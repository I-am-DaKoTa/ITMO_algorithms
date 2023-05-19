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
        self.size = 1  # Размер поддерева с корнем в текущем узле


# Класс бинарного дерева поиска
class BST:
    def __init__(self):
        # Инициализируем пустым корнем
        self.root = None

    def _insert(self, node, key):
        # Если достигли конца дерева, создаем новый узел и возвращаем его
        if node is None:
            return Node(key)

        # Если значение меньше текущего узла, рекурсивно добавляем новый узел в левое поддерево
        if key < node.key:
            node.left = self._insert(node.left, key)

        # Если значение больше текущего узла, рекурсивно добавляем новый узел в правое поддерево
        elif key > node.key:
            node.right = self._insert(node.right, key)

        # Обновляем размер поддерева с корнем в текущем узле
        node.size = 1 + self.size(node.left) + self.size(node.right)
        return node

    # Добавление узлов в дерево
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Определение размера дерева
    def size(self, node):
        return node.size if node else 0

    def _find_min_greater_than(self, node, key):
        # Если достигли конца дерева, возвращаем 0
        if node is None:
            return 0

        # Если текущий узел имеет значение меньше или равно заданному, рекурсивно идем вправо, а иначе влево
        if node.key <= key:
            return self._find_min_greater_than(node.right, key)
        else:
            # Если в левом поддереве есть хотя бы (key - 1) элементов, рекурсивно идем влево
            if node.left and node.left.size >= key - 1:
                return self._find_min_greater_than(node.left, key)
            return node.key

    # Поиск узла с наименьшим значением, большим заданного ключа
    def find_min_greater_than(self, key):
        return self._find_min_greater_than(self.root, key)


bst = BST()
with open('input.txt') as f_in, open('output.txt', 'w') as f_out:
    for line in f_in:
        cmd, arg = line.split()  # Запрос
        if cmd == '+':
            bst.insert(int(arg))
        elif cmd == '>':
            f_out.write(str(bst.find_min_greater_than(int(arg))) + '\n')
print("Время работы: %s секунд" % (perf_counter() - t_start))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
