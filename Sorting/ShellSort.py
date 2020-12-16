def shellSort(arr):
    mid = len(arr)//2
    while mid > 0:
        for i in range(mid,len(arr)):
            temp = arr[i]
            j = i
            while j >= mid and arr[j-mid] > temp:
                arr[j] = arr[j-mid]
                j -= mid
            arr[j] = temp
        mid //= 2
    return arr 

def main():
    l = [55,7,84,55,65,76,23,-456]
    print(l)
    print(shellSort(l))

if __name__ == '__main__':
    main()