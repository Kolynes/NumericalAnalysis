import number_one

def newton_raphson_method(func, x=10, e=0.001, max_iterations=1000):
    """
        author: Collins C. Chinedu <kolyneschinedu@gmail.com>

        calculates the root of a non linear function using the Newton-Raphson iterative method

        params: 

                 func -> scalar function of the basic form 'f(x)'
                 x -> initial guess of the root
                 e -> epsilon value that defines the acceptable approximation of the root ie ' |f(x)| < e ' 
                 max_iterations -> maximum number of iterations to execute when finding the root
    """
    for n in range(max_iterations):
        y = func(x)
        y_prime = number_one.derivative(func, x)
        if abs(y) >= e:
            x = x - (y / y_prime)
        else:
            return x
    raise RootNotFoundException

class RootNotFoundException(Exception):
    """
        author: Collins C. Chinedu <kolyneschinedu@gmail.com>

        A custom exception to throw when a function's root is not found.
    """
    def __init__(self, *args):
        super(Exception, self)
        self.args = [("No root found in the maximum number of iterations")]

