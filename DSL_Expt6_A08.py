#Quick Sort
def partition(A, lb, ub):
    pivot = lb
    i = lb + 1
    j = ub
    while i <= j:

        while i <= ub and A[pivot] >= A[i]:
            i = i + 1

        while A[pivot] < A[j]:
            j = j - 1

        if i < j:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    temp = A[pivot]
    A[pivot] = A[j]
    A[j] = temp
    return j


def Quick_Sort(A, lb, ub):

    if lb < ub:

        mid = partition(A, lb, ub)

        Quick_Sort(A, lb, mid - 1)#recursion

        Quick_Sort(A, mid + 1, ub)#recursion


def Accept_Per(A):#Accepting the list
    A.clear()
    n = int(input("Enter the total Strength of class :"))

    for i in range(n):

        x = float(input("Enter the percentage of %d student :" % (i + 1)))

        A.append(x)


def Display_Per(A):#Displaying percentage of all students

    print("Percentage of students are:")

    for i in range(len(A)):

        print("%.2f" % A[i])



def Display_Per1(A):#Displaying percentage of top five students

    print("Percentage of top five students are:")

    for i in range(len(A)-1,-1,-1):

        print("%.2f" % A[i])



def main():

    A = []

    while True:

        print("\nPress 1. to accept and display :")

        print("\n Press 2. Quick sort :")

        print("\nPress 3. Exit")

        ch = int(input("Enter your choice:"))

        if ch == 3:

            print("End of program")

            quit()

        elif ch == 1:

            Accept_Per(A)

            Display_Per(A)

        elif ch == 2:

            n = len(A)

            Quick_Sort(A, 0, n - 1)
            if(len(A) > 5) :
             print("Top Five Scores : ")
             for i in range(n-1,n-6,-1) :
               print("\t%.2f"%A[i])
            else:    
               Display_Per1(A)


main()