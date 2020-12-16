def bubbleSort(arr):
    sorted = False
    lastUnsorted = len(arr)-1
    while not sorted:
        sorted = True
        for i in range(lastUnsorted):
            if arr[i] > arr[i+1]:
                swap(arr,i,i+1)
                sorted = False
        lastUnsorted -= 1
    return arr

def swap(arr,pos1,pos2):
    arr[pos1],arr[pos2] = arr[pos2], arr[pos1]
    return arr

def main():
    l = [3,4,3,4,6,79,12]
    print(l)
    print(bubbleSort(l))

if __name__ == '__main__':
    main()
    