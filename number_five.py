def implicit_backward_divided_difference(func, x, y_current, y_prev, h=0.001):
    """
        author: Collins C. Chinedu <kolyneschinedu@gmail.com>

        calculates the approximate derivative of an implicit function 'f(x, y)' using the backward divided difference.

        params:

                func -> implicit function of basic form 'f(x, y)'
                x -> point x at which the derivative is approximated
                y_current -> value of y at x
                y_prev -> value of y at (x - h)
                h -> step value
    """
    return (func(x, y_current) - func(x - h, y_prev)) / h

def explicit_eular_method(y, x, df, h=0.001):
    """
        author: Collins C. Chinedu <kolyneschinedu@gmail.com>

        approximates the value of y at a point (x + h) from its explicit differential equation

        params:

                y -> value of y at point x
                x -> a point x of which y is known
                df -> explicit function of form 'f(x, y)' representing the value of dy/dx
                h -> step value
    """
    return y + h*df(x, y)

def implicit_eular_method(y_current, y_prev, x, df, h=0.001):
    """
        author: Collins C. Chinedu <kolyneschinedu@gmail.com>
        
        approximates the value of y at a point (x + h) from its implicit differential equation

        params:

                y_current -> value of y at x
                y_prev -> value of y at (x - h)
                x -> point x at which y_current is known
                df -> implicit function of form 'f(x, y)' representing the value of dy/dx
                h -> step value
    """
    return y_current - (y_current - y_prev - h*df(x, y_current)) / (1 - h * implicit_backward_divided_difference(df, x, y_current, y_prev, h))
    
