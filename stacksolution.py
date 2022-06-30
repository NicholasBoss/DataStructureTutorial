alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
def encode(text): # encode in ceasar cipher
    stack = []
    shift = int(input("Please enter shift (1-26): "))
    for ltr in text:
        if ltr.isalpha():
            location = alpha.find(ltr.lower())
            if ltr.upper() == ltr:
                stack.append(alpha[location + shift].upper())
            else:
                stack.append(alpha[location + shift])
        else:
            stack.append(ltr)
    output = ""
    while len(stack) > 0:
        output += stack.pop()
    print(output)





# will decode the string and return the decoded string using the shift
def decode(text): 
    stack = []
    for shift in range(1,26):
        print(shift, end = " ")
        for ltr in text:
            if ltr.isalpha():
                location = alpha.find(ltr.lower())
                if ltr.upper() == ltr:
                    stack.append(alpha[location - shift].upper())
                else:
                    stack.append(alpha[location - shift])
            else:
                stack.append(ltr)
        output = ""
        while len(stack) > 0:
            output += stack.pop()
        print(output)
                
                



print("Test case 1:")
print("------------")
encode('I love you')
print("------------")
print("Test case 2:")
print("------------")
decode('ois ypif C')
print("------------")
