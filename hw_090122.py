# Exercise #1
# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']

def swap(words, a, b, c, d, e):

    words[a], words[b], words[c], words[d], words[e] = words[e], words[d], words[c], words[b], words[a]

    return words
print(swap(words, 4,3,2,1,0))


# or

words = ['this' , 'is', 'a', 'sentence', '.']
    
def two_point(my_list):
    left = 0
    right = len(my_list) - 1
    
    while left <= right:
        my_list[left], my_list[right] = my_list[right], my_list[left]
        left += 1
        right -= 1
    return my_list
    
two_point(words)


# Exercise #2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...


a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def word_count(arr):
    dict_a = {}

                    
    for word in sorted(arr.split()): #.lower() maybe
        if word in dict_a:
            dict_a[word] += 1
        else:
            dict_a[word] = 1
            
    return dict_a
print(word_count(a_text))




# Exercise #3
# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

# Hint: Linear Searching will require searching a list for a given number.




list_a = [1, 22, 34, 44, 55, 66, 88, 100]

def linear_search(arr, num):
    try:
        for i in range(len(arr)):

            if arr[i] == num:
                return i

        raise ValueError("number not found")
    except ValueError as error:
        print(error)
print(linear_search([1, 22, 34, 44, 55, 66, 88, 100],100))