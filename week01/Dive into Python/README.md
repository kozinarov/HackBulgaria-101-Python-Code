Problems
========================

In a file, called diveintopython.py, code the solutions to the following problems:

The solutions should be written in Python 3.

# 1.Is Number Balanced?
----------------
A number is called balanced, if we take the middle of it and the sums of the left and right parts are equal.

For example, the number `1238033` is balanced, because it's left part is `123` and right part is `033`.

We have : `1 + 2 + 3 = 0 + 3 + 3 = 6`.

A number with only one digit is always balanced!

Implement a function `is_number_balanced(n)` that checks if `n` is balanced.

## Test Examples
```python
>>> is_number_balanced(9)
True
>>> is_number_balanced(4518)
True
>>> is_number_balanced(28471)
False
>>> is_number_balanced(1238033)
True
```
# 2.Increasing and Decreasing Sequences
----------------

Implement the following functions:

## 2.1 Increasing sequnce?

Implement a function, called `is_increasing(seq)` where `seq` is a `list` of integers.

The function should return `True`, if the given sequence is monotonously increasing.

And before you skip this problem, because of the math terminology, let me explain:

**A sequence is monotonously increasing if for every two elements `a` and `b`, that are next to each other (`a` is before `b`), we have `a` < `b`.**

For example, `[1,2,3,4,5]` is monotonously increasing, but `[1,2,3,4,5,1]` is not.

### Test Examples
```python
>>> is_increasing([1,2,3,4,5])
True
>>> is_increasing([1])
True
>>> is_increasing([5,6,-10])
False
>>> is_increasing([1,1,1,1])
False
```

## 2.2 Descreasing sequence?

Implement a function, called `is_decreasing(seq)` where `seq` is a `list` of integers.

The function should return `True`, if the given sequence is monotonously decreasing.

And before you skip this problem, because of the math terminology, let me explain:

**A sequence is monotonously decreasing if for every two elements `a` and `b`, that are next to each other (`a` is before `b`), we have `a` > `b`.**

For example, [5,4,3,2,1] is monotonously decreasing, but [1,2,3,4,5,1] is not.

### Test Examples
```python
>>> is_decreasing([5,4,3,2,1])
True
>>> is_decreasing([1,2,3])
False
>>> is_decreasing([100, 50, 20])
True
>>> is_decreasing([1,1,1,1])
False
```

# 3. Largest Palindrome
----------------

Implement a function get_largest_palindrome(n), which return the largest palindrome smaller than `n`. Given number `n` can also be palindrome.

## Test Examples
```python
>>> get_largest_palindrome(99)
88
>>> get_largest_palindrome(252)
242
>>> get_largest_palindrome(994687)
994499
>>> get_largest_palindrome(754649)
754457
```

# 4. Prime Numbers
----------------

Given an integer, implement a function, called `prime_numbers(n)`.
Use [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to find all the prime numbers less than or equal to `n`.

## Test Examples
```python
>>> prime_numbers(30)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> prime_numbers(3)
[2, 3]
```

# 5. Anagrams
----------------

For anagrams, check here - https://en.wikipedia.org/wiki/Anagram

For example, `listen` and `silent` are anagrams.

Implement a function `is_anagram(a, b)`, which returns `True`, if the string `a` is an anagram of `b`. 

**Consider lowering the case of the two words since the case does not matter**. `SILENT` and `listen` are also anagrams.

## Test Examples
```python
>>> is_anagram("BRADE", "BeaRD")
True
>>> is_anagram("TOP_CODER", "COTO_PRODE")
False
```

# 6. Birthday Ranges
----------------

Implement a function `birthday_ranges(birthdays, ranges)`
We have a list `birthdays` and list of tuples `ranges`. `birthdays` - range from 0 to 365, `ranges` - ranges (one range is a tuple of two numbers - `start` and `end`0.

We want to calculate, for each tuple, how many people are born in that range (between `start` and `end` inclusive).

For example:

```python
Birthdays - [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15]
Ranges - [(4, 9), (6, 7), (200, 225), (300, 365)] 
```

Will give the result:
```python
[5, 2, 0, 1]
```

As we can see, betweeh 4 and 9, inclusive, there are 5 people with birthdays - 5, 6, 7, 4, 5.Between 300 and 365 there is exatly one birthday - 300.



## Test Examples
```python
>>> birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])
[2, 3, 4, 5, 2]
```

# 7. Sum Numbers in Matrix
----------------

You are given a `NxM` matrix  of integer numbers.

Implement a function, called `sum_matrix(m)` that returns the sum of all numbers in the matrix.

The matrix will be represented as nested lists in Python.

## Examples:

```python
>>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> sum_matrix(m)
45
>>> m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> sum_matrix(m)
0
>>> m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
>>> sum_matrix(m)
55
```

# 8. Matrix Bombing
----------------

You are givn a `NxM` matrix of integer numbers.

We can drop a bomb at any place in the matrix, which has the following effect:

* All of the **3 to 8 neighbours** (depending on where you hit!) of the target are reduced by the value of the target.
* Numbers can be reduced only to 0 - they cannot go to negative.

For example, if we have the following matrix:

```
10 10 10
10  9  10
10 10 10
```

and we drop bomb at `9`, this will result in the following matrix:

```
1 1 1
1 9 1
1 1 1
```

Implement a function called `matrix_bombing_plan(m)`.

The function should return a dictionary where keys are positions in the matrix, represented as tuples, and values are the total sum of the elements of the matrix, after the bombing at that position.

The positions are the standard indexes, starting from `(0, 0)`

For example if we have the following matrix:

```
1 2 3
4 5 6
7 8 9
```

and run the function, we will have:

```python
{(0, 0): 42,
 (0, 1): 36,
 (0, 2): 37,
 (1, 0): 30,
 (1, 1): 15,
 (1, 2): 23,
 (2, 0): 29,
 (2, 1): 15,
 (2, 2): 26}
```

We can see that if we drop the bomb at `(1, 1)` or `(2, 1)`, we will do the most damage!


# 9.Transversal
----------------
Lets have a set of sets:

`A = { {1, 2, 3} , {4, 5, 6}, {7, 8, 9} }`

A transerval `T` for `A` is a set that contains at least one element from each set of `A`.

For example: 
`T = {1, 4, 7}`


Implement a function `is_transversal(transversal, family)`, which check if given set is a valid `transerval` for another `family` of sets (set of sets). 

### Signature
```python
def is_transversal(transversal, family):
	pass
```

#### Test Examples
```python
>>> is_transversal([4, 5, 6], [[5, 7, 9], [1, 4, 3], [2, 6]]))
True
>>> is_transversal([1, 2], [[1, 5], [2, 3], [4, 7]])
False
>>> is_transversal([2, 3, 4], [[1, 7], [2, 3, 5], [4, 8]])
False
```