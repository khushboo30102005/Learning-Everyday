class Stack {
  constructor() {
    this.items = [];
  }
  push(element) {
    this.items.push(element);
  }
  peek() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[this.items.length - 1];
  }
  pop() {
    if (this.isEmpty()) {
      return null;
    }
    const removedElement = this.items.pop();
    return removedElement;
  }
  getSize() {
    return this.items.length;
  }
  isEmpty() {
    return this.items.length === 0;
  }
}

const stack = new Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
console.log(stack);
console.log(`Size: ${stack.getSize()}`);
console.log(`Top Value: ${stack.peek()}`);
const x = stack.pop()
console.log('After remove:');
console.log(`Removed Element: ${x}`);
console.log(stack);
console.log(`Size: ${stack.getSize()}`);
console.log(`Top Value: ${stack.peek()}`);
