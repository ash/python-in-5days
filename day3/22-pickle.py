# Demonstrating the difference between pickle and json.

import pickle
import json

data = {"alpha": [1, 3, 4], "beta": "11, 22, 33"}

# You dump your data to a binary (notice the 'b' mode) file:
with open('saved.data', 'wb') as f:
    pickle.dump(data, f)

# You can restore it by loading it back
with open('saved.data', 'rb') as f:
    restored_data = pickle.load(f)
    print(restored_data)

# You can also save the state of a class instance. Here's a class.
class X:
    def __init__(self, value):
        self.value = value

# An here's where you try to save it as a picke object
x = X(27)
with open('x.json', 'wb') as f:
    pickle.dump(x, f)

# After restoring it, you get your object back. Do not be confused with the '.json' file extension:
# this is because we tried to save the object in the json format, and that attempt failed, as you cannot
# represent a class instance using JSON.
with open('x.json', 'rb') as f:
    restored_x = pickle.load(f)
    print(type(restored_x))
    print(restored_x.value)

