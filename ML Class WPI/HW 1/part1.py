import math
import numpy as np
from collections import Counter
# Note: please don't add any new package, you should solve this problem using only the packages above.
# However, importing the Python standard library is allowed: https://docs.python.org/3/library/
#-------------------------------------------------------------------------
'''
    Part 1: Decision Tree (with Discrete Attributes) -- 60 points --
    In this problem, you will implement the decision tree method for classification problems.
    You could test the correctness of your code by typing `pytest -v test1.py` in the terminal.
'''

#-----------------------------------------------
class Node:
    '''
        Decision Tree Node (with discrete attributes)
        Inputs: 
            X: the data instances in the node, a numpy matrix of shape p by n.
               Each element can be int/float/string.
               Here n is the number data instances in the node, p is the number of attributes.
            Y: the class labels, a numpy array of length n.
               Each element can be int/float/string.
            i: the index of the attribute being tested in the node, an integer scalar 
            C: the dictionary of attribute values and children nodes. 
               Each (key, value) pair represents an attribute value and its corresponding child node.
            isleaf: whether or not this node is a leaf node, a boolean scalar
            p: the label to be predicted on the node (i.e., most common label in the node).
    '''
    def __init__(self,X,Y, i=None,C=None, isleaf= False,p=None):
        self.X = X
        self.Y = Y
        self.i = i
        self.C= C
        self.isleaf = isleaf
        self.p = p

