class MinHeap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }
  getParentIndex(index) {
    return Math.floor((index - 1) / 2);
  }
  getLeftChildIndex(index) {
    return 2 * index + 1;
  }
  getRightChildIndex(index) {
    return 2 * index + 2;
  }
  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }
  bubbleUP(index) {
    let currentIndex = index;
    while (currentIndex > 0) {
      const parentIndex = this.getParentIndex(currentIndex);
      if (this.heap[currentIndex] < this.heap[parentIndex]) {
        this.swap(currentIndex, parentIndex);
        currentIndex = parentIndex;
      } else {
        break;
      }
    }
  }
  sinkDown(index) {
    let currentIndex = index;
    const lastIndex = this.heap.length - 1;

    while (true) {
      const leftChildIndex = this.getLeftChildIndex(currentIndex);
      const rightChildIndex = this.getRightChildIndex(currentIndex);
      let swapIndex = null;
      if (leftChildIndex <= lastIndex) {
        if (this.heap[leftChildIndex] < this.heap[currentIndex]) {
          swapIndex = leftChildIndex;
        }
      }
      if (rightChildIndex <= lastIndex) {
        if (
          swapIndex === null &&
          this.heap[rightChildIndex] < this.heap[currentIndex]
        ) {
          swapIndex = rightChildIndex;
        } else if (
          swapIndex !== null &&
          this.heap[rightChildIndex] < this.heap[swapIndex]
        ) {
          swapIndex = rightChildIndex;
        }
      }
      if (swapIndex === null) break;

      this.swap(currentIndex, swapIndex);
      currentIndex = swapIndex;
    }
  }
  insert(value) {
    this.heap.push(value);
    this.bubbleUP(this.heap.length - 1);
  }
  extractMin() {
    if (this.heap.length === 0) {
      return null;
    }
    if (this.heap.length === 1) {
      return this.heap.pop();
    }
    this.swap(0, this.heap.length - 1);
    const minValue = this.heap.pop();
    this.sinkDown(0);
    return minValue;
  }
  peek() {
    return this.heap.length === 0 ? null : this.heap[0];
  }
}
const minHeap = new MinHeap();
minHeap.insert(30);
minHeap.insert(35);
minHeap.insert(70);
minHeap.insert(12);
minHeap.insert(40);
minHeap.insert(25);
minHeap.insert(50);
minHeap.insert(60);
minHeap.insert(65);
minHeap.insert(6);
console.log(`Heap: ${minHeap.heap}`);
console.log(`First root:${minHeap.peek()}`);

let nextMin;
while (minHeap.size() > 0) {
  nextMin = minHeap.extractMin();
  console.log(`Extracted value: ${nextMin} | New Root: ${minHeap.peek()}`);
}
