class Node:
	def __init__(self,data,next):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def insertAtBeginning(self,data):
		node = Node(data,self.head)
		self.head = node

	def insertValues(self,data_list):
		for i in data_list:
			node = Node(i,self.head)
			self.head = node	

	def insertAtEnd(self,data):
		if self.head is None:
			self.head = Node(data,None)
			return
		itr = self.head
		while(itr.next):
			itr=itr.next
		itr.next= Node(data,None)

	def getLength(self):
		if self.head is None:
			print("empty LinkedList")
			return
		itr = self.head
		c = 0
		while(itr):
			c+=1
			itr = itr.next
		return(c)		

	def deleteAt(self,index):
		if(index<0 or index>self.getLength()):
			print("enter a valid index value")
			return
		c = 1
		itr = self.head
		while(c<index):
			itr = itr.next
			c+=1
		itr.next=itr.next.next	

	def insertAt(self,index,data):
		if(index<0 or index>self.getLength()):
			print("enter a valid index value")
			return
		c = 1
		itr = self.head
		while(c<index):
			itr = itr.next
			c+=1
		itr.next=Node(data,itr.next)		

	def removeValue(self,data):
		if self.head is None:
			return
		itr = self.head
		if itr.data == data:
			self.head = itr.next
			return
		while(itr):
			if(itr.next.data==data):
				itr.next = itr.next.next
				return
			itr = itr.next	
		else:
			print("not in LinkedList")	

	def insertAfterValue(self,data,value):
		if self.head is None:
			print("empty linkedlist")
		itr = self.head
		if itr.data == value:
			itr.next = Node(data,itr.next)
			return
		while(itr):
			if(itr.data==value):
				itr.next = Node(data,itr.next)
				return
			itr = itr.next	
		else:
			print("no such value in Linkedlist")		

	def print(self):
		if self.head is None:
			print("empty LinkedList")	
			return
		itr = self.head
		llst = ''
		while(itr):
			llst+=str(itr.data)+'-->'
			itr=itr.next
		print(llst)

myLlist = LinkedList()
myLlist.insertValues([1,2,3,4])
myLlist.insertAtEnd('#')
myLlist.insertAt(3,'*')
myLlist.removeValue('*')
myLlist.print()
myLlist.insertAfterValue(0,1)
myLlist.print()


