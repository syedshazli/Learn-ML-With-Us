from part1 import *
import numpy as np
import sys

def main():

    X,Y = Tree.load_dataset('part2.csv')
    model = Tree.train(X,Y)

    predictionSet = np.array([['low','low','no','yes','male'],
                              ['low','medium','yes','yes','female']])
    predictionSet = predictionSet.T

    outputPrediction = Tree.predict(model,predictionSet)
    print(outputPrediction)

if __name__ == "__main__":
    main()
