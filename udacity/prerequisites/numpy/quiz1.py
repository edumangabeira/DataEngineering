import numpy as np
import string

letter_array = np.array(list(string.ascii_lowercase[0:10]))
print("Letter Array: ", letter_array)

print("dtype: {}".format(letter_array.dtype))
print("shape: {}".format(letter_array.shape))
print("size: {}".format(letter_array.size))
