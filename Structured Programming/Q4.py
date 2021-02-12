def createTupledList():
    l=[]
    print("Add an element for the tuple ? y/n: ")
    ch=str(input())
    while(ch=="y"):
        print("Enter the tuple element : ")
        i=input()
        l.append(tuple(i.split(",")))
        print("Add an element for the tuple ?y/n:  ")
        ch=str(input())
    return l
tuplist = createTupledList()
def sort_tuple(lst):
    return sorted(lst,key=lambda x:x[len(x)-1])
print(sort_tuple(tuplist))
