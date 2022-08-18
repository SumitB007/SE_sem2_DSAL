def addition_matrix(M1,M2,M3,r,c) : #Function for addition
    for i in range(r) :
      A = []
      for j in range(c):
        A.append(M1[i][j] + M2[i][j])
      M3.append(A)


def substraction_matrix(M1,M2,M3,r,c) : #Function for subtraction
   for i in range(r) :
     A = []
     for j in range(c):
       A.append(M1[i][j] - M2[i][j])
     M3.append(A)      


def multiplication_matrix(M1,M2,M3,r1,c1,c2) : #Function for Multiplication
   for i in range(r1) :
      A = []
      for j in range(c2) :
        sum = 0
        for k in range(c1) :
           sum = sum + (M1[i][k] * M2[k][j])
        A.append(sum)
      M3.append(A)  


def find_transpose_matrix(M,r,c,T) : #Function for Transpose
   for i in range(c):
     A = []
     for j in range(r):
       A.append(M[j][i])
     T.append(A) 

def display(M,r,c):  #Function for displaying matrix
    for i in range(r):
        print("\t\t",end=' ')
        for j in range(c):
            print("%4d"%M[i][j],end=' ')
        print(" ")    


def accept_matrix(M):#Function for accepting matrix
    print("Enter the rows and columns of the matrices : ")
    r=int(input("\t row ="))
    c=int(input("\t column ="))
    print("Enter the elements in matrix : \n")
    for i in range(r):
        A = []
        for j in range(c):
            A.append(int(input()))
        M.append(A)


def options():#Choices
    print("1: Addition")
    print("2: Subtraction\t")
    print("3: Multiplication\t")
    print("4: Transpose of 1st Matrix(M1)\t")
    print("5: Transpose of 2nd Matrix(M2)\t")
    print("6: Exit\t")
    
    

def main():
    M1=[]
    M2=[]
    M3=[]
    T1=[]
    accept_matrix(M1)
    r1=len(M1)
    c1=len(M1[0])
    display(M1,r1,c1)
    accept_matrix(M2)
    r2=len(M2)
    c2=len(M2[0])
    display(M2,r2,c2)
    while(True):
        options()
        choice=int(input("Enter your choice : "))
        if(choice==1):
         print("Addition of two matrices : \n")
         if(r1==r2 and c1==c2):
           addition_matrix(M1,M2,M3,r1,c1)
           display(M3,r1,c1)
           M3.clear()
         else:
          print("Addition is not possible")
         
    
        elif(choice==2):     
          print("Subtraction of two matrices : \n")
          if(r1==r2 and c1==c2):
            substraction_matrix(M1,M2,M3,r1,c1)
            display(M3,r1,c1)
            M3.clear()
          else:
            print("Subtraction is not possible")
         

        elif(choice==3):  
          print("Multiplication of two matrices :\n")
          if(c1==r2):
            multiplication_matrix(M1,M2,M3,r1,c1,c2)
            display(M3,r1,c1)
            M3.clear()
          else:
            print("Multiplication not possible(Columns not equal to rows)")
           

        elif(choice==4):  
           print("Transverse of matrix M1 : \n")
           find_transpose_matrix(M1,r1,c1,T1)
           display(T1,r1,c1)
           T1.clear()
           
        elif(choice==5):   
           print("Transverse of matrix M2 : \n")
           find_transpose_matrix(M2,r2,c2,T1)
           display(T1,r2,c2)
           T1.clear()
         

        else:
           print("Exiting")
           break
        

       
main()               
                
