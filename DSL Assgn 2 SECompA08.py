def average(l):#Avg Score
    sum = 0
    cnt = 0
    for i in range(len(l)):
        if l[i] != -1:
            sum += l[i]
            cnt += 1

    avg = sum / cnt
    print("Total Marks are : ", sum)
    print("Average Marks are : %.3f"%(avg))


def Maximum(l):#Highest Score
    Max = l[0]
    for i in range(len(l)):
        if l[i] > Max:
            Max = l[i]
    return (Max)


def Minimum(l):#Lowest Score, Use of array and for loop 
    for i in range(len(l)):
        if l[i] != -1:
            Min = l[i]
            break

    for j in range(i + 1, len(l)):
        if l[j] != -1 and l[j] < Min:
            Min = l[j]
    return (Min)


def absentCnt(l):#No. of absent students
    cnt = 0
    for i in range(len(l)):
        if l[i] == -1:
            cnt += 1
    return (cnt)


def maxFrequency(l):#Marks with highest frequency
    i = 0
    count = 0
    print(" Marks ----> frequency count ")
    for ele in l:
        if l.index(ele) == i:
            print(ele, "---->", l.count(ele))
            if l.count(ele) > count:
                count = l.count(ele)
                mark = ele
        i += 1
    return (mark, count)

def main():
 print("Enter the no of students and their marks accordingly\n")
 marksInFDS = []
 noStudents = int(input("Enter total number of students : "))
 for i in range(noStudents):
    marks = int(input("Enter marks of Student no. " + str(i + 1) + " : "))
    marksInFDS.append(marks)
 
 flag = 1
 while flag == 1:
    print("/          MENU        /")
    print("1. The average score of class ")
    print("2. Highest score and lowest score of class ")
    print("3. Count of students who were absent for the test ")
    print("4. Display mark with highest frequency ")
    print("5. Exit ")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        average(marksInFDS)

    elif choice == 2:
        print("Highest score in the class is : ", Maximum(marksInFDS))
        print("Lowest score in the class is : ", Minimum(marksInFDS))

    elif choice == 3:
        print("Count of students who were absent for the test is : ", absentCnt(marksInFDS))

    elif choice == 4:
        mark, count = maxFrequency(marksInFDS)
        print("Highest frequency of marks {0} is {1} ".format(mark, count))
    elif choice == 5:
        print("Program ended")
        flag=0
    else:
        print("Wrong choice")
        


main()
#END