def main():
    print("Please enter the message to encode: ")
    print("of numbers representing the Unicode encoding of the message. \n")

    #get the message
    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes: ")

    #loop through message and print
    for ch in message:
        print(ord(ch), end=" ")
    
    print() # blank line

main()