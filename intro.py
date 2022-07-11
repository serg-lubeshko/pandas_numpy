import numpy as np

arr1 = np.zeros((5, 3), dtype=int)

print(arr1, 'zeros')
print(arr1.shape, 'zeros - функции, которая возвращает кортеж с количеством элементов по каждой оси.')

arr2 = np.ones((2, 3), dtype=float)
print(arr2, 'ones')

arr = np.array((1, 2, 3), dtype=int)
print(arr, 'array')
print(arr.ndim, 'ndim -  свойства, которое возвращает количество измерений в массиве. ')

arr3 = np.full((2, 8), 'y')
print(arr3, 'full')

arr4 = np.arange(11)
print(arr4, 'arange - функции, которая создает одномерный массив со значениями от 0 до N-1')
