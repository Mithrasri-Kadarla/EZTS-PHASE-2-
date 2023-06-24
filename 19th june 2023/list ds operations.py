l=list(map(int,input().split()))
x=int(input("Enter element to insert:"))
l.append(x)
print("Inserted:",l)
y=int(input("Enter element to remove:"))
if y in l:
    l.remove(y)
    print("Removed element:",l)
else:
    print("No element")
l.sort()
print("Sorted array:",l)
z=int(input("Enter element to search:"))
if z in l:
    print("Found")
else:
    print("Not Found")
