from functions import *





if __name__ == "__main__":

    #Direction of the wind: L: Left, R: Right, C: Center, E:East, W:West
    #representation: LE=1, CE=2, RE=3, LW=-1,CW=-2,RW=-3

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


    countW =np.count_nonzero(A<0,axis = 0)   #West occurences
    countE =np.count_nonzero(A>0,axis = 0)    #East occurences

    #detect zero occurences , only for debugging purposes
    # countZeros=np.count_nonzero(A==0,axis = 0)
    # print("zero occurences: ",countZeros)

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
