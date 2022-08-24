# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

'''
How does this solution ensure data immutability?
=> All of the data is in the object itself and cannot be accessed outside of the object.

Is this solution a pure function? Why or why not?
=> It is not, because it has an append feature 

Is this solution a higher order function? Why or why not?
=> No, it is not. This function doe snot perform operations on other functions

Would it have been easier to solve this problem using a different programming style?
=> I don't think so

Why in particular is functional programming a helpful paradigm when solving this problem?
=> This function is dry, and doesn't need extra objects in order to solve.
'''