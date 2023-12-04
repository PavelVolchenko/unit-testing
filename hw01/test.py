import unittest
from calculator import Calculator
from shop import Shop
from product import Product


def test():
    if 8 != Calculator.calculate(2, 6, '+'):
        raise AssertionError("Ошибка в методе")

    if 0 != Calculator.calculate(2, 2, '-'):
        raise AssertionError("Ошибка в методе")

    if 14 != Calculator.calculate(2, 7, '*'):
        raise AssertionError("Ошибка в методе")

    if 2 != Calculator.calculate(100, 50, '/'):
        raise AssertionError("Ошибка в методе")

    try:
        Calculator.calculate(8, 4, '_')
    except:
        AssertionError("Ошибка в методе")

    assert 8 == Calculator.calculate(2, 6, '+')
    assert 0 == Calculator.calculate(2, 2, '-')
    assert 14 == Calculator.calculate(2, 7, '*')
    assert 2 == Calculator.calculate(100, 50, '/')


class CalculatorTest(unittest.TestCase):

    def test_result(self):
        self.assertEqual(90.0, Calculator.calculate_discount(purchase_amount=100, discount_amount=10))

    def test_zero_result(self):
        self.assertEqual(0, Calculator.calculate_discount(purchase_amount=0, discount_amount=10))

    def test_zero_discount(self):
        self.assertEqual(100, Calculator.calculate_discount(purchase_amount=100, discount_amount=0))

    def test_discount_less_0(self):
        self.assertEqual(105, Calculator.calculate_discount(purchase_amount=100, discount_amount=-5))

    def test_discount_more_100(self):
        self.assertEqual(-10, Calculator.calculate_discount(purchase_amount=100, discount_amount=110))

    def test_negative_amount(self):
        self.assertEqual(-50, Calculator.calculate_discount(purchase_amount=-100, discount_amount=50))


class TestShop(unittest.TestCase):

    def setUp(self):
        self.a = Product('bread', 35)
        self.b = Product('milk', 85)
        self.c = Product('sugar', 45)
        self.d = Product('tea', 25)
        self.e = Product('coffee', 40)
        self.product_list = [self.a, self.b, self.c, self.d, self.e]
        self.shop = Shop(self.product_list)

    def test_get_products(self):
        for product in self.product_list:
            self.assertIsInstance(product, Product)

    def test_set_products(self):
        self.failureException(self.shop.set_products(self.product_list), self.shop)

    def test_sorted_list_products(self):
        shop = self.shop.get_sorted_list_products()
        for i in range(1, len(shop)):
            self.assertGreaterEqual(shop[i].get_cost(), shop[i - 1].get_cost())

    def test_most_expensive_product(self):
        self.assertEqual(self.shop.get_most_expensive_product().get_cost(),
                         max(self.product_list, key=lambda x: x.get_cost()).get_cost())


if __name__ == "__main__":
    test()
    unittest.main()
