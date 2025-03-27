class Node:
    """
        An object for storing a single  node of a linked list. Models the data and the next node of the linked list
    """

    next_node = None
    def __init__(self , data):
        self.data = data

    def __repr__(self): #this gives a representation of the object when it is printed not just some vagues format like <__main__.Node object at 0x7d2b937a4980>
        return f"Node Data: {self.data}" # this works

class LinkedList:
    """
        Singly linked list
    """

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head:
            return True
        else: 
            return False
        
    def size(self):
        """
            return the length of the list
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def __repr__(self):
        """
            lists the nodes in the list IN a list
        """
        nodes = [] #list of all the node representations
        current = self.head
        while current:
            if current is self.head:
                nodes.append(f"[Head node is {current.data}]")
            elif not current.next_node:
                nodes.append(f"[Tail node is {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            current = current.next_node
        return "-->".join(nodes)
                
    def search(self , key):
        """
            searching for the fisrt node containing the given data
        """
        current= self.head
        count = 0
        while current:
            count += 1
            if current.data == key:
                return f"Item is present in node {count}"
            else:
                current = current.next_node
        return f"Item not found in list"
        



    def append(self, node):
        """
            adds a node to the node to the end of the list
        """
        current = self.head
        end = None
        while current.next_node:
            end = current.next_node
            current = current.next_node

        end.next_node = node
        
    def prepend(self, node):
        """
            adds an already existing node as the head of the linked list
        """
        current = self.head
        self.head = node
        self.head.next_node = current 

    def delete(self , node):
        """
            removes a node form a linked list
        """
        prev = None
        post = None
        current = self.head
        if isinstance(node , Node):
            #if the head is the node to be removed 
            if current == node:
                post = node.next_node
                self.head = post
                current.next_node = None
            else:
                while current != node:
                    if current.next_node == node:
                        prev = current
                        post = node.next_node
                        prev.next_node = post
                        node.next_node = None
                        break
                    else:
                        current = current.next_node    

l = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
l.head = n1
n1.next_node = n2
n2.next_node = n3
n3.next_node = n4
# print(l.size())

# l.delete(n4)
# print(l.size())
# print(l.head)
# print(l.size())
print(l.__repr__())

print(l.search(20))

        