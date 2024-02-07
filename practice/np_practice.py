import numpy as np

def create_array():
    arr1 = np.array([0,1,2,3])
    return arr1

def reverse_np_array(arr, method):
    if method ==1:
        rev_arr = arr[::-1]   
    elif method == 2:
        rev_arr = np.flip(arr, axis=0)
    elif method == 3:
        rev_arr = np.array(list(reversed(arr)))
    elif method == 4:
        rev_arr = np.flipud(arr)
    print("Original Array : ", arr)
    print("Reversed Array : ",rev_arr)
    print()
    return rev_arr

#input : 1 2 3 4 5 6 7 8 9
# output : 
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
def reshape_np_from_number(arr):
    array = np.array([int(item) for item in arr.split()])
    array.shape = (3, 3)
    print(array)

#input : 1 2 3 4 5 6 , 2, 3
#output : 
# [[1 2]
#  [3 4]
#  [5 6]]
def fixed_1stdim(string, N, M):
    arr = list(map(int, string.split()))
    arrA = np.array(arr).reshape(N,M)
    print(arrA)
    return arrA

def concat_example():
    array_1 = np.array([[1,2,3],[0,0,0]])
    array_2 = np.array([[0,1,0],[7,8,9]])

    print(array_1)
    print()
    print (np.concatenate((array_1, array_2), axis = 1)   )
    print()
    print (np.concatenate((array_1, array_2), axis = 0)   )


# N, M = map(int, input().split())
# lst=[]
# for _ in range(N):
#     lst.append([int(x) for x in input().split()])

# arr = np.array(lst)
# print(arr.T)
# print(arr.flatten())
