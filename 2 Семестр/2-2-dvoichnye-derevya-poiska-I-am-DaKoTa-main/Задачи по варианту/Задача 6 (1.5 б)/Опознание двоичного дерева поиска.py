from time import perf_counter
import tracemalloc

t_start = perf_counter()
tracemalloc.start()


# Класс узла дерева
class Node:
    def __init__(self, key, left=None, right=None):
        # Инициализируем поля узла
        self.key = key  # Значение узла
        self.left = left  # Левый потомок
        self.right = right  # Правый потомок


# Функция для проверки, является ли дерево деревом поиска
def is_binary_search_tree(root):
    def is_bst_helper(node, low=float('-inf'), high=float('inf')):
        # Если узел пустой, то дерево - бинарное дерево поиска
        if node is None:
            return True
        # Если значение узла находится вне границ, то дерево не является бинарным деревом поиска
        if not low <= node.key <= high:
            return False
        # Рекурсивно проверяем левое и правое поддеревья
        return is_bst_helper(node.left, low, node.key) and is_bst_helper(node.right, node.key, high)

    return is_bst_helper(root)


if __name__ == '__main__':
    with open("output.txt", "w+") as f_out, open('input.txt') as f:
        n = int(f.readline())
        if n == 0:  # Если узлов нет, то дерево корректно
            f_out.write('CORRECT')
        else:
            nodes = []
            # Считываем данные об узлах и создаем объекты Node
            for i in range(n):
                key, left, right = map(int, f.readline().split())
                nodes.append(Node(key, left, right))
            root = nodes[0]  # Первый узел - корневой
            # Обходим узлы дерева и устанавливаем связи между узлами
            for node in nodes:
                if node.left != -1:
                    node.left = nodes[node.left]
                else:
                    node.left = None
                if node.right != -1:
                    node.right = nodes[node.right]
                else:
                    node.right = None
            # Проверяем, является ли дерево деревом поиска
            if is_binary_search_tree(root):
                f_out.write('CORRECT')
            else:
                f_out.write('INCORRECT')
print("Время работы: %s секунд" % (perf_counter() - t_start))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
