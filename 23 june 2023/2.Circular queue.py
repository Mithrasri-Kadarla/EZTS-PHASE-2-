#insert:rear+1-->we add new person at the end of the circular queue
#delete:front=front+1-->FIFO
class CircularQueue():
    def __init__(self,size):
        #initializing the class
        self.size=size
        #can use self.queue=[None]*size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enq(self,data):
        #condition q is full
        if((self.rear+1)%self.size==self.front):
            print("Queue is Full\n")
        #condition for q is empty
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
            #always add element at rear place
        else:
            #next position of rear
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dq(self):
        if(self.front==-1):
            #condition for empty q
            print("Queue is empty\n")
        #condition for only one element
        elif (self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        #condition for empty q
        if (self.front==-1):
            print("Queue is Empty")
        elif(self.rear>=self.front):
            print("Elements in the circular queue",end='')
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=' ')
            print()
        else:
            print("Elements in the circular queue are:",end=' ')
            for i in range(self.front,self.size):
                print(self.queue[i],end=' ')
            for i in range(0,self.rear+1):
                print(self.queue[i],end=' ')
            print()
        if((self.rear+1)%self.size==self.front):
            print('Queue is Full')
ob=CircularQueue(5)
ob.enq(14)
ob.enq(22)
ob.enq(13)
ob.enq(-6)
ob.display()
print("Deleted Value:",ob.dq())
print("Deleted Value:",ob.dq())
ob.display()
ob.enq(9)
ob.enq(20)
ob.enq(5)
ob.display()
ob.enq(100)
