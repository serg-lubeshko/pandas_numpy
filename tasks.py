import numpy as np


def solution(arr):
    arr1 = np.array(array)[1:4, 1:2].flatten()
    arr2 = np.array(array)[2:, 2:3].flatten()
    arr = arr1 + arr2
    return arr


def solution2(arr):
    arr1 = np.array(arr)[0:3, 3:]
    print(arr1)
    arr2 = np.array(arr)[2:, 0:2]
    arr = arr1 + arr2
    print(arr)
    return arr


def solution3(arr):
    arr1 = np.array(arr)[0:, 0:1].flatten()
    print(arr1)
    arr2 = np.array(arr)[0:, 2:3].flatten()
    print(arr2)
    arr = arr1 > arr2
    # arr = arr1 + arr2
    print(arr)
    return arr


if __name__ == '__main__':
    array = ([[10, 12, 14, 18, 20], [8, 22, 18, 19, 12], [4, 14, 84, 38, 11], [2, 32, 4, 31, 9], [1, 11, 1, 8, 6]])

# print(solution(array))
# print(solution2(array))
solution3(array)
