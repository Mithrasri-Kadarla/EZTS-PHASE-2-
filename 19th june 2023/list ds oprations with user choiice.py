def fun():
    l=list(map(int,input().split()))
    def fun1():
        print("1.Insert")
        print("2.Delete")
        print("3.Search")
        print("4.Sort")
        s=int(input("Enter Your choice:"))
        if(s==1):
            x=int(input("Enter element to insert:"))
            l.append(x)
            print("Inserted:",l)
        elif(s==2):
            y=int(input("Enter element to remove:"))
            if y in l:
                l.remove(y)
                print("Removed element:",l)
            else:
                print("No element")
        elif(s==3):
            l.sort()
            print("Sorted array:",l)
        elif(s==4):
            z=int(input("Enter element to search:"))
            if z in l:
                print("Found")
            else:
                print("Not Found")
        else:
            print("Give Correct choice")
    fun1()
fun()
