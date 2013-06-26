
# create a list of random 0's and 1's, 8 elements long
def rand_binary(): 
    r_byte = [0,0,0,0,0,0,0,0]
    for num in range(0,8):
        r_byte[num] = random.randint(0,1)
    display(r_byte)

# display the random byte and get the answer from the user
def display(p):
    answer = raw_input('Guess the decimal value of: '+ str(p))
    if(str(correct(p))==answer):
        print('You got it!!  You understand how to convert from binary to decimal')
    else: 
        print('sorry, that is not correct. you should do the following...')
        showAns(p)

# returns true if the guess is correct and false if not
def correct(binary):
    RightAns = 0
    for dig in range(0,8):
        RightAns += binary[dig]*(2**(7-dig))    
    return RightAns


#displays the algorithm to properly obtaining the decimal value of the binary number
def showAns(binary):
    print('this is the math you would do to get the answer: ')
    for dig in range(0,8):
        print('adding: ' + str(binary[dig]) + '*2^' +str(2**(7-dig)))
    print('when I add those all up I get: '+ str(correct(binary)))
    
