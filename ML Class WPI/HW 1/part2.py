from part1 import *
import numpy as np
import sys

# if we want to print a tree, all we need is the model



def main():

    X,Y = Tree.load_dataset('part2.csv')
    model = Tree.train(X,Y)

    predictionSet = np.array([['low','low','no','yes','male'],
                              ['low','medium','yes','yes','female']])
    predictionSet = predictionSet.T

    outputPrediction = Tree.predict(model,predictionSet)
    print(outputPrediction)

    Tree.print_tree_structure(model)

if __name__ == "__main__":
    main()

# MOVE THIS IN PART1.py
    @staticmethod
    def print_tree_structure(node, level=0, parent_info=""):
        '''
        Show the overall structure of the decision tree
        '''
        attribute_names = ["debt", "income", "married", "owns_property", "gender"]
    
        # Create indentation for current level
        indent = "  " * level
    
        if level == 0:
            print("DECISION TREE STRUCTURE:")
            print("=" * 30)
    
        if node.isleaf:
            print(f"{indent}LEAF: predicts '{node.p}' {parent_info}")
        else:
            attr_name = attribute_names[node.i]
            print(f"{indent}NODE: splits on '{attr_name}' {parent_info}")
        
            # Show all branches from this node
            for value, child in node.C.items():
                branch_info = f"(when {attr_name}='{value}')"
                Tree.print_tree_structure(child, level + 1, branch_info)
