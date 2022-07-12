import numpy as np

# ===============================Тип данных===========================================================
arr = np.arange(10)
print(f"{arr} - тип данных {arr.dtype}")

arr1 = np.arange(10, dtype=float)
print(f"{arr1} - тип данных {arr.dtype}")

# ===============================Преобразование=======================================================
"""Преобразование в заданный тип. astype - создает новый массив"""

arr1_2 = arr1.astype(np.int32)
print(f"arr1 - преобразован в тип {arr.dtype}. Сохранен в новую переменную arr1_2")

list_ = [1.5, 1.2, 2.2, 3.8]
arr2 = np.array(list_).astype(np.int32)
print(f"arr2 - преобразован в тип {arr2.dtype}. Был {list_} >>> {arr2}")

"""Преобразование в заданный тип. Если числа в списке   формата str"""

list3 = ["1.5", "1.2", "2.2", "3.8"]
arr3 = np.array(list3).astype(np.float64)
print(f"list2 - преобразовали в тип {arr3.dtype}. Был {list3} >>> {arr3}")

list4 = ["1.5", "1!2", "2щ2", ""]
try:
    arr4 = np.array(list4).astype(np.float64)
except ValueError:
    print(f"{list4} - имеется ошибка. ValueError")

"""Преобразование в заданный тип, используя другой массив"""

m1 = np.arange(10, dtype=np.int32)
m2 = np.array([1.5, 1.2, 2.2, 3.8])

m1_float = m1.astype(m2.dtype)
print(f"{m1_float}, преобразован в {m1_float.dtype}. Был {m1} >>> {m1_float}")
