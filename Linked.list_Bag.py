class BagNode: 
     
  def __init__(self,data): 
   self.data = data  
   self.next = None 
              
class Bag:

  def __init__(self): 
   self._head = None  
   self._tail = None 
   self.size = 0 
  
  def __len__(self):  
   return self._size   

  def contains(self,item): 
      curNode = self._head 
      while curNode is not None and curNode.data !=item: 
            curNode = curNode.next 
      return curNode is not None  
   
  
  def push(self,item): 
      newNode = BagNode(item) 
      newNode.next = self._head 
      if self._head is None: 
        self._head = newNode 
        self._tail = newNode 
      else: 
        self._head = newNode 
      self.size += 1
  
  def append(self,item): 
      newNode = BagNode(item) 
      if self._head is None: 
         self ._head = newNode 
      else: 
        self._tail.next = newNode 
      self._tail = newNode    
      self.size += 1
  
  def show(self): 
   temp = self._head 
   while temp is not None: 
    print(temp.data)   
    temp = temp.next       
    

  def delete(self,item): 
   temp = self._head 
   before = None 
   while temp is not None and temp.item != item: 
    before = temp 
    temp  = temp.next 
  
  if temp is not None: 
    if temp == self._head: 
      self._head = temp.next 
    else: 
      before.next = temp.next 
    if temp is self._tail: 
      self._tail = prev 
    self.size -= 1  
     
  def iteritems(self): 
      return _BagIterator(self._head) 
    
  class _BagIterator(): 
    def __init__(self,listHead): 
        self._curNode = listHead 
    
    def __iter__(self): 
      return self 
    
    def next(self): 
   if self._curNode is None: 
   else: 
        item = self._curNode.data   
        self._curNode = self._curNode.next
        return item 
   

      