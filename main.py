# Атрибуты
# Обращение к атрибутам
# Время жизни атрибутов
# Конструктор
# Объект и класс
# Методы и функции
# Вызов методов, их объявление
#
# Задача: сумма по всем узлам


# Бинарное дерево - ацикический связный граф
# Есть вершины. Из каждой вершины выходит не более 2 ребер
# Есть корень - начало дерева


class Node:
    def __init__(self, left, right, parent, number):
        self.left = left
        self.right = right
        self.parent = parent
        self.number = number


root = Node(None, None, None, 1)
node7 = Node(None, None, root, 7)
root.left = node7
node9 = Node(None, None, root, 9)
root.right = node9


def sum_numbers(root):
    s = root.number
    right = root.right
    if right is not None:
        s += sum_numbers(right)
    left = root.left
    if left is not None:
        s += sum_numbers(left)
    return s


def find(root, number):
    # TODO: implement method that finds node with given number inside tree
    # TODO: if there's no such node - return False
    # TODO: otherwise return True
    pass


print(find(root, 42))  # False
print(find(root, 9))  # True


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def my_name(self):
        print(f"Меня зовут {self.name}, моя порода {self.breed}")


bonk = Dog("Bonk", "Овчарка")
print(bonk.name)
bonk.my_name()
bonk.my_name()
mila = Dog("Mila", "Шпиц")
print(mila.name)
mila.my_name()

