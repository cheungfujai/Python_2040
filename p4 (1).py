class Node(object):
	def __init__ (self, v, n):
		self.value = v
		self.next = n

class LinkedList(object):
	def __init__(self):
		self.firstLink = None

	def add(self, newElement):
		self.firstLink = Node(newElement, self.firstLink)

	def test (self , testValue):
		check = self.firstLink
		while (check):
			if check.value == testValue:
				return True
			check = check.next
		return False

	def remove (self, testValue):
		prev = None
		delete = self.firstLink
		if delete.value == testValue:
		 	self.firstLink = delete.next
		 	return
		while(delete.next):
			if delete.next.value == testValue:
				delete.next = delete.next.next
				return
			#print(delete.next.value)
			delete = delete.next
			

	def len(self): # return size of linked list
		record = self.firstLink
		count = 0
		while (record):
			count = count + 1
			record = record.next
		return count
	def reverse ( self ): # return reverse linked list
		new_list = None
		relinklist = self.firstLink

		tempnow = relinklist	
		tempnext = tempnow.next	
		tempnow.next = None

		tempprev = tempnow		
		tempnow=tempnext
		tempnext= tempnow.next
		
		while(tempnow):
			new_list = Node(tempnow.value, new_list)

			tempnow.next = tempprev

			tempprev = tempnow		
			tempnow=tempnext
			if(tempnow!=None):
				tempnext= tempnow.next
			

			#relinklist = relinklist.next
		self.firstLink=tempprev

		return new_list

	def Lprint ( self ):
		print('Current linked list: ', end='')
		calllist = self.firstLink #reverse()
		#s=""
		while(calllist):
			#s=calllist.value+s
			print(calllist.value, end='')
			calllist = calllist.next
			if calllist != None:
				#s='-->'+s
				print('-->', end='')
		print('-->none')



# l = LinkedList()
# print('list length %d'% (l.len()))
# l.add( 15 )
# print('list length %d'% (l.len()))
# l.add( 20 )
# print('list length %d'% (l.len()))
# print(l.test( 15 ))
# print(l.test( 30 ))
# l.add( 30 )
# print('list length %d'% (l.len()))
# l.reverse()
# l.Lprint()
# l.remove( 15 )
# print('list length %d '% (l.len()))
# l.remove ( 30 )
# print(’list length %d ’% (l.len()))
# l.remove ( 20 )
# print(’list length %d ’% (l.len()))