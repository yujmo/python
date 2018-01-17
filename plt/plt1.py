# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
with open('/root/桌面/Racc.txt') as fp:
    population_ages = fp.readlines()

popu1 = [float(x.split()[0]) for x in population_ages]
popu2 = [float(x.split()[1]) for x in population_ages]
popu3 = [float(x.split()[2]) for x in population_ages]

x3 = range(0, len(popu3))
x2 = range(0, len(popu2))
x1 = range(0, len(popu1))

plt.plot(x1, popu1, "r--", label='1 line', color="black", marker='*')
plt.plot(x2, popu2, "b--", label='2 line', color="blue", marker='h')
plt.plot(x3, popu3, label='3 line', color="red", marker='p')
plt.xlabel('number')
plt.ylabel('value')
plt.ylim(-2, 2)
plt.xticks(fontsize=20)

plt.title('picture')
plt.grid()

plt.legend()
plt.show()
