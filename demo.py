# System imports
import ctypes

a = ctypes.CDLL("./liba.so")
print("Opened library a. Pushing 3 elements to static vector and calling the size of the vector")
print(a.push_3_items_to_static_vector_and_get_size())
print("And second time on the same library a")
print(a.push_3_items_to_static_vector_and_get_size())

b = ctypes.CDLL("./libb.so")
print("Opened library b. Pushing 3 elements to static vector and calling the size of the vector")
# This prints 3 instead of 9
print(b.push_3_items_to_static_vector_and_get_size())
