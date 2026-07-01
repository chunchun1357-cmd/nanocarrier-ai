import numpy as np

python_list = [120, 180, 150]
numpy_array = np.array([120, 180, 150])

print("--- Python list ---")
print(python_list)
print("list+list:", python_list + python_list)
print("mean:", sum(python_list) / len(python_list))

print("\n--- NumPy array---")
print(numpy_array)
print("array + array:", numpy_array + numpy_array)
print("array + 10:", numpy_array + 10)
print("mean:", numpy_array.mean())
print("std:", numpy_array.std())
print("under 160:", numpy_array[numpy_array < 160])
