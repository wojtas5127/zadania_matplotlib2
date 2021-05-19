import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Zadanie 1

# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
#
# z = np.linspace(0, 2 * np.pi)
# x = np.sin(z)
# y = 2 * np.cos(z)
#
# ax.plot(x,y,z,label='Zadanie1')
# ax.legend()
# plt.show()

# Zadanie 2

# np.random.seed(19680801)
#
# def randrange(n,vmin,vmax):
#     return (vmin - vmax) * np.random.rand(n) + vmin
#
# fig=plt.figure()
# ax=fig.add_subplot(111,projection='3d')
# n=5
#
#
# for c, m, zlow, zhigh in [('r','o',-50,-25),('y','^',-35,5),('g','X',-60,-60),('b','p',60,5),('purple','d',-50,-5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#
# ax.set_xlabel('oś x')
# ax.set_ylabel('oś y')
# ax.set_zlabel('oś z')
# plt.show()

