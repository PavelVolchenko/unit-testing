class Product:

    def __init__(self, name: str, cost: int):
        self.__name = name
        self.__cost = cost

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost
