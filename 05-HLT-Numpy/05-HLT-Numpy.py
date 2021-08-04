import numpy as np

#task1
print('\n Task 1')
a1 = np.arange(10)
print(a1)

#task2
print('\n Task 2')
a2 = np.ones((3,3), dtype = bool)
print(a2)

#task3
print('\n Task 3')
a3 = np.arange(1,11)[::2]
print(a3)

#task4
print('\n Task 4')
a3 -= 1
print(a3)

#task5 -  Convert a 1D array to a 2D array with 2 rows
print('\n Task 5')
a5 = a1.reshape((2,5))
print(a5)

#task6 - Create two 1D arrays a and b, stack these two arrays vertically, use the np.dot and 
# np.sum to calculate totals
print('\n Task 6')
a = np.arange(1,4)
b = np.arange(4,7)

a6 = np.vstack((a,b))

print(a6)
print(np.dot(a,b))
print(np.sum(a6))
print(a6.sum())

#task7 - Create the following pattern without hardcoding. Use only NumPy functions and 
# the below input array
print('\n Task 7')

def f1(x, y):
    return x + 1
g1 = np.fromfunction(f1, (3, 3), dtype=int)
print(g1)

def f2(x, y):
    return y + 1
g2 = np.fromfunction(f2, (3, 3), dtype=int)
print(g2)

a7 = np.concatenate((g1,g2), axis=None)
print(a7)

#task8 - In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) – remove allrepeating items present in
#array b.

print('\n Task 8')

a = [1,2,3,4,5]
b = [4,5,6,7,8,9]
a8 = np.setdiff1d(b,a, assume_unique=True)
print(a8)

#task9 - 9. Get all items between 5 and 10 from a and b and sum themtogether.
print('\n Task 9')
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8,9])

a1 = a[ (a >= 5) & (a < 10) ]
b1 = b[ (b >= 5) & (b < 10) ]

a9 = np.concatenate((a1,b1))
print(np.sum(a9))