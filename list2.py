import string
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
# Hint: Don't use `set()`
def remove_adjacent(nums):
    return [x for (i, x) in enumerate(nums) if ((i == 0) | (x != nums[i-1])) ]

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# The solution should work in "linear" time, making a single pass of both lists.
# Hint: Don't use `sort` or `sorted` -- they are not linear time.

def linear_merge(list1, list2):
    new_list = []
    i = 0
    n = 0
    while i < len(list1) or n < len(list2):
        if(i == len(list1)):
            new_list.extend(list2[n:])
            break
        if(n == len(list2)):
            new_list.extend(list1[i:])
            break
        if(string.ascii_lowercase.index(list1[i][0]) == string.ascii_lowercase.index(list2[n][0])):
            new_list.append(list1[i])
            new_list.append(list2[n])
            i+=1
            n+=1
        if(string.ascii_lowercase.index(list1[i][0]) < string.ascii_lowercase.index(list2[n][0])):
            new_list.append(list1[i])
            i+=1
            continue
        if(string.ascii_lowercase.index(list2[n][0]) < string.ascii_lowercase.index(list1[i][0])):
            new_list.append(list2[n])
            n+=1
            continue
    return new_list


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    test(remove_adjacent([2, 2, 3, 3, 3, 4, 5, 2, 3]), [2, 3, 4, 5, 2, 3])

    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])

# Standard boilerplate (python idiom) to call the main() function.
if __name__ == '__main__':
    main()
