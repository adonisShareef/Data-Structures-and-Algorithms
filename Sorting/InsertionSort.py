def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def main():
    l = [50,46,5,7,23,4,5]
    print(l)
    print(insertionSort(l))

if __name__ == '__main__':
    main()