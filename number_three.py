import math
import number_two

# definition of logarithmic function given 
function = lambda x: x/10 - math.log10(x)

# calculation of the root
try:
    root = number_two.newton_raphson_method(function)
    print("x = %f" %root)
except number_two.RootNotFoundException as e:
    print(e.args[0])