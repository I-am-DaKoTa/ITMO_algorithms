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


# Класс бинарного дерева
class BinaryTree:
    def __init__(self):
        self.root = None

    # Добавление узла в дерево
    def addNode(self, key):
        x = self.root
        y = None
        cmp = 0
        # Пока не достигнем конца дерева
        while x is not None:
            # Сравниваем ключ текущего узла с ключом нового узла
            cmp = x.key - key
            if cmp == 0:  # Если ключи равны, новый узел не добавляем
                return
            else:
                y = x  # Сохраняем текущий узел в y
                # Если ключ нового узла больше текущего, идем направо
                if cmp < 0:
                    x = x.right
                # Иначе идем налево
                else:
                    x = x.left
        # Создаем новый узел
        newNode = Node(key)
        # Если дерево пустое, новый узел становится корневым
        if y is None:
            self.root = newNode
            print(key, "корень")
        else:
            # Если ключ нового узла больше y, новый узел становится правым потомком y
            if cmp > 0:
                y.left = newNode
                print(key, "левый для", y.key)
            # Иначе новый узел становится левым потомком y
            else:
                y.right = newNode
                print(key, "правый для", y.key)

    # Удаление узла из дерева
    def removeSubtree(self, key):
        x = self.root
        y = None
        cmp = 0
        # Пока не достигнем конца дерева
        while x is not None:
            # Вычисляем разницу ключей
            cmp = x.key - key
            # Если ключи совпадают, то удаляем узел
            if cmp == 0:
                break
            else:
                y = x
                # Если ключ искомого узла больше текущего ключа, идем направо
                if cmp < 0:
                    x = x.right
                # Иначе идем налево
                else:
                    x = x.left
        # Если узел не найден
        if x is None:
            print("Ничего не удалено")
            return 0
        count = self.nodesCount(x)
        print("удаляется", x.key)
        print("его поддерево", count, "узлов")
        # Удаляем ссылку на узел из родительского узла
        if x.key > y.key:
            y.right = None
        else:
            y.left = None
            # Удаляем ссылку на узел
        x = None
        # Возвращаем количество узлов в поддереве
        return count

    # Подсчет количества узлов в поддереве
    def nodesCount(self, node):
        # Если у узла нет потомков, возвращаем 1
        if node.left is None and node.right is None:
            return 1
        left = right = 0

        # Если есть левый потомок, считаем количество узлов в его поддереве
        if node.left is not None:
            left = self.nodesCount(node.left)

        # Если есть правый потомок, считаем количество узлов в его поддереве
        if node.right is not None:
            right = self.nodesCount(node.right)

        # Возвращаем количество узлов в поддереве
        return left + right + 1


if __name__ == "__main__":
    with open("input.txt") as f:
        nodesCount = int(f.readline())  # количество узлов в дереве
        arrayNodes = []  # массив для хранения узлов дерева
        for i in range(nodesCount):
            node = [int(x) for x in f.readline().split()]
            arrayNodes.append(node)

        removesCount = int(f.readline())
        arrayRemove = [int(x) for x in f.readline().split()]
    tree = BinaryTree()
    for node in arrayNodes:
        tree.addNode(node[0])
    with open("output.txt", "w") as f:
        for i in range(removesCount):
            nodesCount -= tree.removeSubtree(arrayRemove[i])
            print(nodesCount)
            f.write(str(nodesCount) + "\n")
print("Время работы: %s секунд" % (perf_counter() - t_start))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
