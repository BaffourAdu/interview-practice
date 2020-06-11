import Node from "./Node.mjs"

export default class LinkedList {
  constructor() {
    // A reference to the node at the beginning of the list
    this.head = null;
    // A reference to the node at the end of the list
    this.tail = null;
    // Number of nodes in the list
    this.length = 0;
  }

  // Returns a boolean indicating whether the list is empty
  isEmpty() {
    return this.length === 0;
  }

  // Prints out the entire list
  printList () {
    const nodes = [];
    let current = this.head;
    while (current) {
      nodes.push(current.value);
      current = current.next;
    }
    return nodes.join(' -> ');
  }

  // Pushes a value on to the end of the linked list
  push(value) {
    // Create an instance of a new node
    const node = new Node(value);
    // If the list is empty
    if (this.head === null) {
      // Set new node as head
      this.head = node;
      // Set new node as tail
      this.tail = node;
      // Increase number of nodes
      this.length++;
      return node;
    }
    // Set tail node pointer to point to new node
    this.tail.next = node;
    // Set new node as tail
    this.tail = node;
    this.length++;
  }

  // Removes / Pops off the last value from the list
  pop() {
    // Check if list is empty
    if (this.isEmpty()) {
      return null;
    }
    // Get tail node
    const nodeToRemove = this.tail;
    // if there's only one node
    if (this.head === this.tail) {
      // Set head to null
      this.head = null;
      // Set tail to null
      this.tail = null;
      // Decrement number of nodes
      this.length--;
      return nodeToRemove;
    }
    // Get Head node
    let currentNode = this.head;
    // Variable to hold second to last node
    let secondToLastNode;
    // Start at the front and iterate until
    // we find the second to last node
    while (currentNode) {
      if (currentNode.next === this.tail) {
        // Move the pointer for the second to last node
        secondToLastNode = currentNode;
        break;
      }
      currentNode = currentNode.next;
    }
    // Pop off that node
    secondToLastNode.next = null;
    // Move the tail to the second to last node
    this.tail = secondToLastNode;
    this.length--;
    // Initialized to this.tail
    return nodeToRemove;
  }

  // Returns an item from a given index
  get(index) {
    // Index is outside the bounds of the list
    if (index < 0 || index > this.length) {
      return null;
    }
    if (this.isEmpty()) {
      return null;
    }
    if (index === 0 )  {
      return this.head;
    }
    let current = this.head;
    let iterator =  0;
    while (iterator < index) {
      iterator++;
      current = current.next;
    }
    return current;
    }

  // Deletes an item from a given index
  delete(index) {
    // Index is outside the bounds of the list
   if (index < 0 || index > this.length - 1) {
     return null;
   }
 
   if (this.isEmpty()) {
     return null;
   }
 
   if (index === 0) {
     const nodeToDelete = this.head;
     this.head = this.head.next;
     this.length--;
     return nodeToDelete;
   }
 
   let current = this.head;
   let previous;
   let iterator = 0;
 
   while (iterator < index) {
     iterator++;
     previous = current;
     current = current.next;
   }
   const nodeToDelete = current;
   // Re-direct pointer to skip the element we're deleting
   previous.next = current.next;

   if(previous.next === null) {
     this.tail = previous;
   }
 
   this.length--;
 
   return nodeToDelete;
 }
}