#-----------------------------------------------
class Tree(object):
    '''
        Decision Tree (with discrete attributes). 
        We are using ID3(Iterative Dichotomiser 3) algorithm. So this decision tree is also called ID3.
    '''
    #--------------------------
    @staticmethod
    def entropy(Y):
        '''
            Compute the entropy of a list of values.
            Input:
                Y: a list of values, a numpy array of int/float/string values.
            Output:
                e: the entropy of the list of values, a float scalar
            Hint: you could use collections.Counter.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        e = 0
        myCounter = Counter(Y)
        for i in myCounter:
            probability = myCounter[i]/len(Y)
            e += probability * math.log(probability, 2)
        
        e = -e




        #########################################
        return e 
    
    
            
    #--------------------------
    @staticmethod
    def conditional_entropy(Y,X):
        '''
            Compute the conditional entropy of y given x. The conditional entropy H(Y|X) means average entropy of children nodes, given attribute X. Refer to https://en.wikipedia.org/wiki/Information_gain_in_decision_trees
            Input:
                X: a list of values , a numpy array of int/float/string values. The size of the array means the number of instances/examples. X contains each instance's attribute value. 
                Y: a list of values, a numpy array of int/float/string values. Y contains each instance's corresponding target label. For example X[0]'s target label is Y[0]
            Output:
                ce: the conditional entropy of y given x, a float scalar
        '''
        #########################################
        ## INSERT YOUR CODE HERE

        # average entropy of children nodes given an attribute.
        # X is a list of each instance's attribute value. size is number of examples
        # Y is a list of each instance's target label. 
        # X[0] Target Label is Y[0]

        ce = 0
        grouped = {}
        myCounter = Counter(X)
        for x, y in zip(X, Y):
            if x not in grouped:
                grouped[x] = []
            grouped[x].append(y)

        for i in grouped:
            ce += Tree.entropy(grouped[i]) * myCounter[i]/len(Y)
   
        #########################################
        return ce 
    
    
    
    #--------------------------
    @staticmethod
    def information_gain(Y,X):
        '''
            Compute the information gain of y after spliting over attribute x
            InfoGain(Y,X) = H(Y) - H(Y|X) 
            Input:
                X: a list of values, a numpy array of int/float/string values.
                Y: a list of values, a numpy array of int/float/string values.
            Output:
                g: the information gain of y after spliting over x, a float scalar
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        g = Tree.entropy(Y) - Tree.conditional_entropy(Y,X)

     

 
        #########################################
        return g


    #--------------------------
    @staticmethod
    def best_attribute(X,Y):
        '''
            Find the best attribute to split the node. 
            Here we use information gain to evaluate the attributes. 
            If there is a tie in the best attributes, select the one with the smallest index.
            Input:
                X: the feature matrix, a numpy matrix of shape p by n. 
                   Each element can be int/float/string.
                   Here n is the number data instances in the node, p is the number of attributes.
                Y: the class labels, a numpy array of length n. Each element can be int/float/string.
            Output:
                i: the index of the attribute to split, an integer scalar
        '''
        #########################################
        ## INSERT YOUR CODE HERE

        # loop through features (rows) of matrix
        # calculate info gain for each row
        # Find index of best feature (which has most info gain)
        infoGain = []
        for row in X:
            infoGain.append(Tree.information_gain(Y, row))
        
        # find index of best attribute
        i = 0
        maxNum = 0
        for j in range(len(infoGain)):
            if maxNum < infoGain[j]:
                maxNum = infoGain[j]
                i = j
 
        #########################################
        return i

        
    #--------------------------
    @staticmethod
    def split(X,Y,i):
        '''
            Split the node based upon the i-th attribute.
            (1) split the matrix X based upon the values in i-th attribute
            (2) split the labels Y based upon the values in i-th attribute
            (3) build children nodes by assigning a submatrix of X and Y to each node
            (4) build the dictionary to combine each  value in the i-th attribute with a child node.
    
            Input:
                X: the feature matrix, a numpy matrix of shape p by n.
                   Each element can be int/float/string.
                   Here n is the number data instances in the node, p is the number of attributes.
                Y: the class labels, a numpy array of length n.
                   Each element can be int/float/string.
                i: the index of the attribute to split, an integer scalar
            Output:
                C: the dictionary of attribute values and children nodes. 
                   Each (key, value) pair represents an attribute value and its corresponding child node.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        # Confusions: 
        # Do we create new node objects here?
        # How can Y be split based on an arbitrary feature? What is the relation?
        # What should be in the 'submatrix' of X & Y?
        C = {}

        # for each value in the current attribute split, store the value of the attribute and the indexes which it occurs
        value_to_indices = {}
        for index, value in enumerate(X[i]):
            if value not in value_to_indices:
                value_to_indices[value] = []
            value_to_indices[value].append(index)
        
        for value, indices in value_to_indices.items():
            X_subset = X[:,indices]
            Y_subset = Y[indices]
            
            myNewList = Counter(Y_subset)

            emptyCounter = None
            emptyIndex = None
            emptyP = None


            childNode = Node(X_subset, Y_subset, emptyIndex, emptyCounter, False, emptyP)

            # Store value of child node in dictionary
            C[value] = childNode
 
        




        
        #########################################
        return C

    #--------------------------
    @staticmethod
    def stop1(Y):
        '''
            Test condition 1 (stop splitting): whether or not all the instances have the same label. 
    
            Input:
                Y: the class labels, a numpy array of length n.
                   Each element can be int/float/string.
            Output:
                s: whether or not Conidtion 1 holds, a boolean scalar. 
                True if all labels are the same. Otherwise, false.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        s = False
        mySet = set(Y)
        if len(mySet) == 1:
            s = True




        
        #########################################
        return s
    
    #--------------------------
    @staticmethod
    def stop2(X):
        '''
            Test condition 2 (stop splitting): whether or not all the instances have the same attribute values. 
            Input:
                X: the feature matrix, a numpy matrix of shape p by n.
                   Each element can be int/float/string.
                   Here n is the number data instances in the node, p is the number of attributes.
            Output:
                s: whether or not Conidtion 2 holds, a boolean scalar. 
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        s = True
        for row in X:
            if len(set(row)) != 1:
                s = False
                break


    
   



 
        #########################################
        return s
    
            
    #--------------------------
    @staticmethod
    def most_common(Y):
        '''
            Get the most-common label from the list Y. 
            Input:
                Y: the class labels, a numpy array of length n.
                   Each element can be int/float/string.
                   Here n is the number data instances in the node.
            Output:
                y: the most common label, a scalar, can be int/float/string.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        myNewList = Counter(Y)
        y = myNewList.most_common(1)[0][0]
    



 
        #########################################
        return y
    
    
    
    #--------------------------
    @staticmethod
    def build_tree(t):
        '''
            Recursively build tree nodes.
            Input:
                t: a node of the decision tree, without the subtree built.
                t.X: the feature matrix, a numpy float matrix of shape p by n.
                   Each element can be int/float/string.
                    Here n is the number data instances, p is the number of attributes.
                t.Y: the class labels of the instances in the node, a numpy array of length n.
        '''
        #########################################
        ## INSERT YOUR CODE HERE

        # it's recursive, as in we need to keep calling build_tree
        if Tree.stop1(t.Y) or Tree.stop2(t.X):
            t.C = None
            t.i = None
            t.p = Tree.most_common(t.Y)
            t.isleaf = True
            return t

        t.i = Tree.best_attribute(t.X, t.Y)
        t.C = Tree.split(t.X, t.Y, t.i)
        t.p = Tree.most_common(t.Y)
        t.isleaf = False

        for value in t.C:
            Tree.build_tree(t.C[value])
        


    

   


 
        #########################################
    
    
    #--------------------------
    @staticmethod
    def train(X, Y):
        '''
            Given a training set, train a decision tree. 
            Input:
                X: the feature matrix, a numpy matrix of shape p by n.
                   Each element can be int/float/string.
                   Here n is the number data instances in the training set, p is the number of attributes.
                Y: the class labels, a numpy array of length n.
                   Each element can be int/float/string.
            Output:
                t: the root of the tree.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        t = Node(X, Y)

        Tree.build_tree(t)

    


 
        #########################################
        return t
    
    
    
    #--------------------------
    @staticmethod
    def inference(t,x):
        '''
            Given a decision tree and one data instance, infer the label of the instance recursively. 
            Input:
                t: the root of the tree.
                x: the attribute vector, a numpy vectr of shape p.
                   Each attribute value can be int/float/string.
            Output:
                y: the class labels, a numpy array of length n.
                   Each element can be int/float/string.
        '''
        #########################################
        ## INSERT YOUR CODE HERE

        # x is the feature values
        # now based on the feature values, label the class
        # but we must label it 'recursivley'
        if t.isleaf == True:
            return t.p
        
        # Otherwise, we are not at the leaf node. Keep calling this function

        index = t.i
        value = x[index]
        if value not in t.C:
            return t.p

        myChild = t.C[value]


        y = Tree.inference(myChild, x)
        

   




 
        #########################################
        return y
    
    #--------------------------
    @staticmethod
    def predict(t,X):
        '''
            Given a decision tree and a dataset, predict the labels on the dataset. 
            Input:
                t: the root of the tree.
                X: the feature matrix, a numpy matrix of shape p by n.
                   Each element can be int/float/string.
                   Here n is the number data instances in the dataset, p is the number of attributes.
            Output:
                Y: the class labels, a numpy array of length n.
                   Each element can be int/float/string.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        G = [None] * X.shape[1]
        for i in range(len(G)):
            G[i] = Tree.inference(t,X[:,i ])
        
        Y = np.array(G)
        






        #########################################
        return Y



    #--------------------------
    @staticmethod
    def load_dataset(filename = 'data1.csv'):
        '''
            Load dataset 1 from the CSV file: 'data1.csv'. 
            The first row of the file is the header (including the names of the attributes)
            In the remaining rows, each row represents one data instance.
            The first column of the file is the label to be predicted.
            In remaining columns, each column represents an attribute.
            Input:
                filename: the filename of the dataset, a string.
            Output:
                X: the feature matrix, a numpy matrix of shape p by n.
                   Each element can be int/float/string.
                   Here n is the number data instances in the dataset, p is the number of attributes.
                Y: the class labels, a numpy array of length n.
                   Each element can be int/float/string.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        X_DATA = []
        Y_DATA = []
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # skip first line
        for line in lines[1:]:
            mySplit = line.strip().split(',')
            Y_DATA.append(mySplit[0])
            X_DATA.append(mySplit[1:])
        
        X = np.array(X_DATA)
        X = X.T
        Y = np.array(Y_DATA)




 
        #########################################
        return X,Y

    