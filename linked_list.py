class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedList:
    def __init__(self):
        self.head=None
    
    def insertAtBeginning(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp
        
    def insertAtEnd(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=temp
    
    def traverse(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next
    
    def delFromBeginning(self):
        if self.head==None:
                raise Exception("Empty Linked List")
            else:
                temp=self.head
                self.head=self.head.next
                del temp
                
    def delFromEnd(self):
        if self.head==None:
                raise Exception("Empty Linked List")
            else:
                curr=self.head
                prev=None
                while curr.next!=None:
                    prev=curr
                    curr=curr.next
                prev.next=curr.next
                del curr
            
