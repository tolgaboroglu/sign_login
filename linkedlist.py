class ListNode: 
    def __init__(self,data): 
        self.data=data 
        self.next=None  
        
#Searching 
curNode = head 
while curNode is not None and  
      curNode.data != target: 
          curNode=curNode.next 
        
found = curNode is not None 

#add new values 
newNode = ListNode(neItem) 
newNode.next = head 
head =newNode 

#given the head reference,we can target from the liked list 

predNode = None 
curNode = head 
while curNode is not None and curNode.data != target: 
    predNode = curNode 
    curNode = curNode.next 
    
    if curNode is not None : 
        if curNode is head : 
            head = curNode.next 
        else : 
            predNode.next = curNode.next 
