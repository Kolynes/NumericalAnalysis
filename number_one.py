def derivative(func, x, h=0.001):
    """
        author: Collins C. Chinedu <kolyneschinedu@gmail.com>

        approximates the derivative of a scalarn function at a point x using centered divided difference

        params:
        
                 func -> scalar function of the basic form 'f(x)'
                 x -> a point x at which to calculate the derivative
                 h -> step value (making this smaller calculates a more accurate derivative)
    """
    return (func(x + h) - func(x - h)) /(2 * h)