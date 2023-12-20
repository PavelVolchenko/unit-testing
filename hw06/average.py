"""Программа рассчитывает среднее значение каждого списка,
 сравнивает эти средние значения и выводит соответствующее сообщение"""


class Average:
    """При инициализации класс принимает два списка чисел"""

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    @staticmethod
    def average(lst):
        """Рассчитывает среднее значение списка"""
        return sum(lst) / len(lst)

    def compare(self):
        """Сравнивает средние значение списков и возвращает строку"""
        if self.average(self.list_1) > self.average(self.list_2):
            return "Первый список имеет большее среднее значение."
        if self.average(self.list_1) < self.average(self.list_2):
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
