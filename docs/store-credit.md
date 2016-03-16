# Store Credit

## Problem

You recive a credit C at a local sotre and would like to buy two items. You first walk
through the store and create a list L of all available items. From this list you woluld like to
buy two items that add up to the entire value of the credit. The solution you provide will
consist of the two integers indicating the positions of the items in your list (smaler
number first).

### Input

The first line of input gives the number of cases, __N__. __N__ test cases follow. For each test case
there will be:

* One line containing the value __C__, the amount of credit you have at the store.
* One line containing the value __I__, the number of items in the store.
* One line containing a space separated list fo __I__ integers. Each integer __P__ indicates the price of an item in the store.
* Each test case will have exactly one solution.

### Output

For each test case, output one line containing "Case #__x__: " followed by the indices of the
two items whose price adds up to the store credit. The lower index should be output first.

### Limits

5 <= __C__ <= 1000

1 <= __P__ <= 1000

### Small dataset

__N__ = 10

3 <= __I__ <= 100

### Large dataset

__N__ = 50

3 <= __I__ <= 2000

### Sample

```
Input                         Output
3                             case #1: 2 3
100                           case #2: 1 4
3                             case #3: 4 5
5 75 25
200
7
150 24 79 50 88 345 3
8
8
2 1 9 4 4 56 90 3
```