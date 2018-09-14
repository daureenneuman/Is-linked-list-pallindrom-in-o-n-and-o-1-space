def mergeTwoLinkedLists(l1, l2):
    current1=l1
    current2=l2
    if not l1 and not l2:
        return []
    elif not l1:
        return l2
    elif not l2:
        return l1
    else:
        if l1.value<= l2.value:
            current=current1
            current1=current1.next
            head=l1
        else:
            current=current2
            current2=current2.next
            head=l2
        while current1 and current2:
            if current1.value<=current2.value:
                current.next=current1
                current=current.next
                current1=current1.next
            else:
                current.next=current2
                current=current.next
                current2=current2.next
        if not current2:
            current.next=current1
            return head
        else:
            current.next=current2
            return head
        