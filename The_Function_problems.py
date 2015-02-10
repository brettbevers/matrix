# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1) Tuple Sum
def tuple_sum(A, B): return [(sum(X), sum(Y)) for (X, Y) in [zip(a, b) for (a, b) in zip(A, B)]]


'''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    '''
pass  ## 2: (Problem 2) Inverse Dictionary
def inv_dict(d): return {v: k for (k, v) in d.items()}


'''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Examples:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'})
    {'merci':'thank you', 'au revoir':'goodbye'}]
    '''
pass  ## 3: (Problem 3) Nested Comprehension
def row(p, n): return [p + i for i in range(n)]


'''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
pass

comprehension_with_row = [row(i, 20) for i in range(15)]

comprehension_without_row = [[i + j for j in range(20)] for i in range(15)]



## 4: (Problem 4) Probability Exercise 1
domain_4 = {1, 2, 3, 5, 6}


def f(x): return x + 1


dist_4 = {1: 0.5, 2: 0.2, 3: 0.1, 5: 0.1, 6: 0.1}
Pr_f_is_even = sum([dist_4[x] for x in domain_4 if f(x) % 2 == 0])
Pr_f_is_odd = sum([dist_4[x] for x in domain_4 if f(x) % 2 == 1])



## 5: (Problem 5) Probability Exercise 2
domain_5 = {1, 2, 3, 4, 5, 6, 7}


def g(x): return x % 3


dist_5 = {1: 0.2, 2: 0.2, 3: 0.2, 4: 0.1, 5: 0.1, 6: 0.1, 7: 0.1}
Pr_g_is_1 = sum([dist_5[x] for x in domain_5 if g(x) == 1])
Pr_g_is_0or2 = sum([dist_5[x] for x in domain_5 if g(x) == 0 or g(x) == 2])

