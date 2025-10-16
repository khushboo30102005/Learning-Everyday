class Queue{
  constructor() {
    this.item = []
  }
  enqueue(ele){
    this.item.push(ele)
  }
  dequeue(){
    if(this.isEmpty()){
      return null
    }
    const removedElement = this.item.shift()
    return removedElement
  }
  getFront(){
      if(this.isEmpty()){
      return null
    }
    return this.item[0]
  }
  getRear(){
      if(this.isEmpty()){
      return null
    }
    return this.item[this.item.length-1]
  }
  isEmpty(){
   return this.item.length === 0
  }
  getSize(){
    return this.item.length
  }
}
const queue = new Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

console.log(`Size: ${queue.getSize()}`);
console.log(queue.item);
console.log(`Rear: ${queue.getRear()}  Front: ${queue.getFront()}`);

queue.dequeue()
console.log(`Size: ${queue.getSize()}`);
console.log(queue.item);
console.log(`Rear: ${queue.getRear()}  Front: ${queue.getFront()}`);