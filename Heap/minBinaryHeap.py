class minBinaryHeap:
    def __init__(self):
        self.heaplist = []
        self.length = 0
    #main methods
    def add(self, k):
        """
        Inserts a new item into the heap and calls percolateUp to maintain hepa property on insertion
        """
        self.heaplist.append(k)
        self.length += 1
        self.percolateUp(self.length-1)

    def remove(self):
        """
        Send root to the end of list
        percolate down to keep heap property
        return the pop of list 
        """
        self.heaplist[0], self.heaplist[-1] = self.heaplist[-1], self.heaplist[0]
        result = self.heaplist.pop()
        self.length -= 1
        #percolate after taking out the min value
        self.percolateDown(0)
        return result

    def min(self):
        """
        min in min heap is the root
        """
        return self.heaplist[0]

    def size(self):
        return len(self.heaplist)

    #helper methods
    def percolateUp(self,i):
        """
        Moves a new item up in order to maintain the heap property

        parent: i - 1 // 2 
        i = i - 1 becuase zero index
        """
        while (i - 1) // 2 >= 0:
            if self.heaplist[i] < self.heaplist[(i - 1)// 2]:
                #swap 
                self.heaplist[i], self.heaplist[(i - 1) // 2] = self.heaplist[ (i - 1) // 2], self.heaplist[i]
            #now move to the parent position
            i = (i - 1) // 2

    def percolateDown(self, i):
        """
        Moves a new item up in order to maintain the heap property
        """
        while i * 2 + 1 < self.length:
            childToSwap = self.minChild(i) 
            if self.heaplist[i] > self.heaplist[childToSwap]:
                #swap 
                self.heaplist[i], self.heaplist[childToSwap] = self.heaplist[childToSwap], self.heaplist[i]
            #now move to the parent position
            i = childToSwap

    def minChild(self, i):
        """
        Finds the min child of the parent

        lChild = i * 2 + 1
        rChild = i * 2 + 2
        """
        lChild = i * 2 + 1
        rChild = i * 2 + 2
        if rChild >= self.length: return lChild
        else:
            if self.heaplist[lChild] < self.heaplist[rChild]: return lChild
            else: return rChild


def main():
    heap = minBinaryHeap()
    heap.add(5)
    heap.add(2)
    heap.add(3)
    print(heap.remove())
    print(heap.min())
    print(heap.heaplist)
   

if __name__ == '__main__':
    main()