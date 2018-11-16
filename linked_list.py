from typing import Optional

# single linked list
class Node:
	def __init__(self,data,next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return self.data

# reverse the single linked list
def reverse(head:Node):
	reverse_head = None
	current = head

	while current is not None:
		reverse_head,current,reverse_head.next = current,current.next,reverse_head
	return reverse_head

# detect whether there is a circle in the single linked list or not
def check_circle(head: Node):
	fast = head
	slow = head
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			return True
	return False

# merge two linked lists which are sorted already
def merge_sorted_list(l1:Node, l2:Node):
	p1,p2 = l1,l2

	fake_head = Node(0)
	current = fake_head
	while p1 and p2:
		if p1.data<=p2.data:
			current.next = p1
			p1 = p1.next
		else:
			current.next = p2
			p2 = p2.next
		current = current.next
	print(p1,p2,current)
	current.next = p1 if p1 else p2

	return fake_head.next

# remove one node in position of n
def remove_nth_node(head:Node,n:int):
	fast = head
	count = 0
	while count<n and fast:
		fast = fast.next
		count+=1
	slow = head
	while fast.next:
		slow,fast = slow.next,fast.next
	slow.next = slow.next.next	
	return head

# print all nodes in linked list
def print_all(p):
	print('phead:',end='')
	while p is not None:
		print(p.data,end='->')
		p = p.next

	print('None')

if __name__ == '__main__':
	n1 = Node('1')
	n2 = Node('3')
	n3 = Node('7')
	n4 = Node('34')
	n5 = Node('54')
	n6 = Node('77')
	n1.next,n2.next,n3.next,n4.next,n5.next,n6.next = n2,n3,n4,n5,n6,None
	m1 = Node('4')
	m2 = Node('13')
	m3 = Node('27')
	m4 = Node('44')
	m5 = Node('57')
	m1.next,m2.next,m3.next,m4.next,m5.next = m2,m3,m4,m5,None
	# m6 = Node('177')

	p = merge_sorted_list(m1,n1)
	# p = remove_nth_node(n1,2)
	print_all(p)


