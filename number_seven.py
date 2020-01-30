import number_six
import matplotlib.pyplot as plt

x = []
y = []
for i in map(lambda element: element[0], number_six.points):
    x.append(i)
for i in map(lambda element: element[1], number_six.points):
    y.append(i)
plt.plot(x, y)
plt.legend()
plt.show()