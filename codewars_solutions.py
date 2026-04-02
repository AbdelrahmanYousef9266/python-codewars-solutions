# Solution: Even or Odd
def even_or_odd(number): # define a function that takes number as argument.
    if number % 2 == 0: # check if the number is divisible by 2.
        return "Even" # number is even.
    else:
        return "Odd" # number is odd
    


    
# Solution: Convert a Number to a String
def number_to_string(num):
    return str(num)



# Solution: Remove String Spaces
def no_space(x):              # function that removes spaces from a string
    return x.replace(" ", "") # replace all spaces with nothing


# Solution: Vowel Count
def get_count(string):  # function that counts vowels in a string
     return sum(1 for char in string if char in 'aeiouAEIOU')  # count vowels using a generator expression