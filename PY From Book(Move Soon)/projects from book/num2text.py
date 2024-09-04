def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents. \n")

    # get message
    inString = input("Please enter the Unicode-encoded message: ")

    # loop
    message = ""
    for numStr in inString.split():
        codeNum = int(numStr)       # converts digits into number
        message = message + chr(codeNum)    # concatentate character to message 

    print("\The decoded message is:", message)

main()