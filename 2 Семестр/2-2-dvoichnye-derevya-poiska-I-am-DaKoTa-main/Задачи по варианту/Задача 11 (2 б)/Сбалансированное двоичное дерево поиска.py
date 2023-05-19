from time import perf_counter
import tracemalloc

t_start = perf_counter()
tracemalloc.start()


# Класс узла дерева
class Node:
    def __init__(self, key):
        # Инициализируем поля узла
        self.key = key  # Значение узла
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок


# Класс бинарного дерева поиска
class BST:
    def __init__(self):
        self.root = None

    # Вставка значения в дерево
    def insert(self, key):
        # Если дерево пустое, создаем корень
        if self.root is None:
            self.root = Node(key)
        # Иначе находим место для вставки нового узла
        else:
            curr = self.root
            while True:
                # Если ключ уже есть в дереве, выходим
                if key == curr.key:
                    return
                elif key < curr.key:
                    # Если левый потомок отсутствует, создаем новый узел
                    if curr.left is None:
                        curr.left = Node(key)
                        return
                    else:
                        # Иначе переходим к левому потомку
                        curr = curr.left
                else:
                    # Если правый потомок отсутствует, создаем новый узел
                    if curr.right is None:
                        curr.right = Node(key)
                        return
                    # Иначе переходим к правому потомку
                    else:
                        curr = curr.right

    # Удаления значения из дерева
    def delete(self, key):
        # Нахождение минимального узла в дереве
        def find_min_node(node):
            while node.left is not None:
                node = node.left
            return node

        def delete_helper(node, key):
            if node is None:
                return node
            if key < node.key:
                node.left = delete_helper(node.left, key)
            elif key > node.key:
                node.right = delete_helper(node.right, key)
            else:
                # Если удаляемый узел является листовым узлом
                if node.left is None and node.right is None:
                    node = None
                # Если у удаляемого узла нет левого поддерева
                elif node.left is None:
                    node = node.right
                # Если у удаляемого узла нет правого поддерева
                elif node.right is None:
                    node = node.left
                # Если у удаляемого узла есть оба поддерева
                else:
                    # Находим минимальный узел в правом поддереве
                    min_node = find_min_node(node.right)
                    # Заменяем ключ удаляемого узла на ключ минимального узла
                    node.key = min_node.key
                    # Рекурсивно удаляем минимальный узел из правого поддерева
                    node.right = delete_helper(node.right, min_node.key)
            return node

        # Удаление значения с корневого узла
        self.root = delete_helper(self.root, key)

    # Поиск значения в дереве
    def exists(self, key):
        curr = self.root
        while curr is not None:
            # Если ключ найден, возвращаем True
            if key == curr.key:
                return True

            # Если ключ меньше текущего, идем налево
            elif key < curr.key:
                curr = curr.left

            # Иначе идем направо
            else:
                curr = curr.right

        # Если ключ не найден, возвращаем False
        return False

    def next(self, key):
        curr = self.root
        next_key = None
        while curr is not None:
            # Если ключ текущей ноды больше искомого
            if curr.key > key:
                # Если следующий ключ еще не найден, или найденный ключ больше текущего
                if next_key is None or curr.key < next_key:
                    # Запоминаем текущий ключ как следующий
                    next_key = curr.key
                # Идем налево
                curr = curr.left
            else:
                # Иначе идем направо
                curr = curr.right

        # Возвращаем следующий ключ или "none", если его нет
        return str(next_key) if next_key is not None else "none"

    def prev(self, key):
        curr = self.root
        prev_key = None
        while curr is not None:
            # Если ключ текущей ноды меньше искомого
            if curr.key < key:
                # Если предыдущий ключ еще не найден, или найденный ключ меньше текущего
                if prev_key is None or curr.key > prev_key:
                    # Запоминаем текущий ключ как предыдущий
                    prev_key = curr.key
                # Идем направо
                curr = curr.right
            else:
                # Иначе идем налево
                curr = curr.left

        # Возвращаем предыдущий ключ или "none", если его нет
        return str(prev_key) if prev_key is not None else "none"


bst = BST()
with open("input.txt", "r") as f:
    n = 0
    for line in f:
        n += 1
f.close()
with open("output.txt", "w+") as f_out, open('input.txt') as f:
    for i in range(n):
        line = f.readline().strip().split()
        # Обработка команды insert
        if line[0] == "insert":
            bst.insert(int(line[1]))
        # Обработка команды delete
        elif line[0] == "delete":
            bst.delete(int(line[1]))
        # Обработка команды exists
        elif line[0] == "exists":
            # Запись результата поиска в файл вывода
            f_out.write(str(bst.exists(int(line[1]))) + '\n')
        # Обработка команды next
        elif line[0] == "next":
            # Запись результата поиска следующего элемента в файл вывода
            f_out.write(str(bst.next(int(line[1]))) + '\n')
        # Обработка команды prev
        elif line[0] == "prev":
            # Запись результата поиска предыдущего элемента в файл вывода
            f_out.write(str(bst.prev(int(line[1]))) + '\n')
print("Время работы: %s секунд" % (perf_counter() - t_start))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
