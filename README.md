# BatteryPolarity

A school project to create an algorithm in 5 steps to determine if 4 batteries in a spinning canister are all facing the same direction.

- Step 1: peek adjacent - change both to p and check
- Step 2: peek opposite - change both to p and check
- Step 3: peek opposite - if either are n, change to p, else if both p change 1 to n
- Step 4: peek adjacent -  flip both
- Step 5: peek opposite - if n change both

Requirements to run code:
- Python 3+
- PIP
- venv