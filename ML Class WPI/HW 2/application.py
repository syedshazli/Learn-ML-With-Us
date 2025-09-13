import math
import numpy as np
from linear_regression import *
from sklearn.datasets import make_regression
# Note: please don't add any new package, you should solve this problem using only the packages above.
#-------------------------------------------------------------------------
'''
    Problem 2: Apply your Linear Regression
    In this problem, use your linear regression method implemented in problem 1 to do the prediction.
    Play with parameters alpha and number of epoch to make sure your test loss is smaller than 1e-2.
    Report your parameter, your train_loss and test_loss 
    Note: please don't use any existing package for linear regression problem, use your own version.
'''

#--------------------------

n_samples = 200
X,y = make_regression(n_samples= n_samples, n_features=4, random_state=1)
y = np.array(y).T
X = np.array(X)
Xtrain, Ytrain, Xtest, Ytest = X[::2], y[::2], X[1::2], y[1::2]

#########################################
## INSERT YOUR CODE HERE

trainingLoss = 0
w = train(Xtrain, Ytrain, alpha = 0.1, n_epoch = 90)

PredictedTraining = Xtrain.dot(w)

trainingLoss = compute_L(PredictedTraining, Ytrain)
print("Training Loss is: "+str(trainingLoss))

# Test Loss
testLoss = 0

PredictedTest = Xtest.dot(w)

testLoss = compute_L(PredictedTest, Ytest)
print("Test Loss is: "+str(testLoss))


# Combined = Combined.astype('float64')
# Ytrain = Ytrain.astype('float64')
# for r in range(len(Ytrain)):
#         if Combined[r] == Ytrain[r]:
#             print("Hey")
#         else:
#             print("Here's our thing. Combined: " + str(Combined[r]) + " Ytrain: " + str(Ytrain[r]) + '\n')






#########################################

