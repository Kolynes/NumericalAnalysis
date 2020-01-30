import math 
import number_five

# definition of the derivative
df = lambda x, y: -math.sin(x) * (math.cos(x * y))**2

# define the table of points (x, y) and step value
points = []
h = 0.001

# insert into the table the initial point
x = 0
y = 1
points.append((x, y))

# calculate initial approximation
y_prev = y
y_current = number_five.explicit_eular_method(y, x, df, h)
points.append((x + h, y_current))
x += h

# iteratively populate the table
while x <= 2:
    temp = y_current
    y_current = number_five.implicit_eular_method(y_current, y_prev, x, df, h)
    y_prev = temp
    points.append((x + h, y_current))
    x += h