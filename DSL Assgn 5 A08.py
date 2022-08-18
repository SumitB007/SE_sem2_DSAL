def Accept(p):
    p.clear()
    n=int(input("Enter the total number of students : "))
    for i in range(n):
        x=float(input("Enter the percentage of Fe students : "))
        p.append(x)

def Display(p):
    print("FE students percentage :")
    for i in range(len(p)):
        print("%.2f"%p[i])


def Topfive(p):
    print("Top five FE students percentage :")
    for i in range(len(p)-1,len(p)-6,-1):
        print("%.2f"%p[i])


def selection_sort(p):
    n=len(p)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if(p[j]<p[min_index]):
                min_index=j
        temp=p[i]
        p[i]=p[min_index]
        p[min_index]=temp

def bubble_sort(p):
    n=len(p)
    for i in range(1,n):
        for j in range(n-i):
            if(p[j]>p[j+1]):
                temp=p[j]
                p[j]=p[j+1]
                p[j+1]=temp

def main():
    p=[]
    while True:
        print("\n Press 1.Accept students percentage")
        print("\n Press 2.Selection sort")
        print("\n Press 3.Bubble sort")
        print("\n Press 4.Exit")
        ch=int(input("Enter the choice : "))
        if(ch==1):
           Accept(p)
           Display(p)
        elif(ch==2):
           selection_sort(p)
           if(len(p)>5):
             Topfive(p)
           else:
             Display(p)
        elif(ch==3):
           bubble_sort(p)
           if(len(p)>5):
            Topfive(p)
           else:
               Display(p) 
        else:
            print("End program")
            break

main()
