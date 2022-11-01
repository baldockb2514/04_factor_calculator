# Functions go here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5 

    #add decoration to start and ent of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a number that is equal to or greater than 1, and equal or less than 200.")
    print()
    print("This calculator gives you the factors of a number, as well if it is a UNITY, perfect square, or prime number")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation to continue, or any key to quit.")
    print()
    return""

# Checks that integer is between two numbers
def num_check(question, low, high):
    valid = False
    while not valid:
        
        error = "Please enter a number that is between {} and {}.".format(low, high)
        
        try:
        
            # ask user to enter a number
            response = int(input(question))
            
            # checks number is more than zero
            if low <= response <=high:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    


# gets factors, returns a sorted list
def get_factors(to_factor):

    stop = int(to_factor**(0.5))

    factors_list = []

    for item in range(1, stop +1):
        # print("to_factor % {}".format(item)) 
        is_factor = to_factor % item

        # if modulo is 0, the number is a factor
        if is_factor == 0:

            # gets second factor by dividing 'to factor' by the first factor
            factor_2 = (to_factor / item)

            factors_list.append(int(item))

            if factor_2 not in factors_list:
                factors_list.append(int(factor_2))

    # output
    factors_list.sort()
    return factors_list


# Main Routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue: ")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":
    
    comment = ""

    # ask user for number to be factored
    var_to_factor = num_check("Number? ", 1, 200)

    if var_to_factor != 1:
        factors_list = get_factors(var_to_factor)
    else:
        factors_list = ""
        comment = "One is UNITY!  It only has one factor.  Itself :)"

    # comments for squares / primes
    if len(factors_list) == 2:
        comment = "{} is a prime number".format(var_to_factor)
    elif len(factors_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)
    
    # output factors and comments

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is special..."

    else: 
        heading = "Factors of {}".format(var_to_factor)

    # output factors and comment
    statement_generator(heading, "*")
    print()
    print(factors_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()