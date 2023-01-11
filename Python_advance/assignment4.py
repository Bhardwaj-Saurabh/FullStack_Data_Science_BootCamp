'''1. In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1:

The beginning of the sequence is this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

The function fastFib(num) returns the fibonacci number Fn, of the given num as an argument.
Examples
fib_fast(5) ➞ 5
fib_fast(10) ➞ 55
fib_fast(20) ➞ 6765
fib_fast(50) ➞ 12586269025
'''
def fib_fast(num):
    total = 0
    for i in range(num+1):
        total += i

    return total

print(fib_fast(5))

'''

2. Create a function that takes a strings characters as ASCII and returns each characters hexadecimal value as a string.

Examples
convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"
convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"
convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"
'''
def convert_to_hex(given_string):
    outcome = []
    for letter in given_string:
        outcome.append(str(letter.encode('utf-8').hex()))
    return ' '.join(outcome)
print(convert_to_hex("Big Boi"))

'''
3. Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.
Given a censored string and a string of the censored vowels, return the original uncensored string.

Example
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
uncensor("abcd", "") ➞ "abcd"
uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
'''
def uncensor(my_string, lost_vowels):

    true_string = ''
    n = 0
    for letter in my_string:
        if letter != '*':
            true_string += letter
        else:
            true_string += lost_vowels[n]
            n += 1

    return true_string

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))

'''
4. Write a function that takes an IP address and returns the domain name using PTR DNS records.

Example
get_domain("8.8.8.8") ➞ "dns.google"
get_domain("8.8.4.4") ➞ "dns.google"
'''



'''
5. Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:

Examples

fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288
fact_of_fact(5) ➞ 34560
fact_of_fact(6) ➞ 24883200
'''
def fact_of_fact(num):
    outcome = 1
    for i in range(1, num+1):
        fcto_2 = 1
        for j in range(1, i+1):
            fcto_2 *= j
        outcome *= fcto_2
    return outcome

print(fact_of_fact(6))
        

