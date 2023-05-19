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
        # Инициализируем пустым корнем
        self.root = None

    # Вставка узла в дерево
    def insert(self, key):
        # Проверяем, если дерево пустое, то создаем корневой узел
        if self.root is None:
            self.root = Node(key)
        else:
            curr = self.root
            # Идем по дереву вниз, пока не найдем подходящее место для вставки нового узла
            while True:
                # Если ключ уже есть в дереве, то вставка не производится
                if key == curr.key:
                    return

                # Если новый ключ меньше текущего, то идем налево
                elif key < curr.key:
                    # Если левая ветвь пуста, создаем новый узел там
                    if curr.left is None:
                        curr.left = Node(key)
                        return
                    # Иначе продолжаем идти по левой ветви
                    else:
                        curr = curr.left

                # Если новый ключ больше текущего, то идем направо
                else:
                    # Если правая ветвь пуста, создаем новый узел там
                    if curr.right is None:
                        curr.right = Node(key)
                        return
                    # Иначе продолжаем идти по правой ветви
                    else:
                        curr = curr.right

    # Удаление узла из дерева
    def delete(self, key):
        def find_min_node(node):
            while node.left is not None:
                node = node.left
            return node

        def delete_helper(node, key):
            # Если узел не найден, возвращаем его
            if node is None:
                return node
            # Если ключ меньше значения узла, рекурсивно ищем его в левом поддереве
            if key < node.key:
                node.left = delete_helper(node.left, key)

            # Если ключ больше значения узла, рекурсивно ищем его в правом поддереве
            elif key > node.key:
                node.right = delete_helper(node.right, key)

            else:
                # Если у узла нет потомков, просто удаляем его
                if node.left is None and node.right is None:
                    node = None

                # Если у узла есть только один потомок, просто заменяем его на этого потомока
                elif node.left is None:
                    node = node.right
                elif node.right is None:
                    node = node.left

                # Если у узла есть два потомка
                else:
                    # Находим узел с минимальным значением в правом поддереве
                    min_node = find_min_node(node.right)
                    # Заменяем удаляемый узел на узел с минимальным значением
                    node.key = min_node.key
                    # Рекурсивно удаляем узел с минимальным значением из правого поддерева
                    node.right = delete_helper(node.right, min_node.key)
            return node

        # Вызываем вспомогательную функцию для удаления узла
        self.root = delete_helper(self.root, key)

    # Проверка наличия узла в дереве
    def exists(self, key):
        curr = self.root
        # Продолжаем обход дерева, пока не дойдем до конца или не найдем узел с искомым ключом
        while curr is not None:
            # Если ключ текущего узла равен искомому, возвращаем True
            if key == curr.key:
                return True
            # Если искомый ключ меньше ключа текущего узла, идем влево
            elif key < curr.key:
                curr = curr.left
            # Если искомый ключ больше ключа текущего узла, идем вправо
            else:
                curr = curr.right
        # Если не нашли искомый узел, возвращаем False
        return False

    # Поиск ключа следующего по величине
    def next(self, key):
        curr = self.root
        next_key = None
        # Продолжаем обход дерева, пока не дойдем до конца или не найдем узел с искомым ключом
        while curr is not None:
            # Если ключ текущего узла больше искомого, запоминаем его, идем влево
            if curr.key > key:
                if next_key is None or curr.key < next_key:
                    next_key = curr.key
                curr = curr.left
            # Если ключ текущего узла меньше или равен искомому, идем вправо
            else:
                curr = curr.right
        # Если нашли следующий ключ, возвращаем его в виде строки, иначе возвращаем "none"
        return str(next_key) if next_key is not None else "none"

    # Поиск ключа предыдущего по величине
    def prev(self, key):
        curr = self.root
        prev_key = None
        # Продолжаем обход дерева, пока не дойдем до конца или не найдем узел с искомым ключом
        while curr is not None:
            # Если ключ текущего узла меньше искомого, запоминаем его, идем вправо
            if curr.key < key:
                if prev_key is None or curr.key > prev_key:
                    prev_key = curr.key
                curr = curr.right
            # Если ключ текущего узла больше или равен искомому, идем влево
            else:
                curr = curr.left
        # Если нашли предыдущий ключ, возвращаем его в виде строки, иначе возвращаем "none"
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
        if line[0] == "insert":  # если первое слово в строке - "insert"
            bst.insert(int(line[1]))  # вызываем метод insert
        elif line[0] == "delete":  # если первое слово в строке - "delete"
            bst.delete(int(line[1]))  # вызываем метод delete
        elif line[0] == "exists":  # если первое слово в строке - "exists"
            f_out.write(str(bst.exists(int(line[1]))) + '\n')  # вызываем метод exists
        elif line[0] == "next":  # если первое слово в строке - "next"
            f_out.write(str(bst.next(int(line[1]))) + '\n')  # вызываем метод next
        elif line[0] == "prev":  # если первое слово в строке - "prev"
            f_out.write(str(bst.prev(int(line[1]))) + '\n')  # вызываем метод prev
print("Время работы: %s секунд" % (perf_counter() - t_start))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
