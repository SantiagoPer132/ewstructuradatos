
def insercion(A):
    for i in range(len(A)):
        for j in range(i,0,-1):
            if(A[j-1] > A[j]):
                aux=A[j];
                A[j]=A[j-1];
                A[j-1]=aux;
    print (A);

A=[6,5,3,1,8,7,2,4];
print (A);
insercion(A);
import time
print(time.time())
