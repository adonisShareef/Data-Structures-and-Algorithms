def quickSort(arr,l,r):
    if l < r:
        p = partition(arr,l,r)
        quickSort(arr,l,p-1)
        quickSort(arr,p+1,r)
    return arr

def swap(arr,pos1,pos2):
    arr[pos1],arr[pos2] = arr[pos2], arr[pos1]
    return arr

def partition(arr, l,r):
    pivot = arr[r]
    i = l - 1
    for j in range(l,r):
        if arr[j] < pivot:
            i += 1
            swap(arr,i,j)
    swap(arr,i+1,r)
    return i+1

def main():
    l = [2,8,-5,3,0,4,3,4,3,4,-7]
    print(l)
    print(quickSort(l,0,len(l)-1))

if __name__ == '__main__':
    main()