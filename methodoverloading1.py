class Calculator:
    def add(self, *args):
        total = 0
        for num in args:
            total += num
        return total

calc = Calculator()

print(calc.add(2, 3))      
print(calc.add(2, 3, 4))