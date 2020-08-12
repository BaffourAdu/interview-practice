"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        if head == None:
          self.length = 0
        else:
          self.length = 1
    
    def print_list(self):
        lists = []
        if self.head == None:
            return
        
        counter = 1
        current = self.head

        while counter <= self.length:
          lists.append(current.value)
          current = current.next
          counter += 1
        
        print(lists)

        
    def append(self, new_element):
        current = self.head
        self.length += 1
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
      """Get an element from a particular position.
      Assume the first position is "1".
      Return "None" if position is not in the list."""
      if position < 1 or position > self.length:
        return None
  
      counter = 1
      current = self.head

      while counter != position:
          current = current.next
          counter += 1
    
      return current
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        counter = 1
        current = self.head
        previous = None
        
        while counter != position:
            previous = current
            current = current.next
            counter += 1
        
        self.length += 1
        previous.next = new_element
        new_element.next = current
    
    def delete(self, value):
        """Delete the first node with a given value."""
        
        if self.head == None:
            return
        
        current = self.head
        previous = None

        self.length -= 1

        if self.head.value == value:
            self.head = current.next
            return

        while current.value != value:
            previous = current
            current = current.next

        previous.next = current.next
        

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

ll.print_list()

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# # Should also print 3
print(ll.get_position(3).value)

# # Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)
ll.print_list()

# Test delete
ll.delete(1)
ll.print_list()

# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)



class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next