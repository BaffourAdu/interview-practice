// Question:
// Given a singly linked list, find middle of the linked list. For example, if given linked list is 1->2->3->4->5 then output should be 3.
// If there are even nodes, then there would be two middle nodes, we need to print second middle element. For example, if given linked list is 1->2->3->4->5->6 then output should be 4.
// (source: https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/)
// Solved by: Baffour Adu Boampong

import LinkedList from "../data-structures/LinkedList.mjs"

function isOdd(value) {
  if (value % 2 !== 1) return false;
  return true
}

function getMiddleElement(list) {
  let middleNode;

  if (list.isEmpty()) return;
  if (list.length < 2) return;
  
  if (isOdd(list.length)) {
    const results = list.length / 2
    const index = Math.floor(results)
    middleNode = list.get(index)
  }
  
  if (!isOdd(list.length)) {
    const index = list.length / 2
    middleNode = list.get(index)
  }
  return middleNode.value
}


const list1 = new LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
const middleElement = getMiddleElement(list1)
console.log(`List 1: ${list1.printList()}`)
console.log(`Middle Element in List 1: ${middleElement} \n\n`)

const list2 = new LinkedList()
list2.push(1)
list2.push(2)
list2.push(3)
list2.push(4)
list2.push(5)
list2.push(6)
const middleElement2 = getMiddleElement(list2)
console.log(`List 2: ${list2.printList()}`)
console.log(`Middle Element in List 2: ${middleElement2} \n\n`)



