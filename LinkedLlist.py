class Node:
    #Class for creating a Node which contains the data and the next address 
    #If this is the first node hence the next value will be none
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    #Creating a class for LinkedList which contains various functions 
    def __init__(self):
        #head of the Linked List
        self.head = None
    
    def insert_at_start(self,data):
        #Function for inserting at the starting 
        new_node = Node(data,self.head) #creating a new node 
        self.head = new_node #now head will point to newly created node
    def insert_at_end(self,data):
        if self.head is None: #which means there is nothing in the Linked List
            new_node = Node(data,self.head) #creating a new node 
            self.head = new_node #now head will point to newly created node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data,None)
    def print(self): #funtion for prinitng the nodes and the datas
        element = ''
        if self.head is None:
            element += 'Null'
        temp = self.head
        while temp: #looping through the head to check the next element 
            element += str(temp.data)+ '--->'
            temp = temp.next
        print(element)

            
if __name__ == '__main__':
    ll = LinkedList()  
    ll.insert_at_start(2)
    ll.insert_at_start(3)
    ll.insert_at_start(4)
    ll.insert_at_end(5)
    ll.insert_at_end(9)
    ll.print()

