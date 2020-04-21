import time 

# Returns number of words in string 
def countWords(string): 
    state = OUT 
    wc = 0
  
    # Scan all characters one by one 
    for i in range(len(string)): 
  
        # If next character is a separator,  
        # set the state as OUT 
        if (string[i] == '\n' or string[i] == '\t' or string[i] == ' ' or string[i] == '?' or string[i] == '!' or string[i] == '.' or string[i] == ',' or string[i] == ';' ): 
            state = OUT 
  
        # If next character is not a word  
        # separator and state is OUT, then  
        # set the state as IN and increment  
        # word count 
        elif state == OUT: 
            state = IN 
            wc += 1
  
    # Return the number of words 
    return wc



# Returns number of sentences in string
def countSentences(string): 
    state = OUT
    sc = 0
  
    # Scan all characters one by one 
    for i in range(len(string)): 
  
        # If next character is a sentence ender,  
        # set the state as IN 
        # also considers two sentence enders in a row
        if (string[i] == '?' or string[i] == '!' or string[i] == '.'):
            state = IN

        # Option to add extra logic for Mr. /Mrs. 
  
        # If next character is not a sentence ender
        # then
        # set the state as OUT and increment  
        # sentence count 
        elif (state == IN):
            state = OUT 
            sc += 1
  
    # Return the number of sentences 
    return sc


# Returns number of characters in string(excluding spaces)
def countCharacters(string): 
    cc = 0
    sc = 0
  
    # Scan all characters one by one 
    for i in range(len(string)): 
  
        # If next character is a separator,  
        # count separately
        if (string[i] == '\n' or string[i] == '\t' or string[i] == ' '): 
            sc += 0

        # If next character is not a seperator 
        # increment count
        else:
            cc += 1
  
    # Return the number of words 
    return cc



# Driver Code 
start = time.perf_counter()
fileObject = open("piney.txt", "r")
data = fileObject.read()

OUT = 0
IN = 1
print("No. of words : " + str(countWords(data))) 
print("No. of sentences : " + str(countSentences(data))) 
print("No. of characters : " + str(countCharacters(data))) 

finish = time.perf_counter()

print(f'Finished in {round(finish-start,10)} seconds(s)')
