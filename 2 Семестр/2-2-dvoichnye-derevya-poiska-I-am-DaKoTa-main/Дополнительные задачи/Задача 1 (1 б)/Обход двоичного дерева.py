# класс Node для представления узлов дерева
class Node:
    def __init__(self, key, left_child, right_child):
        self.key = key  # Ключ узла
        self.left_child = left_child  # Левый потомок
        self.right_child = right_child  # Правый потомок


# класс Tree для представления дерева
class Tree:
    def __init__(self, nodes):
        self.nodes = nodes  # Массив узлов дерева

    # Центрированный обход в глубину
    # node_index - индекс текущего узла, traversal_list - список для сохранения значений ключей
    def inorder_traversal(self, node_index, traversal_list):
        if node_index == -1:
            return
        node = self.nodes[node_index]
        # Обходим левое поддерево
        self.inorder_traversal(node.left_child, traversal_list)
        # Добавляем ключ текущего узла
        traversal_list.append(node.key)
        # Обходим правое поддерево
        self.inorder_traversal(node.right_child, traversal_list)

    # Прямой обход в глубину
    # node_index - индекс текущего узла, traversal_list - список для сохранения значений ключей
    def preorder_traversal(self, node_index, traversal_list):
        if node_index == -1:
            return
        node = self.nodes[node_index]
        # добавляем ключ текущего узла
        traversal_list.append(node.key)
        # обходим левое поддерево
        self.preorder_traversal(node.left_child, traversal_list)
        # обходим правое поддерево
        self.preorder_traversal(node.right_child, traversal_list)

    # Обратный обход в глубину
    # node_index - индекс текущего узла, traversal_list - список для сохранения значений ключей
    def postorder_traversal(self, node_index, traversal_list):
        if node_index == -1:
            return
        node = self.nodes[node_index]
        # обходим левое поддерево
        self.postorder_traversal(node.left_child, traversal_list)
        # обходим правое поддерево
        self.postorder_traversal(node.right_child, traversal_list)
        # добавляем ключ текущего узла
        traversal_list.append(node.key)


with open("input.txt") as f:
    n = int(f.readline())  # Количество узлов
    nodes = []  # Список узлов дерева
    for i in range(n):
        key, left_child, right_child = map(int, f.readline().split())
        nodes.append(Node(key, left_child, right_child)) # создаем узел с заданным ключом и потомками
tree = Tree(nodes) # создаем объект дерева
inorder_list = []

# обходим дерево в порядке in-order, сохраняем значения ключей в список
tree.inorder_traversal(0, inorder_list)
with open("output.txt", 'w+') as f:
    # записываем значения ключей в порядке in-order в файл
    f.write(' '.join(map(str, inorder_list)) + '\n')
    preorder_list = []

    # обходим дерево в порядке pre-order, сохраняем значения ключей в список
    tree.preorder_traversal(0, preorder_list)
    # записываем значения ключей в порядке pre-order в файл
    f.write(' '.join(map(str, preorder_list)) + '\n')
    postorder_list = []

    # обходим дерево в порядке post-order, сохраняем значения ключей в список
    tree.postorder_traversal(0, postorder_list)
    # записываем значения ключей в порядке post-order в файл
    f.write(' '.join(map(str, postorder_list)) + '\n')
