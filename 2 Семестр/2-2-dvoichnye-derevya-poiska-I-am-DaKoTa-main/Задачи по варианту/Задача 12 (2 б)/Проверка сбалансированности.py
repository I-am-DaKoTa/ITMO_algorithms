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
        self.height = 1  # Высота узла

    def balance(self):
        # Вычисляем баланс узла (разницу между высотами правого и левого поддеревьев)
        right_height = self.right.height if self.right else 0
        left_height = self.left.height if self.left else 0
        return right_height - left_height


def read_tree_from_input_file():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        # Создаем словарь узлов дерева, где ключ - номер узла, значение - объект Node
        nodes = {i + 1: Node(None) for i in range(n)}
        # Заполняем поля узлов
        for i in range(n):
            # Считываем значения ключа и потомков
            key, left, right = map(int, f.readline().split())
            # Получаем узел по его номеру
            node = nodes[i + 1]
            node.key = key
            if left:
                node.left = nodes[left]
            if right:
                node.right = nodes[right]
        # Возвращаем корневой узел дерева
        return nodes[1]


# Функция для обновления высоты узла
def update_height(node):
    # Обновляем высоты всех узлов в дереве (построчный обход дерева)
    left_height = node.left.height if node.left else 0
    right_height = node.right.height if node.right else 0
    node.height = max(left_height, right_height) + 1


# Функция для обновления высот всех узлов в дереве
def update_heights(node):
    # Записываем балансы узлов дерева в файл
    if not node:
        return
    update_heights(node.left)  # Обновляем высоты у левого поддерева
    update_heights(node.right)  # Обновляем высоты у правого поддерева
    update_height(node)  # Обновляем высоту узла


# Функция для записи балансов всех узлов в выходной файл
def write_balances_to_output_file(root):
    with open('output.txt', 'w') as f:
        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            # Записываем баланс текущего узла в файл
            f.write(str(node.balance()) + '\n')
            if node.left:
                # Добавляем левого потомка в список узлов для обхода
                nodes.append(node.left)
            if node.right:
                # Добавляем правого потомка в список узлов для обхода
                nodes.append(node.right)


root = read_tree_from_input_file()
update_heights(root)
write_balances_to_output_file(root)
print("Время работы: %s секунд" % (perf_counter() - t_start))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
