# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations = []
    lettersUsed = []
    
    if len(sequence) == 1:
        permutations.append(sequence)
        return permutations
    
    #take each char in sequence and add to each permutation of sequence w/o char to aquire string
    else:
        for letter in sequence: #for each letter in sequence string
            if letter not in lettersUsed: #if letter is not being repeated
                
                lettersUsed.append(letter) #letter is being used so add to list
                
                #Create string with the chosen letter taken out
                remainingString =list(sequence)
                remainingString.remove(letter)
                remainingString = ''.join(remainingString)
                
                for permutation in get_permutations(remainingString): #get strings from permutation function to put 'letter' in
                    for i in range(len(permutation)+1): 
                        
                        #create permutation for letter in each position of string
                        string = list(permutation)
                        string.insert(i, letter) #inserts letter at position i
                        string = ''.join(string) #joins with new letter into a string
                        
                        #check if the created permutation has already been added
                        if string not in permutations: 
                            permutations.append(string)
                            
    return permutations
    #add string to list
    #return list
    
    

if __name__ == '__main__':
#    #EXAMPLE
    print('----------------------')
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'bac', 'bca', 'acb', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    print('----------------------')
    example_input = 'cba'
    print('Input:', example_input)
    print('Expected Output:', ['cba', 'bca', 'bac', 'cab', 'acb', 'abc'])
    print('Actual Output:', get_permutations(example_input))
    
    print('----------------------')
    example_input = 'aaa'
    print('Input:', example_input)
    print('Expected Output:', ['aaa'])
    print('Actual Output:', get_permutations(example_input))
    
    print('----------------------')
    example_input = 'aba'
    print('Input:', example_input)
    print('Expected Output:', ['aba', 'baa', 'aab'])
    print('Actual Output:', get_permutations(example_input))
    
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
