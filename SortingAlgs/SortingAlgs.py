
def selectionSort(arr):
    for i in range(0,len(arr)-1):
        iMin = i
        for j in range(i,len(arr)):
            if arr[j] < arr[iMin]:
                iMin = j
        temp = arr[i]
        arr[i] = arr[iMin]
        arr[iMin] = temp
    return arr

def insertionSort(arr):
    for i in range(1,len(arr)):
        hole = i
        value = arr[i]
        while hole > 0 and arr[hole-1] > arr[hole]:
            arr[hole] = arr[hole-1]
            hole -= 1
        arr[hole] = value
    return arr

def bubbleSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def mergeSort(a):
    def merge(b,c,a):
        i = 0
        j = 0
        k = 0
        while i < len(b) and j < len(c):
            if b[i] <= c[j]:
                a[k] = b[i]
                i += 1       
            else:
                a[k] = c[j]
                j +=1
            k += 1
        while i < len(b):
            a[k] = b[i]
            i += 1
            k += 1
        while j < len(c):
            a[k] = c[j]
            j += 1
            k+= 1

    if len(a) < 2:
        return
    mid = len(a)/2
    b = a[0:mid] #In python we can use slicing instead of loop to fill aux arrays.
    c = a[mid:len(a)]
    mergeSort(b)
    mergeSort(c)
    merge(b,c,a)
    

a = [4,1,7,3,5,6,2]
mergeSort(a)
print(a)

    
    
