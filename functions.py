#n: number of samples
import numpy as np
from numpy import random

#κωδικοποιηση: LE=1, CE=2, RE=3, LW=-1,CW=-2,RW=-3

#generate initial population of samples
def initial_pop(tableA):

    ini_values=[1,2,3]
    n=tableA.shape[0]       #number of rows=number of samples
    tableA[:,0]=np.random.choice(ini_values,n)     #fill with samples at t=0,(uniform distribution over all entries of ini_values at t=0)


def repopulate(tableA,t):

    #set value for position
    for row in range(len(tableA)):
        x = random.rand()       #generate random number(0,1) to define wind value at timestep t
        if tableA[row,t-1]==1:   #LE
            tableA[row,t]=1
            if x>0.7:
                tableA[row,t]=-tableA[row,t]   #W

        elif tableA[row,t-1]==-1:  #LW
            tableA[row,t]=np.random.choice([-1,-2])
            if x>0.7:
                tableA[row,t]=-tableA[row,t]   #E

        elif tableA[row,t-1]==2:   #CE
            tableA[row,t]=np.random.choice([1,2])
            if x>0.7:
                tableA[row,t]=-tableA[row,t]    #W

        elif tableA[row,t-1]==-2:  #CW
            tableA[row,t]=np.random.choice([-2,-3])
            if x>0.7:
                tableA[row,t]=-tableA[row,t]  #E

        elif tableA[row,t-1]==3:   #RE
            tableA[row,t]=np.random.choice([2,3])
            if x>0.7:
                tableA[row,t]=-tableA[row,t]    #W

        elif tableA[row,t-1]==-3: #RW
            tableA[row,t]=-3
            if x>0.7:
                tableA[row,t]=-tableA[row,t]  #E

def weighted(tableA,t,e):
    w=np.zeros(tableA.shape[0])
    #με np.where?
    if e[t]=="C":
        w[:]=np.where(np.absolute(tableA[:,t])==1,0.2,np.where(np.absolute(tableA[:,t])==2,0.4,0.2))
    elif  e[t]=="L":
        w[:]=np.where(np.absolute(tableA[:,t])==1,0.7,np.where(np.absolute(tableA[:,t])==2,0.3,0.1))
    return w


def resample(sum,w,tableA,tableB,t):

    for row in range(len(tableA)):
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




















































#main program: defines number of samples, initializes tableA