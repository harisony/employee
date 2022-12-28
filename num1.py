import numpy as np
data_from_text_file=np.genfromtxt('sampy.txt',delimiter=',')
#print(data_from_text_file)
print(data_from_text_file)
data_from_text_file=data_from_text_file.astype('int32')
print(data_from_text_file)
print(data_from_text_file>6)

# fill values
# fill values

fill_values = np.genfromtxt('sampy.txt' ,delimiter= ',', dtype=np.int32)
print(fill_values)

fill_values = np.genfromtxt('sampy.txt' ,delimiter= ',', dtype=np.int32, filling_values = 100)
print(fill_values)
def numpy_function(x,y,z):
    return 10 * x + y + z
b = np.fromfunction(numpy_function, (4, 2, 5), dtype=int )
print(b)


