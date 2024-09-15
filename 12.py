def count_vowels(s):
    vowels = 'aeiouAEIOerfds'
    return sum(1 for char in s if char in vowels)

def add_numbers(a, b):
    return a + b

def max_in_list(lst):
    return max(lst)

def unique_elements(lst):
    return list(set(lst))

def sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

def reverse_list(lst):
    return lst[::-1]

def count_above_average(lst):
    average = sum(lst) / len(lst) if lst else 0
    return sum(1 for x in lst if x > average)

def filter_strings_with_substring(lst, substring):
    return [s for s in lst if substring in s]

def reverse_string(s):
    return s[::-1]

def filter_alpha_numeric(lst):
    return [s for s in lst if s.isalnum()]

def add_matrices(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

def median_of_list(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        return sorted_lst[n // 2]

def is_palindrome(s):
    return s == s[::-1]

import math

def factorial(n):
    return math.factorial(n)

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def keys_with_max_value(d):
    max_value = max(d.values())
    return [k for k, v in d.items() if v == max_value]