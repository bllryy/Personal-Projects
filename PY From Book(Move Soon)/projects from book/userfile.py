def main():
    print("This program creates a file of usernames from a ")
    print("file of names")

    # get names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # open
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process
    for line in infile:
        # get first and last names from line
    first, last = line.split
        # create usernames 
    uname = (first[0]+last[:7]).lower()
        # write it to output file
    print(uname, file=outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

main()