import numpy as np

matrix_array = np.random.rand(10,10)
Min =  matrix_array.min(axis=1)
Max =  matrix_array.max(axis=1)

Min_column =  matrix_array.min(axis=0)
Max_column =  matrix_array.max(axis=0)
print(matrix_array)
print("Minimum element in array in each row:", Min)
print("Maximum element in array in each row:", Max)

print("Minimum element in array in each column:", Min_column)
print("Maximum element in array in each column:", Max_column)


print("------------------------------------")
print("using for loop")

min_row = [min(row) for row in matrix_array]

min_col = [min(column) for column in zip(*matrix_array)]
print("minimum row value",min_row)
print("minimum column value",min_col)

max_row = [max(row) for row in matrix_array]

max_col = [max(column) for column in zip(*matrix_array)]
print("maximum row value",max_row)
print("maximum column value",max_col)