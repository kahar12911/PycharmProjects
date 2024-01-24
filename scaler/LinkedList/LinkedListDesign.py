
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None



def insertNodeAtEnd(data):
    new_node = Node(data)
    if ll.head is None:
        ll.head=new_node
    else:
        p = ll.head
        while p.next != None:
            p=p.next 
        p.next=new_node
    return ll.head

def insertNodeAtBeginning(data):
    new_node = Node(data)
    new_node.next = ll.head
    ll.head = new_node
    return ll.head

def inserNodeAtPosition(data,position):
    new_node = Node(data)
    if position==0:
        insertNodeAtBeginning(data)
    # elif position>len(ll):
    #     print("Position out of range")
    else:
        current = ll.head
        for _ in range(position-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

# print LL   
def printLL():
    if ll.head == None:
        return 0
    else:
        temp = ll.head
        while temp.next:
            print(temp.data, "->" , end=" ")
            temp = temp.next
        print(temp.data, end=" ")
        print("")
        
def deleteNodeAtEnd():
    if ll.head is not None:
        if ll.head.next is None:
            ll.head = None
        else:
            last = ll.head
            current = ll.head.next
            while current.next:
                last = current
                current = current.next
            last.next = None

def deleteNodeAtBeginning():
    if ll.head is not None:
        ll.head = ll.head.next


def deleteNodeAtPosition(position):
    if ll.head==None:
        return
    elif position<1 : #or position > getLength():
        print("Invalid Position")
    elif position == 1:
        p = ll.head
        ll.head = ll.head.next
        p.next = None
    else:
        i = 1
        p = ll.head
        while i < position and p.next:
            q=p
            p = p.next 
            i += 1
        if p.next:
            p.next = p.next.next
        else:
            q.next = None


def deleteMiddleNode():
    if not ll.head: return None
    p = slow = fast = ll.head
    i=0
    temp=None
    while fast and fast.next:
        p=slow
        slow = slow.next
        fast = fast.next.next
    p.next=slow.next
    
def reverseLL():
    #head=A
    if not ll.head:
        return
    if not ll.head.next:
        return ll.head
    if not ll.head.next.next:
        p=ll.head
        q=p.next
        p.next=None
        q.next=p
        ll.head=q
        return ll.head
    else:
        p=ll.head
        q=p.next
        r=q.next
        #print(p.data,q.data,r.data)
        p.next=None
        while q:
            
            q.next=p 
            p=q
            ll.head=q
            q=r 
            if r: r=r.next
            #print(p.data,p.next.data,q.data,r.data)
        return ll.head
    
    
ll=LinkedList()
# insertNode(1)
# insertNode(2)
# insertNode(3)
# #printLL()
# insertNode(4)
# #printLL()
# #delete_node(4)
# insertNode(5)
# printLL()
A=[97,63,89,34,82,95,4,70,14,41,38,83,49,32,68,56,99,52,33,54]
for i in range(len(A)):
    insertNodeAtEnd(A[i])
printLL()
reverseLL()
printLL() 
        
    
        