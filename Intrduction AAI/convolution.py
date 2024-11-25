import numpy as np

original_data = np.array([[3, 0, 1, 2, 7, 4, 4, 3],
                         [1, 5, 8, 9, 3, 1, 1, 5],
                         [2, 7, 2, 5, 1, 3, 2, 2],
                         [0, 1, 3, 1, 7, 8, 7, 1],
                         [4, 2, 1, 6, 2, 9, 9, 6],
                         [2, 4, 5, 2, 3, 8, 6, 9],
                         [4, 3, 5, 3, 2, 2, 7, 2],
                         [3, 5, 2, 1, 2, 9, 3, 1]])
cnn_filter = np.array([[1, 2, 3],
                       [4, 1, -1],
                       [-2, -3, -4]])

DATA_ROW, DATA_COL = original_data.shape
FILTER_ROW, FILTER_COL = cnn_filter.shape

temp_li = list()
convolved_li = list()
for row in range(DATA_ROW - (FILTER_ROW - 1)):
    temp_li.clear()
    for col in range(DATA_COL - (FILTER_COL - 1)):
        slicing_data = original_data[row:row + FILTER_ROW, col:col + FILTER_COL]
        temp_li.append(np.dot(slicing_data.flatten(), cnn_filter.flatten()))
    convolved_li.append(temp_li[:])

for li in convolved_li:
    print(li)