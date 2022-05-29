#n: number of samples
import numpy as np
from numpy import random

#κωδικοποιηση: LE=1, CE=2, RE=3, LW=-1,CW=-2,RW=-3

def initial_pop(tableA):

    ini_values=[1,2,3]
    n=tableA.shape[0]       #number of rows=number of samples
    tableA[:,0]=np.random.choice(ini_values,n)     #fill with samples at t=0,(uniform distribution over all entries of ini_values at t=0)


def repopulate(tableA,t):

    #set value for position
    for row in range(len(A)):
        x = random.rand()       #generate random number(0,1) to define wind value at timestep t
        if tableA[row,t-1]==1:   #LE
            tableA[row,t]=1
            if x>0.7:
                tableA[row,t]=-tableA[row,t]   #W

        elif tableA[row,t-1]==-1:  #LW
            tableA[row,t]=np.random.choice([1,2])
            if x>0.7:
                tableA[row,t]=-tableA[row,t]   #E

        elif tableA[row,t-1]==2:   #CE
            tableA[row,t]=np.random.choice([1,2])
            if x>0.7:
                tableA[row,t]=-tableA[row,t]    #W

        elif tableA[row,t-1]==-2:  #CW
            tableA[row,t]=np.random.choice([2,3])
            if x>0.7:
                tableA[row,t]=-tableA[row,t]  #E

        elif tableA[row,t-1]==3:   #RE
            tableA[row,t]=np.random.choice([2,3])
            if x>0.7:
                tableA[row,t]=-tableA[row,t]    #W

        elif tableA[row,t-1]==-3: #RW
            tableA[row,t]=3
            if x>0.7:
                tableA[row,t]=-tableA[row,t]  #E

def weighted(tableA,t,e):
    w=np.zeros(n)
    #με np.where?
    if e[t]=="C":
        w[:]=np.where(np.absolute(tableA[:,t])==1,0.2,np.where(np.absolute(tableA[:,t])==2,0.4,0.2))
    elif  e[t]=="L":
        w[:]=np.where(np.absolute(tableA[:,t])==1,0.7,np.where(np.absolute(tableA[:,t])==2,0.3,0.1))
    return w


def resample(sum,w,tableA,tableB,t):

    for row in range(len(A)):
        # print("iteration: ",row)
        # x = random.uniform(0, sum)
        x = random.rand()    #generate random number(0,1)
        # print("random number is: ",x)
        prod=x*sum
        # print(prod)
        var=0
        valDetected=False
        for j in range(len(w)):
            var=var+w[j]
            # print(" var is:",var)
            if var>prod:
                # print("var is greater than prod",var)
                # print(" j is: ",j)
                tableB[row,t]=np.copy(tableA[j,t])
                valDetected=True
                break
        if valDetected==False:   #in order to avoid zero values in case var<prod
            tableB[row,t]=np.copy(tableA[row,t])

        # print("j is ",j)
        # tableB[row,t]=tableA[j,t].copy()


    # print(tableB)
    tableA[:,t]=np.copy(tableB[:,t])      #copy back new samples for timestep t






#test function
if __name__ == "__main__":
#κωδικοποιηση: LE=1, CE=2, RE=3, LW=-1,CW=-2,RW=-3

    n=1000 #number of samples (slow performance with 10000 samples)
    timesteps=5  #number of timesteps
    e = np.array(["","C", "L", "L"], dtype="object")   #observations
    A=np.zeros((n,timesteps),dtype=int)        #initalize tables
    B=np.zeros((n,timesteps),dtype=int)
    initial_pop(A)        #fill with initial samples (t=0)
    # print(A,e)
    # print(A.shape)
    for t in range(1,timesteps-1):  #for each t
        # print(" t is: ",t)
        repopulate(A,t)
        # print(A)
        w=weighted(A,t,e)
        # print(w)
        sum=np.sum(w)
        # print(" sum is: ",sum)
        resample(sum,w,A,B,t)
        # print(" new A is: ",A)

    repopulate(A,timesteps-1)    #for t=4 there is no observation
    # print("final A is:",A)

    #calculate propabilities

    countL = np.count_nonzero(np.logical_or(A==1,A==-1),axis = 0)    #Left occurences
    countC = np.count_nonzero(np.logical_or(A==2,A==-2),axis=0)    #Center
    countR = np.count_nonzero(np.logical_or(A==3,A==-3),axis=0)    #Right


    countE =np.count_nonzero(A<0,axis = 0)   #West occurences
    countW =np.count_nonzero(A>0,axis = 0)    #East occurences

    #detect zero occurences , only for debugging purposes
    countZeros=np.count_nonzero(A==0,axis = 0)
    print("zero occurences: ",countZeros)

    #P(X2 | e1:3)
    x2=[countL[2]/n,countC[2]/n,countR[2]/n]
    print("P(X2) ",x2)

    #P(X3 | e1:3)
    x3=[countL[3]/n,countC[3]/n,countR[3]/n]
    print("P(X3) ",x3)

    #P(X4 | e1:3)
    x4=[countL[4]/n,countC[4]/n,countR[4]/n]
    print("P(X4) ",x4)

    #P(A2|e1:3)
    A2=[countE[2]/n,countW[2]/n]
    print("P(A2) ",A2)

    #P(A3 | e1:3)
    A3=[countE[3]/n,countW[3]/n]
    print("P(A3) ",A3)

    #P(A4 | e1:3)
    A4=[countE[4]/n,countW[4]/n]
    print("P(A4) ",A4)
















































#main program: defines number of samples, initializes tableA