class Deque {
  constructor() {
    this.items = {};
    this.head = 0;
    this.tail = 0;
  }
  addHead(element) {
    this.head--;
    this.items[this.head] = element;
  }
  addTail(element) {
    this.items[this.tail] = element;
    this.tail++;
  }
  removeHead() {
    if (this.isEmpty()) {
      return undefined;
    }
    const result = this.items[this.head];
    delete this.items[this.head];
    this.head++;
    if (this.isEmpty()) {
      this.head = 0;
      this.tail = 0;
    }
    return result;
  }
  removeTail() {
    if (this.isEmpty()) {
      return undefined;
    }
    this.tail--;
    const result = this.items[this.tail];
    delete this.items[this.tail];
    if (this.isEmpty()) {
      this.head = 0;
      this.tail = 0;
    }
    return result;
  }
  peekHead() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.head];
  }
  peekTail() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.tail - 1];
  }
  isEmpty() {
    return (this.head === this.tail);
  }
  size() {
    return this.tail - this.head;
  }
  print() {
    if (this.isEmpty()) {
      console.log('Deque is empty');
      return;
    }
    let output = "";
    for (let i = this.head; i < this.tail; i++) {
      output += this.items[i] + (i < this.tail - 1 ? ' <-> ' : '');
    }
    console.log(output);
  }
}

let d = new Deque();

d.addTail(10)
d.addTail(20)
d.addTail(30)
d.print()
d.addHead(40)
d.addHead(50)
d.print()
console.log(`Size of Deque: ${d.size()}`);
d.removeHead()
d.print()
d.removeTail()
d.print()
console.log(`Size of Deque: ${d.size()}`);