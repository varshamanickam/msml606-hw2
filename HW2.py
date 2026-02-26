import csv

### REFERENCES USED:
#1) https://cse.iitkgp.ac.in/~debdeep/teaching/FOCS/slides/TreesnRelations.pdf
#2) https://youtu.be/WHs-wSo33MM?si=kqIleThDT-w4K2qA
#3) Clarified stack tree relationship using chatgpt. Asked it to walk me through examples and give me
# example problems to see if I understood postfix correctly


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HomeWork2:

    # Problem 1: Construct an expression tree (Binary Tree) from a postfix expression
    # input -> list of strings (e.g., [3,4,+,2,*])
    # this is parsed from p1_construct_tree.csv (check it out for clarification)

    # there are no duplicate numeric values in the input
    # support basic operators: +, -, *, /

    # output -> the root node of the expression tree. Here: [*,+,2,3,4,None,None]
    # Tree Node with * as root node, the tree should be as follows
    #         *
    #        / \
    #       +   2
    #      / \
    #     3   4

    def constructBinaryTree(self, input) -> TreeNode:
        operations = {"+", "-", "*", "/"} 
        #just including the basic ops mentioned in the hw instructoins
        #used a set above because only unique elements and easy condition to check presence. eg: if token is in operations: do logic
        # and if token not in operations, then that would mean that that token is a number assuming only numbers and these listed ops will be in the input
        
        stack = []

        #logic for the for loop: goes throug the tokens in the input and if it's a number (operand), push as leaf nodes
        # if not a number (so if operator), then pop twice, push the operator with the 2 subtrees popped earlier as its children
        # finally, return the final root

        #handling empty input edge case
        if not input:
            return None # since empty input produces empty tree
        
        for token in input:
            token = token.strip() #i don't see any whitespaces in the test cases but just in case edge case handling

            #like I mentioned earlier, if token not in operatinos, then that token is a number and should be pushed as a leaf node
            if token not in operations:
                node = TreeNode(token)
                stack.append(node)
            
            # if it is a token, need to pop twice, right subtree first and then left subtree and then push the operator node and then 
            # the popped nodes as its children
            # Also, the first one popped is right and second one popped is left subtree because postfix format is (left operand   right operand   operator)
            else:
                #need to pop twice (2 subtrees) when we come across an operator in the input so if there aren't 2 subtrees to pop, then that's not enough 
                #operands before an operator. Not satisfying: (total_num of operands = total_num_of_operators + 1)
                if len(stack) < 2:
                    raise ValueError("Not enough operands before operator")
                right_subtree = stack.pop() #first pop - right
                left_subtree = stack.pop() #second pop - left subtree

                # pushing the operator as operator node and then popped nodes as its left and right children nodes
                node = TreeNode(token, left_subtree, right_subtree) 
                stack.append(node)
        
        # Used chatgpt here to understand how the final stack should only have one element. Took a bit to click that we're not adding the nodes themselves
        # but subtrees to the stack so if there's more than one subtree, then that means that there are multiple complete expressoins that were never combined 
        # into one expression 
        # This case will happen when (total # of operands) != (total # of operators + 1)
        if len(stack) != 1:
            raise ValueError("More than 1 complete expression present. There should only be one final complete expression.")
        
        return stack[0] #we want the first element (there should only be one element going by the logic I mentioned just above)
    
        




    # Problem 2.1: Use pre-order traversal (root, left, right) to generate prefix notation
    # return an array of elements of a prefix expression
    # expected output for the tree from problem 1 is [*,+,3,4,2]
    # you can see the examples in p2_traversals.csv

    def prefixNotationPrint(self, head: TreeNode) -> list:
        pass

    # Problem 2.2: Use in-order traversal (left, root, right) for infix notation with appropriate parentheses.
    # return an array of elements of an infix expression
    # expected output for the tree from problem 1 is [(,(,3,+,4,),*,2,)]
    # you can see the examples in p2_traversals.csv

    # don't forget to add parentheses to maintain correct sequence
    # even the outermost expression should be wrapped
    # treat parentheses as individual elements in the returned list (see output)

    def infixNotationPrint(self, head: TreeNode) -> list:
        pass


    # Problem 2.3: Use post-order traversal (left, right, root) to generate postfix notation.
    # return an array of elements of a postfix expression
    # expected output for the tree from problem 1 is [3,4,+,2,*]
    # you can see the examples in p2_traversals.csv

    def postfixNotationPrint(self, head: TreeNode) -> list:
        pass


class Stack:
    # Implement your stack using either an array or a list
    # (i.e., implement the functions based on the Stack ADT we covered in class)
    # You may use Python's list structure as the underlying storage.
    # While you can use .append() to add elements, please ensure the implementation strictly follows the logic we discussed in class
    # (e.g., manually managing the "top" of the stack
    
    # Use your own stack implementation to solve problem 3

    def __init__(self):
        # TODO: initialize the stack
        pass

    # Problem 3: Write code to evaluate a postfix expression using stack and return the integer value
    # Use stack which you implemented above for this problem

    # input -> a postfix expression string. E.g.: "5 1 2 + 4 * + 3 -"
    # see the examples of test entries in p3_eval_postfix.csv
    # output -> integer value after evaluating the string. Here: 14

    # integers are positive and negative
    # support basic operators: +, -, *, /
    # handle division by zero appropriately

    # DO NOT USE EVAL function for evaluating the expression

    def evaluatePostfix(exp: str) -> int:
        # TODO: implement this using your Stack class
        pass


# Main Function. Do not edit the code below
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)

        assert output == postfix, f"P1 Test {i} failed: tree structure incorrect"
        print(f"P1 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    with open('p2_traversals.csv', 'r') as f:
        testcases = list(csv.reader(f))

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)

        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"

        print(f"P2 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 3")
    testcases = []
    try:
        with open('p3_eval_postfix.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                testcases.append(row)
    except FileNotFoundError:
        print("p3_eval_postfix.csv not found")

    for idx, row in enumerate(testcases, start=1):
        expr, expected = row

        try:
            s = Stack()
            result = s.evaluatePostfix(expr)
            if expected == "DIVZERO":
                print(f"Test {idx} failed (expected division by zero)")
            else:
                expected = int(expected)
                assert result == expected, f"Test {idx} failed: {result} != {expected}"
                print(f"Test case {idx} passed")

        except ZeroDivisionError:
            assert expected == "DIVZERO", f"Test {idx} unexpected division by zero"
            print(f"Test case {idx} passed (division by zero handled)")