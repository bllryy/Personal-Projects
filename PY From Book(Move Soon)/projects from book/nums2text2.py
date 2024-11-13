def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it repeats.\n")

    # get the message
    inString = input("Please enter the unicode message: ")

    # loop thorugh each substring and build unicode message
    chars = []
    for numStr in inString.split():
        codeNum = int(numStr)   # convert digits to a number 
        chars.append(chr(codeNum))
    
    message = "".join(chars)
    print("\nThe decoded message is: ", message)

main()