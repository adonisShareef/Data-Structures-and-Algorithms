import BubbleSort
import SelectionSort
import InsertionSort
import ShellSort
import MergeSort
import QuickSort
import random 
import time

def randomList():
    result = []
    rand = random.randint(1,10000)
    for i in range(rand):
        randNum = random.randint(-100,100)
        result.append(randNum)
    return result

def main():
    l = randomList()
    print("List size: ", len(l))
    
 #BubbleSort
    start = time.time()
    BubbleSort.bubbleSort(l)
    end = time.time()
    print("BubbleSort: ", end - start)
    
#InsertionSort
    start = time.time()
    InsertionSort.insertionSort(l)
    end = time.time()
    print("InsertionSort: ", end - start)

#SelectionSort
    start = time.time()
    SelectionSort.selectionSort(l)
    end = time.time()
    print("SelectionSort: ", end - start)

#ShellSort
    start = time.time()
    ShellSort.shellSort(l)
    end = time.time()
    print("ShellSort: ", end - start)

#MergeSort
    start = time.time()
    MergeSort.mergeSort(l)
    end = time.time()
    print("MergeSort: ", end - start)

#QuickSort
    start = time.time()
    QuickSort.quickSort(l,0,len(l)-1)
    end = time.time()
    print("QuickSort: ", end - start)

if __name__ == '__main__':
    main()