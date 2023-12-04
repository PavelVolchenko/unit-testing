class Calculator:
    @staticmethod
    def calculate(first_operand: float, second_operand: float, operator: chr):
        match operator:
            case '+':
                return first_operand + second_operand
            case '-':
                return first_operand - second_operand
            case '*':
                return first_operand * second_operand
            case '/':
                if second_operand != 0:
                    return first_operand / second_operand
                raise ZeroDivisionError("Division by zero is not possible")
        raise ValueError("Unexpected value operator: " + operator)

    @staticmethod
    def square_root(number: float):
        if number == 0:
            raise ArithmeticError("It is not possible to extract the root from 0")
        if number < 0:
            raise ArithmeticError("It is impossible to extract the root from negative numbers")
        return number ** 0.5

        # @ param purchase_amount сумма покупки
        # @ param discount_amount размер скидки (в процентах)
        # @ return возвращает сумму покупки с учетом скидки

    @staticmethod
    def calculate_discount(purchase_amount: float, discount_amount: int):
        if purchase_amount < 0:
            raise ArithmeticError(" Purchase amount can't be negative")
        if discount_amount < 0:
            raise ArithmeticError("Negative discount is not possible")
        if discount_amount > 100:
            raise ArithmeticError("Discount more 100% is not possible")
        return purchase_amount - purchase_amount * discount_amount / 100
