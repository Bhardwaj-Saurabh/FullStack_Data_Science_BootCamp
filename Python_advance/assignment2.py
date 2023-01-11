'''
1. Write a function that takes a positive integer num and calculates how many dots exist 
in a pentagonal shape around the center dot on the Nth iteration.

In the image below you can see the first iteration is only a single dot. On the second, 
there are 6 dots. On the third, there are 16 dots, and on the fourth there are 31 dots.

Return the number of dots that exist in the whole pentagon on the Nth iteration.

Examples
pentagonal(1) ➞ 1
pentagonal(2) ➞ 6
pentagonal(3) ➞ 16
pentagonal(8) ➞ 141
'''
def pentagonal(number):
    '''
    This function takes a positive integer num and calculates how many dots exist  
    in a pentagonal shape around the center dot on the Nth iteration.

    Parameters:
    - a positive integer number

    Return:
    - the number of dots that exist in the whole pentagon on the Nth iteration
    '''
    no_of_dot = 1
    for i in range(number):
        no_of_dot += 5 * i
    return no_of_dot

print(pentagonal(8))

'''
2.  Make a function that encrypts a given input with these steps:
Input: "apple"
Step 1: Reverse the input: "elppa"
Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"
Output: "1lpp0aca"

Examples
encrypt("banana") ➞ "0n0n0baca"
encrypt("karaca") ➞ "0c0r0kaca"
encrypt("burak") ➞ "k0r3baca"
encrypt("alpaca") ➞ "0c0pl0aca"
'''
vowels = {'a':'0', 'e':'1', 'i':'2', 'o':'2', 'u':'3'}
def encrypt(text):
    '''
    This function takes a string that encrypts a given input with these steps:
    Step 1: Reverse the input
    Step 2: Replace all vowels using the vowels dictionary
    Step 3: Add "aca" to the end of the word:

    Parameters:
    - text string

    Return:
    - output string as per the above steps
    '''
    reverse_string = text[::-1]
    output = ''
    for letter in reverse_string: 
        if letter in vowels.keys():
            output += vowels[letter]
        else:
            output += letter
    output += 'aca'
    return output

print(encrypt("alpaca"))

'''
3. Given the month and year as numbers, return whether that month contains a Friday 13th.(i.e You can check Python's datetime module)

Examples
has_friday_13(3, 2020) ➞ True
has_friday_13(10, 2017) ➞ True
has_friday_13(1, 1985) ➞ False
'''
import datetime

# def has_friday_13(month, year):
#     given_date = datetime.date(year, month)
#     given_date = given_date.strftime('%A, %B-%Y')
#     print(given_date)


'''

4. Write a regular expression that will help us count how many bad cookies are produced every day. 
You must use RegEx negative lookbehind.

Example
lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
pattern = "yourregularexpressionhere"
len(re.findall(pattern, ", ".join(lst))) ➞ 2
'''


'''
5. Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
pluralize(["table", "table", "table"]) ➞ { "tables" }
pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
'''

def pluralize(things_list):
    unique_things = set()
    for i in things_list:
        no = 0
        for j in things_list:
            if i == j:
                no += 1
        if no > 1:
            unique_things.add(i + 's')
        else:
            unique_things.add(i)

    return unique_things

print(pluralize(["chair", "pencil", "arm"]))