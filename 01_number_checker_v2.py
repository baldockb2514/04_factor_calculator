def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter a number that is between 1 and 200."
        
        try:
        
            # ask user to enter a number
            response = int(input(question))
            
            # checks number is more than zero
            if 1 <= response <=200:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    

to_factor = num_check("What number do you want to factor? ")