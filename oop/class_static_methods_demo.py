# class Calculator:
    
#     def add(a,b):
#         # self.a = a
#         # self.b = b
#         return a + b
#     @staticmethod
    
#     def multipy(cls,a,b):
#         return a* b
#     @classmethod


class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
