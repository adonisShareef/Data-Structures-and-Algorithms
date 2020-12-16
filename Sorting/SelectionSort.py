def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j
        swap(arr, i,min)
    return arr

def swap(arr,pos1,pos2):
    arr[pos1],arr[pos2] = arr[pos2], arr[pos1]
    return arr

def main():
    l = [-4,6,34,5,6,12,98]
    print(l)
    print(selectionSort(l))

if __name__ == '__main__':
    main()