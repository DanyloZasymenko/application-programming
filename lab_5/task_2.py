import numpy as np

n = 208
m = 6


def number_approximation(a, z):
    index = np.unravel_index(np.abs(a - z).argmin(), a.shape)
    print('row: ', index[0], ' column: ', index[1], ' element: ', a[index])


a = np.random.randint(-600, 600, (n, m))
print(a)
z = float(input("Enter z: "))
number_approximation(a, z)
