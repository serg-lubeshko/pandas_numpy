import numpy as np

# or |
# and &


users = np.array(["Андрей", "Иван", "Николай", "Александр", "Андрей"])
visits = np.array(
    [
        [1, 2, 1, 0, 0, 1, 1],
        [1, 2, 1, 0, 0, 1, 1],
        [2, 1, 0, 2, 0, 2, 1],
        [1, 2, 1, 0, 1, 1, 1],
        [1, 2, 1, 0, 0, 1, 0],
    ])

mask1 = users == "Иван"
print(f'mask1 Иван - {mask1}')
mask2 = users == "Андрей"
print(f'mask2 Андрей - {mask2}')

print(f"union mask1 | mask2 (Иван+Андрей){mask1 | mask2}")

# 2. Можно маску круче написать

mask = (users == "Иван") | (users == "Александр")
print(f"2. Можно маску круче написать mask = (users == 'Иван') | (users == 'Александр') >>> {mask}")


#******************индексация***************************

index_array1=visits[0]
index_array2=visits[2]
print(f"3.new_array = np.array([line1, line2])>>>{np.array([index_array1, index_array2])}")
#можем записать это более компактно
new_m2d = visits[[0, 2], :]
print(f"4.можем записать это более компактно new_m2d = visits[[0, 2], :] >>> {new_m2d}")