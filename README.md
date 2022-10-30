# BatteryPolarity

A school project to create an algorithm in 5 steps to determine if 4 batteries with two poles in a spinning store are all facing the same direction.

- Step 1: peek adjacent - change both to p and check
- Step 2: peek opposite - change both to p and check
- Step 3: peek opposite - if either are n, change to p, else if both p change 1 to n
- Step 4: peek adjacent - flip both
- Step 5: peek opposite - if either are n, change to p

Requirements to run code:
- Python 3+
- PIP
- venv


# Analysis:

This is an appropriate and simple solution when we are only dealing with 4 batteries in the store that only have two poles.
Unfortunately, this solution would not scale well if you add extra batteries or the batteries have more than two poles.

Thus, this is an adequate solution if there are only 4 batteries that each have two polarities. 
Upscaling of any parameters would cause issues and would require a different solution.

# Big O

We can guarantee that we can solve this problem in just 5 steps.

Therefore:
PEEK, SPIN, CHANGE = O(5) = O(1) = Constant time
