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

print()
to_factor = num_check("What number do you want to factor? ", 1, 200)