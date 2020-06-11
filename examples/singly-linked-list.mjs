import LinkedList from "../data-structures/LinkedList.mjs"

const list = new LinkedList()
list.push(2)
list.push(4)
list.push(8)
list.push(10)
list.push(12)
list.push(10)

list.pop()

list.delete(0)

const printedList = list.printList()
console.log({printedList})
console.log(list.get(3))