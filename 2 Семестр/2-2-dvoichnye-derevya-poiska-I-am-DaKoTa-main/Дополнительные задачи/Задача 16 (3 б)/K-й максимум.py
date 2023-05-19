from bisect import bisect_left, insort_left  # двоичный поиск
from time import perf_counter
import tracemalloc

t_start = perf_counter()
tracemalloc.start()


class OrderStatisticTree:
    def __init__(self):
        self.tree = []  # Списка для хранения элементов
        self.count = 0  # Счетчик числа элементов в списке

    # Добавляем элемент в список
    def insert(self, x: int):
        insort_left(self.tree, x)  # Вставляем элемент в отсортированный список
        self.count += 1  # Увеличиваем счетчик числа элементов в списке

    # Поиска k-го максимума
    def find_by_order(self, k: int) -> int:
        return self.tree[k]  # Возвращаем k-й элемент отсортированного списка

    # Удаления элемента из списка
    def erase(self, x: int):
        index = bisect_left(self.tree, x)  # Находим индекс элемента в отсортированном списке
        if index < len(self.tree) and self.tree[index] == x:  # Если элемент найден
            self.tree.pop(index)  # Удаляем элемент из списка
            self.count -= 1  # Уменьшаем счетчик числа элементов в списке


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        n = int(f.readline())
    f.close()
    # Создаем объект класса OrderStatisticTree для хранения дерева и счетчика
    oSet = OrderStatisticTree()
    with open("output.txt", "w+") as f_out, open('input.txt') as f:
        for i in range(n + 1):
            command, *args = map(int, f.readline().split())
            # Если команда равна 1, то добавляем аргумент как элемент в дерево
            if command == 1:
                oSet.insert(*args)
            # Если команда равна 0, то находим k-й максимум, где k = oSet.count - args[0]
            elif command == 0:
                k = oSet.count - args[0]
                f_out.write(str(oSet.find_by_order(k)) + '\n')
            # Если команда равна -1, то удаляем элемент из дерева по аргументу
            elif command == -1:
                oSet.erase(*args)
print("Время работы: %s секунд" % (perf_counter() - t_start))
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
