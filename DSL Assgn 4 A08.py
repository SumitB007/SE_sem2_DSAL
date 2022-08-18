def accept(A):
    n=int(input("\n Enter total nuber of friends:"))
    print("\n Enter your friends information: ")
    for i in range(n):
        print("\n Enter friend %d information :"%(i+1))
        name=input("\n Enter the name: ")
        mob=input("\n Enter mobile number: ")
        X=[name,mob]
        A.append(X)
    return n

def display(A,n):
    if(n==0):
        print("\n No record found")
    else:
        print("\n Your friends information is : ")
        for i in range(n):
            print("\tFriend no. %d : %s %s"%((i+1),A[i][0],A[i][1]))     


def iteractive_Binary(A,n,s):
    lb=0
    ub=n-1
    while(lb<=ub):
        mid=int((lb+ub)/2)
        if(s==A[mid][0]):
            return mid
        else:
            if(s<A[mid][0]):
                ub=mid-1
            else:
                lb=mid+1

    return -1

def recursive_Binary(A,lb,ub,s):
    if(lb<=ub):
        mid=int((lb+ub)/2)
        if(s==A[mid][0]):
            return mid
        else:
            if(s<A[mid][0]):
                return recursive_Binary(A,lb,mid-1,s)
            else:
                return recursive_Binary(A,mid+1,ub,s)
    else:  
      return -1

    
def Fibonacci(A,n,s):
    f1=0
    f2=1
    f3=f1+f2
    offset=-1
    while(f3<=n):
        f1=f2
        f2=f3
        f3=f1+f2
    while(f3>=0):
        i=min(offset+f1,n-1)
        if(A[i][0]==s):
            return i

        else:
            if(s<A[i][0]):
                f3=f1
                f2=f2-f1
                f1=f3-f2

            else:
                f3=f2
                f2=f1
                f1=f3-f2
                offset=i
    if(f2 and A[n-1] == s):
        return n-1               

    return -1


def insert(A,n,s):
    mob=input("\nEnter your friends mobile number : ")
    X=[s,mob]
    A.append(X)
    j=n-1
    while(j>=0):
        if(A[j][0]<=s):
            break
        else:
            A[j+1]=A[j]
        j=j-1
    A[j+1]=X
    display(A,n+1)



def main():
    A=[]
    while True:
        print("\nPress 1.Accept friends information :")
        print("\nPress 2.Iteractive Binary Search :")
        print("\nPress 3.Recursive Bunary Search :")
        print("\nPress 4.Fibonacci Search :")
        print("\nPress 5.Display Record :")
        print("\nPress 6.Exit :")
        ch=int(input("\n Enter your choice :"))
        if(ch==1):
            n=accept(A)
            display(A,n)
        elif(ch==2):
            s=input("\n Enter the friend you want to search: ")
            f=iteractive_Binary(A,n,s)
            if(f==-1):
                print("\nFriend id not present")
                insert(A,n,s)
                n=n+1
            else:
                print("Friend id present")

        elif(ch==3):
            s=input("\n Enter the friend you want to search: ")
            f=recursive_Binary(A,0,n-1,s)
            if(f==-1):
                print("\nFriend id not present")
                insert(A,n,s)
                n=n+1
            else:
                print("\nFriend id present")
               
        elif(ch==4):
            s=input("\n Enter the friend you want to search: ")
            f=Fibonacci(A,n,s)
            if(f==-1):
                print("\nFriend id not present")
                insert(A,n,s)
                n=n+1
            else:
                print("\nFriend id present")

        elif(ch==5):
            display(A,n)

        elif(ch==6):
            break

main()
