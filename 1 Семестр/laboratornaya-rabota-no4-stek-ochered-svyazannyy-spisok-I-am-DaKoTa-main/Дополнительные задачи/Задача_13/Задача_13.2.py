# Класс очереди с функциями Enqueue, Dequeue c проверкой
# на переполнение и опустошения очереди.
class Queue:

    # Класс для создания узла связанного списка,
    # где первый элемент значение, а второй ссылка на второй элемент
    class Node:
        def __init__(self, data):
            # устанавливает данные в выделенном узле и возвращает их
            self.data = data
            self.next = None

    def __init__(self):
        self.back = None
        self.front = None

    # Функция для добавления элемента в очередь
    def enqueue(self, item):  # Вставка # в конце

        # Выделяет новый узел
        node = Queue.Node(item)

        # Проверка пуста ли очередь
        if self.front is None:
            # Инициализирует как верхние, так и нижние
            self.front = node
            self.back = node
        else:
            # Обновление сзади
            self.back.next = node
            self.back = node

    # Функция для извлечения из очереди нижнего значения и его удаления из очереди
    def dequeue(self):
        if self.front is None:
            print('Очередь опустошена')
            exit(-1)

        # Принимает к сведению данные верхнего узла
        front = self.front.data

        # Обновляет верхний указатель, чтобы он указывал на следующий узел
        self.front = self.front.next

        # Если список станет пустым
        if self.front is None:
            self.back = None

        # вернуть удаленный элемент
        return front

    # Функция вывода нижнего значения без последующего его удаления
    def peek(self):
        if not self.isEmpty():
            return self.front.data
        else:
            print('Error peek')
            exit(-1)

    # Функция для проверки пуста ли очередь или нет
    def isEmpty(self):
        return self.back is None and self.front is None


if __name__ == '__main__':

    q = Queue()

    q.enqueue(2)
    q.enqueue(7)
    q.enqueue(3)
    q.enqueue(1)
    q.enqueue(5)
    print('Нижний элемент', q.peek())
    q.enqueue(2)
    q.enqueue(6)
    q.enqueue(2)
    print('Нижний элемент', q.peek())

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print('Нижний элемент', q.peek())
    q.dequeue()
    q.dequeue()

    if q.isEmpty():
        print('Очередь пуста')
    else:
        print('Очередь не пуста')

    q.dequeue()