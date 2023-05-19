# Класс стека с функциями и isEmpty, push, pop и вывода данных
class Stack:

    # Класс для создания узла связанного списка,
    # где первый элемент значение, а второй ссылка на второй элемент
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.top = None

    # Функция для добавления элемента в стек
    def push(self, data):  # вставить в начало

        # Выделяет новый узел
        node = Stack.Node(data)

        # устанавливает данные в выделенном узле
        node.data = data

        # устанавливает указатель .next нового узла так, чтобы он указывал на текущий
        # верхний узел списка
        node.next = self.top

        # обновить верхний указатель
        self.top = node



    # Функция для извлечения из стека верхнего значения и его удаления из стека
    def pop(self):
        if self.isEmpty():
            print('Error pop')
            exit(-1)

        # Принимает к сведению данные верхнего узла
        top = self.top.data

        # Обновляет верхний указатель, чтобы он указывал на следующий узел
        self.top = self.top.next

        return top

    # Функция вывода верхнего значения без последующего его удаления
    def peek(self):
        if not self.isEmpty():
            return self.top.data
        else:
            print('Error peek')
            exit(-1)

    # Функция для проверки пуст ли стек или нет
    def isEmpty(self):
        return self.top is None



if __name__ == '__main__':

    stack = Stack()

    stack.push(2)
    stack.push(7)
    stack.push(3)
    stack.push(1)
    stack.push(5)
    print('Верхний элемент', stack.peek())
    stack.push(2)
    stack.push(6)
    stack.push(2)
    print('Верхний элемент', stack.peek())

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print('Верхний элемент', stack.peek())
    stack.pop()
    stack.pop()

    if stack.isEmpty():
        print('Стек пустой')
    else:
        print('Стек не пустой')

    stack.pop()
