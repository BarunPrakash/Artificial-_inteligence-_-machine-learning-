""" linear Reg Algo 
Desgined : by barun
Date:10 :4 :2019
Mission: Improving Algo
"""

#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt 

w = 1  # random Guess: random values
x_data  = [1.0 ,2.0,3.0]
y_data  = [2.0,4.0,6.0]

# our model for for forward oass
def forwardVal(x ,w):
    return x*w
    
##############################
 
def forwardValGlobal(x):
    return x*w
  
def randomLoss(x,y,w):
    yp = forwardVal(x,w)
    return (yp -y)*(yp -y)
    
def randomLoss(x,y):
    yp = forwardVal(x,w)
    return (yp -y)*(yp -y)
    
###############################

#compute loss for different W


def gradientForLr(x,y):
    return 2 *x *(x * w -y)
###############################################
    
def computelossForDiffrentWeight():
    w_list =[]
    mse_list =[]
    for w in  np.arange(0.0,4.1 ,0.1):
        print("W=",w)
        l_sum =0
        for x_val ,y_val in zip(x_data ,y_data):
            y_pv =forwardVal(x_val,w)
            l = randomLoss(x_val,y_val,w)
            l_sum +=l
            print("\t",x_val,y_val,y_pv,l)
        print("MsE",l_sum/3)
        w_list.append(w)
        print("append",w_list)
        mse_list.append(l_sum/3)
        print("mselist",mse_list)
        
        
    plt.plot(w_list,mse_list)
    plt.ylabel('Loss') 
    plt.xlabel('Weigth')
    plt.show()
  
  
#################################
def findGradient():
    #befor trainnig
    print("predict befor trainnig",4,forwardValGlobal(4))
    #Trainnig loop 
    global w 
    for epoch in range(100):
        for x_val ,y_val in zip(x_data,y_data):
            grad =gradientForLr(x_val,y_val)
            w =w - 0.01 * grad
            print("\tgrad:",x_val,y_val,grad)
            l = randomLoss(x_val,y_val)
        print("Prog:",epoch,"W=", w , "loss=", l)
    #after trainnig
    
    print("Predict after trainnig ","4 hours" ,forwardValGlobal(4))
    

