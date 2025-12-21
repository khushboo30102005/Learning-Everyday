class Node {
  constructor(data, prev = null, next = null) {
    this.data = data;
    this.prev = prev;
    this.next = next;
  }
}
class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }
  append(data) {
    const newNode = new Node(data, this.tail);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.size++;
  }
  prepend(data) {
    const newNode = new Node(data, null, this.head);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.head.prev = newNode;
      this.head = newNode;
    }
    this.size++;
  }
  insertAt(data, index) {
    if (index < 0 || index > this.size) {
      console.error('Invalid Index');
      return false;
    }
    if (index === 0) {
      this.prepend(data);
      return true;
    }
    if (index === this.size) {
      this.append(data);
      return true;
    }
    let current = this.head;
    let count = 0;
    while (count < index) {
      current = current.next;
      count++;
    }
    const newNode = new Node(data, current.prev, current);
    current.prev.next = newNode;
    current.prev = newNode;
    this.size++;
    return true;
  }
  removeAt(index) {
    if (index < 0 || index >= this.size) {
      console.error('Invalid Index');
      return null;
    }
    let current;
    let removedData;
    if (index === 0) {
      removedData = this.head.data;
      this.head = this.head.next;
      if (this.head) {
        this.head.prev = null;
      } else {
        this.tail = null;
      }
    } else if (index === this.size - 1) {
      current = this.tail;
      removedData = current.data;
      this.tail = current.prev;
      this.tail.next = null;
    } else {
      let count = 0;
      current = this.head;
      while (count < index) {
        current = current.next;
        count++;
      }
      removedData = current.data;
      current.prev.next = current.next;
      current.next.prev = current.prev;
    }
    this.size--;
    return removedData;
  }
  isEmpty() {
    return this.size === 0;
  }
  getSize() {
    return this.size;
  }
  printListForward() {
    let current = this.head;
    let result = '';
    while (current) {
      result += current.data + ' <-> ';
      current = current.next;
    }
    result += ' null ';
    console.log(result);
  }
  printListBackward() {
    let current = this.tail;
    let result = '';
    while (current) {
      result += current.data + ' <-> ';
      current = current.prev;
    }
    result += ' null ';
    console.log(result);
  }
}

const list = new DoublyLinkedList();
list.append(10);
list.append(20);
list.append(30);
list.append(40);
list.prepend(50);
list.insertAt(60, 2);
list.printListForward();
list.printListBackward();
