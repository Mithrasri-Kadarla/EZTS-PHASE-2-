# insertion happens at the rear end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enq(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dq(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
a_queue=Queue()
while True:
    print("enqueue <value>")
    print("dequeue")
    print("quit")
    do=input("what would u like to do?").split()
    print("do:",do)
    print("do[0]:",do[0])
    op=do[0].strip().lower()
    if op=='enqueue':
        a_queue.enq(int(do[1]))
    elif op=='dequeue':
        dequeued=a_queue.dq()
        if dequeued is None:
            print('Queue is empty')
        else:
            print("Dequeued value:",int(dequeued))
    elif op=='quit':
        break
