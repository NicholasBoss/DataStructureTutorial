# The Stack Data Structure

The stack data structure allows for a user to input information, such as letters or numbers in a list which then outputs them
in reverse order. 

For example, if someone wanted to encode a message using a stack in a caesar cipher, and that message was, 'I love you', they would put it in the stack, specify the shift and it would output one of twenty-six different encoded messages. 

The caesar cipher is one of the most basic encoding methods available and is not practical for real world use. The Cipher asks for a shift. That shift takes the text entered and shifts each letter that amount in the alphabet. If it reaches 'z', the shift continues back at 'a' and the same is true in the reverse case.

The following code shows this at work:
```Python
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

encode('I love you')
```


# Your Task

Your task is to create a decoder that will print all possible iterations of the decoded phrase and find out which iteration the decode test case is.

[Stack Task]()

[Stack Solution]()
