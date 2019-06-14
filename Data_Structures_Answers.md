Time complexity deals with finding out how the computational time of an algorithm changes with the change in size of the input. On the other hand space complexity deals with finding out how much (extra)space would be required by the algorithm with change in the input size

Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
    O(1) constant time - no loops
2. What is the space complexity of your ring buffer's `append` function?
    O(1) constant time - no loops
3. What is the runtime complexity of your ring buffer's `get` method?
    O(n) on else and O(1) on if
4. What is the space complexity of your ring buffer's `get` method?
    O(1) constant time - no loops
5. What is the runtime complexity of the provided code in `names.py`?
    0(n^2) Lists are the same length and * by each other. 
6. What is the space complexity of the provided code in `names.py`?
    O(n) Machine holding both lists. The longer the list,the more space
7. What is the runtime complexity of your optimized code in `names.py`?
    O(n log n)
8. What is the space complexity of your optimized code in `names.py`?
    O(n)