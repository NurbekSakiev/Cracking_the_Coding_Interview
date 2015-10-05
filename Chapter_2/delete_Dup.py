# using Buffer - O(n)
def delete_Dup(head):
	if not head:
		return
	prev = None
	past = set()
	while head != None:
		if head.data in past:
			prev.next = head.next
		else:
			past.add(head)
			prev = head
		head = head.next

# No Buffer Use - O(n^2)
def delete_Dup2(head):
	current = ListNode(head)
	while current != None:
		runner = ListNode(current)
		while runner.next != None:
			if runner.next.data == current.data:
				runner.next = runner.next.next
			else:
				runner = runner.next
		current = current.next
 
