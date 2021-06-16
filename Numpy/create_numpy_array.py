import numpy as np

#List
v = np.array([1, 2, 3, 4, 5])
print(v)
#Matrix the argumen

m = np.array([[1, 2, 3], [4, 5, 8]])
print(m)

#Melihat type array
print(type(v))
print(type(m))

#tipe list
a = [1,2,3]
print(type(a))

#Untuk mengetagui shape dari array 
v.shape
print(v.shape)
print(m.shape)

#Untuk mengetahui type data di dalam array menggunakan apa
m.dtype
print(m.dtype)

# Jika ingin mendefine tipe data yang digunakan pake dtype dibelakang
m = np.array([[3, 5, 7],[3, 6, 8]], dtype= float)
print(m)