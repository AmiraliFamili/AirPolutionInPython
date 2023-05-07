def sumvalues(values):
    """This function will calculate the sum of the given numbers (float or int) as an array or list 
    
    Argument(s) : 
    ---------------
    -  Values : a list or array that can contain anything 
    ---------------
    Note(s) : The program can detect any possible errors and rais an exception to make sure it always return the right value 
    using try and except keywords .
    ---------------
    Return(s) : This function return's the sum of the elements in a given list or array 
    """ 
    sum = 0 
    for i in values : 
        try: 
            sum += float(i)
        except:
            if type(i) == str : 
                pass
            else: 
                print("Invalid Input !")
    return sum 

def maxvalue(values):
    """ This function will return the maximum value within a given array or list and it will
    detect if elements of a list are not numbers
    
    Argument(s) : 
    ---------------
    -  Values : a list or array that can contain anything 
    ---------------
    Note(s) : 
    - This program can detect any possible errors and rais an exception to make sure it always return the right value 
    using try and except keywords .
    ---------------
    Return(s) : This function return's the maximum value of the elements in a given list or array 
    """ 
    for i in values :   # this line makes sure that max value is indeed a float not a string 
        try: 
            max = float(values[i])
        except: 
            continue
    for i in values: 
        try: 
            if max < float(i): 
                max = float(i)    
        except:
            if type(i) == str : 
                pass
            else: 
                print("Invalid Input !")
    return max

def minvalue(values):
    """This function will return the maximum value within a given array or list and it will 
    detect if elements of a lits are not numbers
        
    Argument(s) : 
    ---------------
    -  Values : a list or array that can contain anything 
    ---------------
    Note(s) : This program can detect any possible errors and rais an exception to make sure it always return the right value 
    using try and except keywords .
    ---------------
    Return(s) : This function return's the minimum value of the elements in a given list or array 
    """   
    for i in values :   # this line makes sure that min value is indeed a float not a string 
        try: 
            min = float(values[i])
        except: 
            continue
    for i in values: 
        try: 
            if min > float(i): 
                min = float(i)    
        except:
            if type(i) == str : 
                pass
            else: 
                print("Invalid Input !")
    return min

def meannvalue(values):
    """This function will calculate the meanvalue (average) of numbers whithin a given list or array 
    
    Argument(s) : 
    ---------------
    -  Values : a list or array that can contain anything 
    ---------------
    Note(s) : This program can detect any possible errors and rais an exception to make sure it always return the right value 
    using try and except keywords .
    ---------------
    Return(s) : This function return's the meanvalue (average)  of the elements in a given list or array 
    """    
    sum = 0
    len_counter = 0
    for i in values : 
        try : 
            i = float(i)
            sum += i
            len_counter += 1.0
            
        except : 
            if type(i) == str : 
                pass
            else: 
                print("Invalid Input !")
                
    return sum / len_counter
            
def countvalue(values,xw):
    """This function will match the variable 'xw' to every single elements of the 
    given list or array and will return the number of matched elements
    
    Argument(s) : 
    ---------------
    -  Values : a list or array that can contain anything 
    - xw : a string to match with the Values 
    ---------------
    Note(s) : This program will not count matched elements in the lists within the Values list (2D array/list)
    ---------------
    Return(s) : This function return's the number of matches with a given string to all elements in a list or array 
    """ 
     
    count = 0   
    for i in values : 
        if i == xw : 
            count += 1 
        
    if count > 0 : 
        return count 
    else : 
        return 0