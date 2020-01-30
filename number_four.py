import math
import number_two

# initial contants 
P_pr = 6
t = 1/2

# Definitions of A1, A2, A3, A4
A1 = 0.06215 * math.e**(1.2 * (1 - t)**2)
A2 = 14.76*t - 9.76*(t**2) + 4.58*(t**3)
A3 = 90.7*t - 242.2*(t**2) + 42.4*(t**3)
A4 = 2.18 + 2.82*t

#definition of the function of y
function_of_y = lambda y: -A1*P_pr + (y + y**2 + y**3 - y**4)/((1 - y)**3) - A2*y**2 + A3*y**A4

# definition of z
definition_z = lambda y: (A1 * P_pr) / y

# calculation of the root
try:
    root = number_two.newton_raphson_method(function_of_y)
except number_two.RootNotFoundException as e:
    print(e.args[0])

# solve for z
z = definition_z(root)
print("z = %f" %z)