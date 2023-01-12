'''
1. Create a function that takes a number n (integer greater than zero) as an argument, 
and returns 2 if n is odd and 8 if n is even.
You can only use the following arithmetic operators: addition of numbers +, subtraction of numbers -, 
multiplication of number *, 
division of number /, and exponentiation **.
You are not allowed to use any other methods in this challenge (i.e. no if statements, 
comparison operators, etc).

Examples
f(1) ➞ 2
f(2) ➞ 8
f(3) ➞ 2
'''
def f(num):
    return 8 * (num%2 ==0) + 2 * (num%2 != 0)

print(f(2))

'''

2. Create a function that returns the majority vote in a list. 
A majority vote is an element that occurs > N/2 times in a list 
(where N is the length of the list).

Examples
majority_vote(["A", "A", "B"]) ➞ "A"
majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None

'''
def majority_vote(votes):
    N = len(votes)
    value = {}
    for iter_1 in set(votes):
        count = 0
        for iter_2 in votes:
            if iter_1 == iter_2:
                count += 1
        value[iter_1] = count

    out = 0
    out_key = ''
    for k, v in value.items():
        if v > out:
            out = v
            out_key = k
    if out > N/2:
        
        return out_key

print(majority_vote(["A", "B", "A"]))

'''

3. Create a function that takes a string txt and censors any word from a given list lst. 
The text removed must be replaced by the given character char.

Examples
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")
censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"

'''
def censor_string(string_text, censors_word, replace_char):
    
    string_list = []
    for word in string_text.split():
        if word in censors_word:
            replaced_word = len(word)*replace_char
            string_list.append(replaced_word)
        else:
            string_list.append(word)
    
    return ' '.join(string_list)
        
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))

'''
4. In mathematics a Polydivisible Number (or magic number) is a number in a given number 
base with digits abcde... that has the following properties:

-  Its first digit a is not 0.
- The number formed by its first two digits ab is a multiple of 2.
- The number formed by its first three digits abc is a multiple of 3.
- The number formed by its first four digits abcd is a multiple of 4.

Create a function which takes an integer n and returns True if the given number is a 
Polydivisible Number and False otherwise.

Examples

is_polydivisible(1232) ➞ True
# 1     / 1 = 1
# 12    / 2 = 6
# 123   / 3 = 41
# 1232  / 4 = 308

is_polydivisible(123220 ) ➞ False
# 1   / 1 = 1
# 12   / 2 = 6
# 123   / 3 = 41
# 1232   / 4 = 308
# 12322   / 5 = 2464.4         # Not a Whole Number
# 123220   /6 = 220536.333...  # Not a Whole Number
'''

def is_polydivisible(number):
    
    num = ''
    counter = 0
    for i in str(number):
        num += i
        counter += 1
        if int(num)%counter != 0:
            return False
    
    return True

print(is_polydivisible(1232))

'''

5. Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.

Examples
sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 27
sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
sum_primes([]) ➞ None
'''
def sum_primes(numbers):
    total = 0
    for num in numbers:
        prime_no = False
        for i in range(2, num):
            if num%i != 0:
                prime_no = True
            else:
                break
        if prime_no or num == 1 or num == 2:
            total += num
    
    if total > 0:
        return total

print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

