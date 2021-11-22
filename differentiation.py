# import numpy as np
# function1 = np.poly1d([2,3,4,5,6,7])
# print("f(x) =\n",function1)
# derivative = function1.deriv()
# print("f'(x)=",derivative)


class Differentiation:
    def __init__(self):
        self.function = []
    def add(self,value):
        self.function.append(value)
    def derivative(self):
        self.grad_function = []
        for i in range(len(self.function)-1):
            coeff = self.function[i]
            self.grad_function.append(coeff*(len(self.function)-i-1))
        print (self.grad_function)
eg1 = Differentiation()
eg1.add(2)
eg1.add(3)
eg1.add(4)
eg1.add(5)
eg1.add(6)
eg1.add(7)
eg1.derivative()
